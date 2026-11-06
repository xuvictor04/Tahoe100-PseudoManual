---
type: concept
tags: [concept, p53, cell-lines, power, design]
status: current
---

# p53 nullification in cancer cell lines

Why a panel of cancer cell lines is mostly p53-dead, the routes other than [[TP53]] mutation that get it
there, and the consequence for anything read from this data: a test that needs working p53 is a test on
**11 to 17 lines, not 50**.

> [!summary] In one line
> 33 of the 50 lines in [[Tahoe-100M]] carry a TP53 driver mutation, and of the 17 that do not, 6 still fail
> to mount a normal p53 response — because losing p53 *output* does not require mutating *TP53*.

## Why the panel is mostly dead

p53 enforces the arrest-and-apoptosis response to the exact stresses that accompany becoming a tumour —
oncogene activation, replication stress, telomere crisis, aneuploidy. A cell that keeps it intact under that
load does not proliferate; a cell that loses it does. Then the line is established in culture, which selects
again, on the same axis. So a cancer line panel is not a random sample of human cells with respect to p53:
it is enriched, twice, for cells that have found a way around it. TP53 is the most frequently mutated gene
in human cancer for this reason, and 66% of this panel carries a driver mutation in it.

The important corollary is that **mutating TP53 is one route, not the route**. Any lesion that stops p53
protein from accumulating, from being activated, or from reaching its promoters produces the same phenotype
with a wild-type TP53 sequence. A genotype column will call those lines wild-type, and they will behave like
mutants.

## The routes, and where they appear in this panel

[[The p53 pathway]] has the mechanism; this is the inventory, from the earlier MG53/p53 study's per-line table
(`per_line_p53_state.csv`, populated for the 17 genotype-wild-type lines).

| Route | How it lowers p53 output | In this panel |
|---|---|---|
| **TP53 mutation** | missense alleles lose canonical transactivation; truncating, splice and deletion alleles leave no protein | **33/50** — 20 missense-only, 13 truncating/splice/deletion |
| **[[CDKN2A]] / ARF loss** | p14-ARF normally sequesters [[MDM2]] in the nucleolus; without it MDM2 runs unopposed and basal p53 falls | **9/17** wild-type lines by the table's count |
| **[[MDM2]] gain** | more E3 ligase, faster p53 turnover | RKO (rel CN 1.41), LoVo (1.43) |
| **[[MDM4]] amplification** | MDMX binds the p53 transactivation domain and blocks it without degrading p53 | C32 **amplified** (rel CN 2.85, GISTIC +2), SNU-1 (highest MDM4 mRNA of the 50, log2 TPM+1 2.13), H4 (1.85), NCI-H460 (1.71), CHP-212 (1.54) |
| **[[PPM1D]] (WIP1) gain** | dephosphorylates ATM, CHK2 and p53 Ser15 — actively *terminates* damage signalling | A-172 (GISTIC +2), CHP-212 (rel CN 2.30) |
| **[[ATM]] loss** | the kinase that activates p53 after double-strand breaks | SNU-1 (L1154fs heterozygous, VAF 0.58, MSI line), C32 (GISTIC −2, rel CN 0.54), A-172 (ATM/CHEK2 GISTIC −2 in CCLE 2019, flagged near-tetraploid and **not confirmed**) |
| **[[CHEK2]] loss** | the same arm, one step down | C32 (S422fs), LoVo (T389fs subclonal, VAF 0.14), A-172 (same unconfirmed GISTIC call) |
| **Unidentified** | — | Hs 766T: wild-type TP53, functionally unresponsive, Nutlin-3a-resistant (GDSC AUC 0.954), CDKN2A mRNA in the mutant range |

The CDKN2A count depends on what counts as loss. Eight of the 17 wild-type lines carry a homozygous CDKN2A
deletion or deletion/stop-loss (NCI-H460, A549, A498, H4, A-172, C32, LOX-IMVI, A-427); three more have low
CDKN2A mRNA consistent with promoter silencing (RKO, SW48, LS 180); Hs 766T has a splice variant with the
gene intact and mRNA high. The table reports **9/17**; counting silencing brings it to 11 or 12. Only SNU-1
and CHP-212 are recorded as CDKN2A-intact.

Note how often the routes **stack**. C32 carries CDKN2A deletion, MDM4 amplification, ATM loss and a CHEK2
frameshift and is still called fully functional on inducibility. A-172 and CHP-212 each combine two routes
and land in the *uncertain* band. Pathway lesions shift the quantitative level of p53 output; they do not
reliably switch it off, which is why a graded per-line read-out is worth more than the genotype column.

## Nutlin as the external check

Nutlin-3a blocks the MDM2–p53 interaction, so it only kills a line that has p53 available to stabilise.
GDSC Nutlin-3a AUC is therefore an independent, protein-level read on the same question, and in this panel
it mostly agrees with the mRNA-based call: sensitive for H4 (0.627), CHP-212 (0.667), RKO (0.778),
A549 (0.802), LOX-IMVI (0.805), NCI-H460 (0.835); resistant for the two lines flagged as damped,
SNU-1 (0.948) and HepG2/C3A (0.966), and for Hs 766T (0.954). It is a useful cross-check precisely because a
24 h mRNA snapshot cannot see p53 protein at all.

## What this does to the sample size

| Test needs | n | Which lines |
|---|---|---|
| any line | 50 | the whole panel |
| wild-type TP53 **sequence** | **17** | the genotype-wild-type lines |
| p53 that actually **responds** | **11** | the panel-responsive lines, all genotype-wild-type |
| a p53-**null** control arm | **10** | truncating, splice-disrupted or deleted |

The cost is not linear in n, because the lines are the clusters. Inference across lines uses the line as the
unit, and eleven clusters is few-cluster territory: intervals are wide, and a null result from 11 lines is mostly
a bound and has to be reported as one.

The dead lines are not wasted. Their value is as a **control arm**: a line with no intact TP53 allele cannot
mount a p53 response, so whatever a "p53 target" does in it is, by construction, not p53.

## In this vault

Each cell-line note gives its TP53 status (`altered` when the Tahoe cell-line metadata lists a TP53 driver,
`wild type` when the line is listed without one, `unknown` otherwise) and its driver genes. Each gene note's
per-line table shows TP53 status next to the line's response, so a p53 target that rises only in wild-type lines
is visible at a glance. TP53 status is never used to build the vector space or the modules.

> [!warning] One circularity to keep in view
> A p53 programme or a p53-activating drug set selected **using the binary WT/altered labels** will push altered
> lines toward "unresponsive" and wild-type lines toward "responsive", so agreement between genotype and a
> functional call built on it is partly built in. See [[Cross-fitting and circularity]].

## Sources

- The earlier MG53/p53 study: `mg53_p53/findings/tables/p53_nullification.csv` (panel-level counts),
  `per_line_p53_state.csv` (`pathway_context`, `gdsc_nutlin3a_auc`, `expected_p53_output_vs_null`,
  `confidence`), `null_reference_lines.csv` (the ten-line control arm), `PER_LINE_p53_FUNCTION.md`.
- tahoemap: `tables/lines.parquet` (`tp53_status`, `drivers`, `driver_changes`).
