---
symbol: "TRIAP1"
type: "gene"
col: 10013
ensembl_id: "ENSG00000170855"
name: "TP53 regulated inhibitor of apoptosis 1"
location: "12q24.31"
module: 62
arm: "+"
pooled_cpm: 11.27
n_lines_expressing: 50
n_dd_up: 16
n_dd_down: 0
n_dd_up_clean: 6
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 9
direction_downstream: 2
tags: ["gene", "module/062", "written"]
generated_by: "tahoemap"
---

# TRIAP1

*TP53 regulated inhibitor of apoptosis 1* — 12q24.31

> [!summary] In one line
> TRIAP1 is a small p53-induced protein that works inside mitochondria as half of a lipid-transfer complex, and its effect on the cell is to keep it alive — a survival output of p53, not a death one.

## What it is

TRIAP1 — TP53-regulated inhibitor of apoptosis 1, originally named p53CSV for "p53-inducible cell-survival factor" — is a 76-residue protein of the Mdm35 family. It was found as a p53-induced gene whose knockdown increased apoptosis and whose overexpression protected cells against DNA-damage-induced death, with the induction reported to be selective for *mild* genotoxic stress rather than severe damage. That conditionality places it in the arm of the p53 response that attempts survival rather than the arm that commits to death.

Its best-defined job came later and is structural. In the mitochondrial intermembrane space TRIAP1 heterodimerises with PRELID1 and with PRELID3B (SLMO2); these complexes bind and shuttle phosphatidic acid across the intermembrane space, delivering the precursor for cardiolipin synthesis at the inner membrane. Losing TRIAP1 or its PRELI partner lowers cardiolipin, which loosens cytochrome *c* from the inner membrane and leaves cells primed for apoptosis. The anti-apoptotic phenotype therefore has a lipid-level explanation that does not require TRIAP1 to touch the apoptotic machinery at all. An earlier proposal has it binding HSP70 and, through that, dampening APAF1-dependent apoptosome formation; that has much thinner support.

## What is uncertain

Whether TRIAP1 is a *direct* p53 target is likely but not settled: a response element has been reported within the gene rather than in an upstream promoter, and sources disagree over whether it sits in the second intron or the second exon — not a discrepancy to resolve by guessing. The two accounts of its anti-apoptotic action have not been reconciled, and the HSP70/APAF1 one rests on essentially a single study. The "mild damage only" induction pattern comes from the founding work and has not, as far as I can establish, been systematically retested across stress types. And most of the functional work is overexpression and knockdown in cultured cells; what TRIAP1 loss does in a whole animal is much less clear than its biochemistry.

## References

- Park & Nakamura, 2005, *Cancer Research* — identified p53CSV/TRIAP1 as a p53-inducible gene required for survival after low-level genotoxic stress, and proposed the HSP70/APAF1 route.
- Potting et al., 2013, *Cell Metabolism* — showed TRIAP1/PRELI complexes transport phosphatidic acid within mitochondria, and that losing them depletes cardiolipin and sensitises cells to apoptosis.

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 16 drug-doses (10 with an alert ⚠); the strongest is [[Topotecan (hydrochloride) (drug)]] 5 µM: 3.05× (z +11.5, q 6e-28, up in 37 of 39 measured lines) ⚠ toxic. The strongest without an alert is [[Harringtonine (drug)]] 0.5 µM: 2.17× (z +8.3, q 2e-14, up in 42 of 46 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 3 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Ivabradine (hydrochloride) (drug)]] 0.5 µM in 1 line (HepG2/C3A 0.0832×; ⚠ transcription drop; unreliable plate only); [[Niclosamide (olamine) (drug)]] 5 µM in 1 line (RKO 0.100×; ⚠ toxic; cell-cycle shift, would explain all of this change); [[Apalutamide (drug)]] 0.05 µM in 1 line (HepG2/C3A 0.0863×).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[DTWD1]] (+0.66, fdr 1e-05), [[DCP1B]] (+0.64, fdr 7e-06), [[PHLDA3]] (+0.63, fdr 1e-05); moves opposite to [[EPB41L2]] (-0.44, fdr 1e-04).
> It is in [[Module 062]], a single-armed module (p53 targets up).
> Probable direction (from the cell lines, not proof of direct regulation): 9 arrows point to it, the strongest [[TP53]] → it (grade A ⚠); 2 go from it, the strongest it → [[ANKRA2]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 16 in all, 10 with an alert ⚠; shown: the 15 strongest. 16 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 10 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10013.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **3.05×** | +11.5 | 6e-28 | 37/39 (NCI-H460, A498, …) | rises with dose | cell-cycle shift (explains ~6% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **2.17×** | +8.3 | 2e-14 | 42/46 (LS 180, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here) |
| [[Selinexor (drug)]] 5 µM |  | **1.61×** | +7.2 | 1e-10 | 32/48 (NCI-H460, A549, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~44% of this change | **1.81×** | +6.4 | 3e-08 | 30/46 (LS 180, SW480, …) | rises with dose |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~47% of this change | **1.78×** | +6.2 | 7e-08 | 27/47 (NCI-H1792, NCI-H2347, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~43% of this change | **1.71×** | +5.7 | 9e-07 | 28/47 (PANC-1, NCI-H2030, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.68×** | +5.6 | 2e-06 | 29/47 (A549, LS 180, …) | all doses, flat |  |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~66% of this change | **1.44×** | +5.5 | 3e-06 | 24/46 (LoVo, A-427, …) | all doses, flat | composition shift |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~44% of this change | **1.66×** | +5.2 | 1e-05 | 27/46 (NCI-H2030, HEC-1-A, …) | all doses, stronger at high dose | composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.60×** | +5.1 | 2e-05 | 22/44 (LoVo, NCI-H2030, …) | all doses, flat | cell-cycle shift (explains ~13% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~40% of this change | **1.58×** | +4.9 | 5e-05 | 25/42 (hTERT-HPNE, A-172, …) | inconsistent across doses | low cells (technical?) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~58% of this change | **1.55×** | +4.7 | 1e-04 | 22/47 (LS 180, LoVo, …) | rises with dose | composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~50% of this change | **1.43×** | +3.9 | 0.005 | 17/46 (LoVo, LOX-IMVI, …) | rises with dose |  |
| [[Harringtonine (drug)]] 0.05 µM |  | **1.47×** | +3.9 | 0.005 | 17/44 (NCI-H460, LoVo, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Cytarabine (hydrochloride) (drug)]] 5 µM |  | **1.38×** | +3.3 | 0.037 | 17/46 (NCI-H460, C32, …) | top dose only | cell-cycle shift (explains ~16% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 3 in all, none with an alert. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 10013.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 3 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Ivabradine (hydrochloride) (drug)]] 0.5 µM in 1 line (HepG2/C3A 0.0832×; ⚠ transcription drop; unreliable plate only); [[Niclosamide (olamine) (drug)]] 5 µM in 1 line (RKO 0.100×; ⚠ toxic; cell-cycle shift, would explain all of this change); [[Apalutamide (drug)]] 0.05 µM in 1 line (HepG2/C3A 0.0863×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 5 µM |  | 0.785× | -3.7 | 0.13 | 14/48 (MIA PaCa-2, LS 180, …) | top dose only |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | 0.812× | -3.2 | 0.37 | 16/46 (AsPC-1, H4, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Sivelestat (sodium tetrahydrate) (drug)]] 5 µM |  | 0.742× | -3.1 | 0.37 | 8/47 (AsPC-1, LS 180, …) | top dose only | plate-row cell shift |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.37 per unit of S-phase module lfc, +0.26 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10013. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HepG2_C3A (line)]] | wt | 13.2 | 0 | 2 (1 ⚠) | — | [[Ivabradine (hydrochloride) (drug)]] 0.5 µM 0.0832× (z -10.6) ⚠ transcription drop; unreliable plate only · without an alert: [[Apalutamide (drug)]] 0.05 µM 0.0863× (z -9.7) |
| [[NCI-H460 (line)]] | wt | 15.3 | 2 (1 ⚠) | 0 | [[Topotecan (hydrochloride) (drug)]] 5 µM 5.77× (z +10.7) ⚠ toxic · without an alert: [[Selinexor (drug)]] 5 µM 3.18× (z +10.4) | — |
| [[A-172 (line)]] | wt | 11.9 | 1 (1 ⚠) | 0 | [[Topotecan (hydrochloride) (drug)]] 5 µM 5.53× (z +8.6) ⚠ toxic | — |
| [[A498 (line)]] | wt | 16.9 | 1 (1 ⚠) | 0 | [[Topotecan (hydrochloride) (drug)]] 5 µM 5.12× (z +9.8) ⚠ toxic | — |
| [[HS-578T (line)]] | alt | 6.70 | 0 | 1 (1 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.0891× (z -9.5) ⚠ cell-cycle shift, explains ~0% of this change |
| [[LoVo (line)]] | wt | 19.0 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.74× (z +9.0) ⚠ cell-cycle shift, explains ~66% of this change | — |
| [[LOX-IMVI (line)]] | wt | 14.6 | 1 (1 ⚠) | 0 | [[Topotecan (hydrochloride) (drug)]] 5 µM 5.50× (z +8.9) ⚠ toxic | — |
| [[RKO (line)]] | wt | 11.1 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.100× (z -10.0) ⚠ toxic; cell-cycle shift, would explain all of this change |
| [[A-427 (line)]] | wt | 18.6 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 18.8 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 8.48 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 5.89 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 9.81 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 8.34 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 9.13 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 8.41 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 17.0 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 5.67 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 16.2 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 9.66 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 7.28 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 6.79 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 6.08 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 7.74 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 11.6 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 9.43 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 10.2 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 21.9 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 7.79 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 7.02 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 7.96 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 22.4 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 8.99 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 8.89 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 13.4 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 11.7 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 12.5 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 6.84 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 9.08 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 7.68 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 10.7 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 6.60 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 8.33 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 6.87 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 8.01 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 10.6 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 8.50 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 10.4 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 17.9 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 9.93 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10013), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*99 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DTWD1]] | +0.66 | +0.56 / +0.69 | both halves | 1e-05 |  |
| [[DCP1B]] | +0.64 | +0.61 / +0.73 | both halves | 7e-06 |  |
| [[PHLDA3]] | +0.63 | +0.51 / +0.66 | both halves | 1e-05 | pathway: HALLMARK_P53_PATHWAY |
| [[RPS27L]] | +0.62 | +0.61 / +0.63 | both halves | 7e-06 | pathway: HALLMARK_P53_PATHWAY |
| [[EDA2R]] | +0.61 | +0.54 / +0.63 | both halves | 1e-05 |  |
| [[PTCHD4]] | +0.60 | +0.49 / +0.69 | both halves | 1e-05 |  |
| [[NTPCR]] | +0.60 | +0.37 / +0.72 | both halves | 8e-05 |  |
| [[TP53TG1]] | +0.59 | +0.46 / +0.61 | both halves | 3e-05 |  |
| [[FDXR]] | +0.59 | +0.53 / +0.63 | both halves | 1e-05 | pathway: HALLMARK_P53_PATHWAY |
| [[MDM2]] | +0.59 | +0.58 / +0.68 | both halves | 8e-06 | pathway: HALLMARK_P53_PATHWAY |
| [[RRM2B]] | +0.58 | +0.59 / +0.59 | both halves | 7e-06 |  |
| [[PURPL]] | +0.58 | +0.44 / +0.66 | both halves | 3e-05 |  |

## Genes that move opposite

*1 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[EPB41L2]] | -0.44 | -0.32 / -0.44 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*9 arrows, 9 of them with an alert ⚠; grade A 1, B 7, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TP53]] | A | TP53 activity strengthens TRIAP1's drug response | recorded loss-of-function mutation of TP53 in 31 lines vs 17 not recorded | the TP53-altered lines respond 0.79× as strongly (z diff +0.46); strongest at Topotecan (hydrochloride) 5 µM: 2.51x vs 4.29x (z diff +3.3) | 0.049 | ⚠ within organs, on part of the lines; TP53 not expressed in 3 of the 33 altered lines; target measured in part of the lines; both ways; artifact flags |
| [[EDA2R]] | B | EDA2R activity raises TRIAP1's level | lines that do not express EDA2R (28) vs lines expressing it (22) | 1.30× lower at baseline in the lines without EDA2R | 0.020 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000253503, SLC6A15, WNK3 |
| [[CYFIP2]] | B | CYFIP2 activity raises TRIAP1's level | lines that do not express CYFIP2 (9) vs lines expressing it (41) | 1.49× lower at baseline in the lines without CYFIP2 | 0.034 | ⚠ within organs, on part of the lines; also absent: ENSG00000226965, GRIN2C, SEMA6A |
| [[PINCR]] | B | PINCR activity raises TRIAP1's level | lines that do not express PINCR (29) vs lines expressing it (21) | 1.36× lower at baseline in the lines without PINCR | 0.047 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: PTCHD4, ENSG00000269729, PCK1 |
| [[PURPL]] | B | PURPL activity raises TRIAP1's level | lines that do not express PURPL (25) vs lines expressing it (25) | 1.33× lower at baseline in the lines without PURPL | 0.056 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: MIR99AHG, ENSG00000286385, RPS4Y1 |
| [[ACTA2]] | B | ACTA2 activity raises TRIAP1's level | lines that do not express ACTA2 (11) vs lines expressing it (39) | 1.35× lower at baseline in the lines without ACTA2 | 0.057 | ⚠ within organs, on part of the lines; also absent: FAS; maybe low, not absent |
| [[PINCR]] | B | PINCR activity strengthens TRIAP1's drug response | lines that do not express PINCR (29) vs lines expressing it (19) | the lines without PINCR respond 0.82× as strongly (z diff +0.40); strongest at Topotecan (hydrochloride) 5 µM: 2.48x vs 4.06x (z diff +2.9) | 0.076 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: PTCHD4, ENSG00000269729, PCK1; target measured in part of the lines; both ways; artifact flags |
| [[FDXR]] | B | FDXR activity raises TRIAP1's level | lines that do not express FDXR (8) vs lines expressing it (42) | 1.39× lower at baseline in the lines without FDXR | 0.080 | ⚠ within organs, on part of the lines; also absent: GRIN2C, MCM10; maybe low, not absent |
| [[TP53]] | C | TP53 activity raises TRIAP1's level | recorded loss-of-function mutation of TP53 in 33 lines vs 17 not recorded | 1.52× lower at baseline in the TP53-altered lines | 0.645 over the table, 0.016 within its group | ⚠ within its group only (a lead); within organs, on part of the lines; TP53 not expressed in 3 of the 33 altered lines |

### Downstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 0, C 2.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ANKRA2]] | C | TRIAP1's natural level strengthens ANKRA2's drug response | TRIAP1's natural level across 48 lines (lineage-adjusted; a glimpse) | r +0.66, reverse +0.16; direction clear | 0.039 | ⚠ tissue can mimic it; precision caveat; rises at some drug-doses, falls at others |
| [[TP53I3]] | C | TRIAP1's natural level strengthens TP53I3's drug response | TRIAP1's natural level across 46 lines (lineage-adjusted; a glimpse) | r +0.67, reverse +0.28; direction not clear | 0.044 | ⚠ tissue can mimic it; precision caveat; rises at some drug-doses, falls at others; direction unclear |

## Where it sits

- **Module**: [[Module 062]] — p53 targets up; 78 genes; every member is in the + arm (projection on the module's main direction 0.620). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.30; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-15.3, 35.5); signed map (41.3, -24.1). **Vector** length 82.8, 17.4% of its response variance represented; |z| ≥ 3 in 848 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Selinexor (drug)]] 5 µM |  | +6.4 | +7.2 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +6.4 | +11.5 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +4.6 | +5.6 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | +4.4 | +8.3 |
|  | [[Idarubicin (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift | +4.1 | +2.6 |
|  | [[Amsacrine (drug)]] 5 µM |  | +3.2 | +2.7 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +2.6 | +3.9 |
|  | [[Ponatinib (drug)]] 5 µM |  | +1.4 | +0.3 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.05 µM |  | +1.3 | +0.9 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -3.5 | -3.2 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -2.2 | +0.2 |
|  | [[Auranofin (drug)]] 5 µM |  | -2.1 | +1.7 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -2.0 | -0.6 |
|  | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.0 | -0.1 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -1.5 | -3.7 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | -1.3 | -0.9 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | -1.3 | -1.9 |
|  | [[Baicalin (drug)]] 5 µM |  | -1.2 | -1.0 |

## What is on record

|  |  |
|---|---|
| Name | TP53 regulated inhibitor of apoptosis 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 12q24.31 — chr12:120,443,964-120,446,384 (-) |
| Ensembl biotype | protein_coding |
| Also known as | P53CSV, WF-1, HSPC132, p53CSV, MDM35 |
| Hallmark sets | P53_PATHWAY |
| Reactome | 4 pathways, smallest: TP53 Regulates Transcription of Genes Involved in Cytochrome C Release; TP53 Regulates Transcription of Cell Death Genes; Mitochondrial protein degradation |
| Matched by | ensembl_id |

**Function**, from UniProt [O43715](https://www.uniprot.org/uniprotkb/O43715) (TP53-regulated inhibitor of apoptosis 1):

> Involved in the modulation of the mitochondrial apoptotic pathway by ensuring the accumulation of cardiolipin (CL) in mitochondrial membranes. In vitro, the TRIAP1:PRELID1 complex mediates the transfer of phosphatidic acid (PA) between liposomes and probably functions as a PA transporter across the mitochondrion intermembrane space to provide PA for CL synthesis in the inner membrane. Likewise, the TRIAP1:PRELID3A complex mediates the transfer of phosphatidic acid (PA) between liposomes (in …

**Summary**, from NCBI Gene [51499](https://www.ncbi.nlm.nih.gov/gene/51499):

> Enables p53 binding activity. Contributes to phosphatidic acid transfer activity. Involved in several processes, including DNA damage response, signal transduction by p53 class mediator; negative regulation of apoptotic signaling pathway; and positive regulation of phospholipid transport. Located in mitochondrial intermembrane space. Part of protein-containing complex. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:26937](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:26937) · Entrez [51499](https://www.ncbi.nlm.nih.gov/gene/51499) · UniProt [O43715](https://www.uniprot.org/uniprotkb/O43715) · Ensembl [ENSG00000170855](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000170855)

## Data

Gene col 10013: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10013); `tables/drug_effects.parquet` (19 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10013, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10013]; `tensor/DDL_lfc|DDL_z.npy` [10013]; `embed/gene_vectors.npy` [10013]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10013 or target_col == 10013). Every well: [[TRIAP1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. The written part above is `tahoemap/vault_seed/genes/TRIAP1.md`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
