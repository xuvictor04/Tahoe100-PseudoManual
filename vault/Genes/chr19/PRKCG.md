---
symbol: "PRKCG"
type: "gene"
col: 4747
ensembl_id: "ENSG00000126583"
name: "protein kinase C gamma"
location: "19q13.42"
module: 53
arm: "+"
pooled_cpm: 8.58
n_lines_expressing: 45
n_dd_up: 12
n_dd_down: 1
n_dd_up_clean: 8
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 2
direction_downstream: 4
tags: ["gene", "module/053", "written"]
generated_by: "tahoemap"
---

# PRKCG

*protein kinase C gamma* — 19q13.42

> [!note] Written for the earlier MG53/p53 study
> The written section below was written for an earlier study on the same data (MG53/TRIM72 and p53). Where it mentions a score, a rank, a regulon, an association or "this batch", it refers to that study's analysis (transcription-factor activity inferred from target sets, and MG53 as the exposure), which tahoemap does not compute. This run's own numbers are in the generated sections below.

> [!summary] In one line
> PRKCG encodes PKCγ, a calcium- and diacylglycerol-dependent protein kinase C isoform expressed almost exclusively in neurons and most abundant in cerebellar Purkinje cells.

## What it is

A conventional PKC: tandem C1 domains that bind diacylglycerol, a C2 domain that binds calcium, and a kinase domain held off by a pseudosubstrate clamp until both second messengers arrive. Activation downstream of Gq–PLCβ signalling, including mGluR1 in Purkinje cells, drives membrane translocation. Unlike the other conventional isoforms its expression is confined to the central nervous system, so most of what is known comes from cerebellar physiology: long-term depression and developmental synapse elimination. Clinically, dominant missense mutations, concentrated in the regulatory C1 domains but also found in the catalytic half, cause spinocerebellar ataxia type 14, a slowly progressive and largely pure cerebellar ataxia.

## What is uncertain

Whether PRKCG is a p53 target at all. The label is curation; I know of no primary work showing p53 occupancy at this gene or clean induction by p53, and the data-defined p53 programme of the earlier MG53/p53 study did not contain it. The mechanism of SCA14 is also unsettled — increased, unchanged and mislocalisation-driven phenotypes have all been reported for different mutants. And PRKCG carries a readthrough-geometry flag — it sits within 20 kb 3′ of a much higher-expressed same-strand gene, so some reads credited to it may not be its own ([[Readthrough spillover]]).

## References

- Chen et al., 2003, American Journal of Human Genetics — missense mutations in the PKCγ regulatory domain cause dominant non-episodic cerebellar ataxia (SCA14).
- Abeliovich et al., 1993, Cell — hippocampal long-term potentiation is modified in PKCγ-mutant mice.

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 12 drug-doses (4 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 2.74× (z +8.7, q 2e-15, up in 25 of 38 measured lines).
> Pooled over the cell lines (median), lowered significantly by 1 drug-dose (none with an alert); the strongest is [[Bortezomib (drug)]] 0.05 µM: 0.504× (z -4.0, q 0.044, down in 20 of 39 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Digitoxin (drug)]] 5 µM in 1 line (C-33 A 0.0846×; ⚠ toxic; transcription drop); [[Digitoxin (drug)]] 0.05 µM in 1 line (NCI-H2030 0.0505×); [[Bendamustine (drug)]] 0.5 µM in 1 line (J82 0.0518×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[LDHC]] (+0.75, fdr 7e-06), [[TRIM72]] (+0.75, fdr 7e-06), [[FGF18]] (+0.74, fdr 7e-06); moves opposite to [[TRIP4]] (-0.54, fdr 1e-05).
> It is in [[Module 053]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[HCN2]] → it (grade B ⚠); 4 go from it, the strongest it → [[POLG2]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 4 with an alert ⚠. 12 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4747.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **2.74×** | +8.7 | 2e-15 | 25/38 (PANC-1, A-172, …) | top dose only | cell-cycle shift (explains ~10% here); composition shift; position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.67×** | +8.5 | 7e-15 | 35/38 (A-172, PANC-1, …) | top dose only | cell-cycle shift (explains ~5% here); position effect removed |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | **1.28×** | +5.1 | 7e-05 | 23/43 (HEC-1-A, A498, …) | inconsistent across doses |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **2.17×** | +4.7 | 3e-04 | 18/39 (PANC-1, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.73×** | +4.7 | 3e-04 | 18/41 (PANC-1, NCI-H460, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **2.09×** | +4.3 | 0.001 | 17/35 (MIA PaCa-2, CFPAC-1, …) | top dose only | cell-cycle shift (explains ~8% here) |
| [[Filgotinib (drug)]] 5 µM |  | **1.99×** | +4.2 | 0.002 | 20/43 (A498, HepG2/C3A, …) | rises with dose |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **1.84×** | +3.7 | 0.015 | 16/42 (PANC-1, J82, …) | inconsistent across doses |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.72×** | +3.3 | 0.063 | 17/42 (PANC-1, J82, …) | inconsistent across doses | cell-cycle shift (explains ~12% here) |
| [[Pyridoxine (drug)]] 0.05 µM |  | **1.76×** | +3.1 | 0.094 | 10/40 (HepG2/C3A, HOP62, …) | inconsistent across doses | position effect removed |
| [[Harringtonine (drug)]] 5 µM |  | **1.70×** | +3.1 | 0.094 | 14/39 (PANC-1, LoVo, …) | top dose only | cell-cycle shift (explains ~20% here); composition shift |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **2.64×** | +3.1 | 0.095 | 5/17 (PANC-1, MIA PaCa-2, …) | top dose only | noisy plate (z scaled); position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 4 in all, none with an alert. 1 of them lowers it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 4747.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Digitoxin (drug)]] 5 µM in 1 line (C-33 A 0.0846×; ⚠ toxic; transcription drop); [[Digitoxin (drug)]] 0.05 µM in 1 line (NCI-H2030 0.0505×); [[Bendamustine (drug)]] 0.5 µM in 1 line (J82 0.0518×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Bortezomib (drug)]] 0.05 µM |  | **0.504×** | -4.0 | 0.044 | 20/39 (KATO III, A498, …) | inconsistent across doses | cell-cycle shift (explains ~12% here) |
| [[vincristine (drug)]] 0.05 µM |  | 0.567× | -3.3 | 0.20 | 11/39 (LOX-IMVI, KATO III, …) | inconsistent across doses | position effect removed |
| [[NVP-BHG712 (drug)]] 0.05 µM |  | 0.575× | -3.2 | 0.20 | 11/42 (NCI-H2030, A498, …) | inconsistent across doses | position effect removed |
| [[Digitoxin (drug)]] 0.05 µM |  | 0.594× | -3.2 | 0.20 | 16/40 (NCI-H2030, NCI-H1573, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.26 per unit of S-phase module lfc, +0.12 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4747. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 8.71 | 5 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 21.9× (z +21.8) | — |
| [[A-172 (line)]] | wt | 5.85 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 10.2× (z +11.6) | — |
| [[C-33 A (line)]] | alt | 19.4 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0846× (z -10.6) ⚠ toxic; transcription drop |
| [[J82 (line)]] | alt | 4.60 | 0 | 1 | — | [[Bendamustine (drug)]] 0.5 µM 0.0518× (z -8.9) |
| [[NCI-H2030 (line)]] | alt | 11.3 | 0 | 1 | — | [[Digitoxin (drug)]] 0.05 µM 0.0505× (z -9.3) |
| [[A-427 (line)]] | wt | 15.5 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 22.7 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 9.74 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 2.67 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 3.16 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 3.54 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 8.42 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 7.80 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 3.60 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 1.44 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 3.71 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 8.85 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 17.3 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 19.2 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 4.92 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 10.3 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 5.75 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 8.74 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 7.30 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 19.8 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 5.08 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 11.9 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 1.13 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 7.04 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 7.42 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 8.51 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 5.85 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 11.0 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 1.40 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 4.36 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 7.97 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 13.8 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 4.29 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 3.45 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 13.0 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 11.9 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 3.40 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 1.69 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 4.31 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 13.0 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 3.58 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 6.14 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 14.5 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 1.98 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 9.10 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4747), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*99 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LDHC]] | +0.75 | +0.75 / +0.75 | both halves | 7e-06 |  |
| [[TRIM72]] | +0.75 | +0.73 / +0.75 | both halves | 7e-06 |  |
| [[FGF18]] | +0.74 | +0.75 / +0.72 | both halves | 7e-06 | pathway: Intracellular signaling by second messengers |
| [[SEMA4A]] | +0.74 | +0.73 / +0.74 | both halves | 7e-06 |  |
| [[FNDC7]] | +0.73 | +0.72 / +0.72 | both halves | 7e-06 |  |
| [[IQCN]] | +0.72 | +0.73 / +0.70 | both halves | 7e-06 |  |
| [[MIR9-1HG]] | +0.71 | +0.71 / +0.72 | both halves | 7e-06 |  |
| [[PYGM]] | +0.71 | +0.70 / +0.68 | both halves | 7e-06 |  |
| [[GRAMD2A]] | +0.71 | +0.67 / +0.72 | both halves | 7e-06 |  |
| [[FOSB]] | +0.70 | +0.66 / +0.71 | both halves | 7e-06 | **novel candidate** |
| [[CPNE9]] | +0.69 | +0.73 / +0.66 | both halves | 7e-06 |  |
| [[ROPN1L]] | +0.67 | +0.67 / +0.64 | both halves | 7e-06 |  |

## Genes that move opposite

*1 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TRIP4]] | -0.54 | -0.50 / -0.52 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 1, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HCN2]] | B | HCN2 activity raises PRKCG's level | lines that do not express HCN2 (6) vs lines expressing it (44) | 2.31× lower at baseline in the lines without HCN2 | 0.037 | ⚠ within organs, on part of the lines; also absent: ENSG00000267131, USP31, PRELID3A; maybe low, not absent |
| [[KIF17]] | C | KIF17 activity raises PRKCG's level | lines that do not express KIF17 (3) vs lines expressing it (47) | 2.97× lower at baseline in the lines without KIF17 | 0.060 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: DPF1, CNTNAP1, CFL2; maybe low, not absent; its own permutation p |

### Downstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 4, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[POLG2]] | B | PRKCG activity raises POLG2's level | lines that do not express PRKCG (5) vs lines expressing it (45) | 1.56× lower at baseline in the lines without PRKCG | 0.044 | ⚠ within organs, on part of the lines; also absent: SLC36A4, DBN1, CEP41; maybe low, not absent |
| [[CENPBD2P]] | B | PRKCG activity raises CENPBD2P's level | lines that do not express PRKCG (5) vs lines expressing it (45) | 1.27× lower at baseline in the lines without PRKCG | 0.047 | ⚠ within organs, on part of the lines; also absent: SLC36A4, DBN1, CEP41; maybe low, not absent |
| [[FAM222A]] | B | PRKCG activity raises FAM222A's level | lines that do not express PRKCG (5) vs lines expressing it (45) | 1.36× lower at baseline in the lines without PRKCG | 0.052 | ⚠ within organs, on part of the lines; also absent: SLC36A4, DBN1, CEP41; maybe low, not absent |
| [[TTC36]] | B | PRKCG activity raises TTC36's level | lines that do not express PRKCG (5) vs lines expressing it (45) | 1.42× lower at baseline in the lines without PRKCG | 0.087 | ⚠ within organs, on part of the lines; also absent: SLC36A4, DBN1, CEP41; maybe low, not absent |

## Where it sits

- **Module**: [[Module 053]]; 88 genes; every member is in the + arm (projection on the module's main direction 0.676). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (36.3, -16.8); signed map (16.1, 12.0). **Vector** length 83.4, 19.8% of its response variance represented; |z| ≥ 3 in 675 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +6.9 | +8.5 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +5.5 | +8.7 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift | +4.6 | +1.6 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +4.6 | +4.7 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | +4.4 | +3.0 |
|  | [[Filgotinib (drug)]] 5 µM |  | +3.1 | +4.2 |
|  | [[PF-06260933 (drug)]] 5 µM |  | +2.9 | +2.1 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | +2.4 | +2.7 |
|  | [[Lactate (calcium) (drug)]] 5 µM |  | +2.3 | +2.3 |
| fall | [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift | -2.8 | -2.0 |
|  | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.5 | -2.5 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -2.5 | -2.5 |
|  | [[Phenylephrine (hydrochloride) (drug)]] 0.5 µM |  | -2.5 | -2.9 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift | -2.4 | -2.1 |
|  | [[Berbamine (drug)]] 0.05 µM |  | -2.4 | -1.8 |
|  | [[Vinblastine (sulfate) (drug)]] 0.05 µM |  | -2.3 | -2.1 |
|  | [[Vortioxetine (drug)]] 0.5 µM |  | -2.2 | -2.4 |

## What is on record

|  |  |
|---|---|
| Name | protein kinase C gamma |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 19q13.42 — chr19:53,879,190-53,907,652 (+) |
| Ensembl biotype | protein_coding |
| Also known as | PKCC, MGC57564, PKCγ; previously PKCG, SCA14 |
| Gene groups (HGNC) | C2 domain containing protein kinases; Protein kinase C family |
| Hallmark sets | ALLOGRAFT_REJECTION |
| Reactome | 26 pathways, smallest: Disinhibition of SNARE formation; WNT5A-dependent internalization of FZD4; Trafficking of GluR2-containing AMPA receptors |
| Matched by | ensembl_id |

**Function**, from UniProt [P05129](https://www.uniprot.org/uniprotkb/P05129) (Protein kinase C gamma type):

> Calcium-activated, phospholipid- and diacylglycerol (DAG)-dependent serine/threonine-protein kinase that plays diverse roles in neuronal cells and eye tissues, such as regulation of the neuronal receptors GRIA4/GLUR4 and GRIN1/NMDAR1, modulation of receptors and neuronal functions related to sensitivity to opiates, pain and alcohol, mediation of synaptic function and cell survival after ischemia, and inhibition of gap junction activity after oxidative stress. Binds and phosphorylates …

**Summary**, from NCBI Gene [5582](https://www.ncbi.nlm.nih.gov/gene/5582):

> Protein kinase C (PKC) is a family of serine- and threonine-specific protein kinases that can be activated by calcium and second messenger diacylglycerol. PKC family members phosphorylate a wide variety of protein targets and are known to be involved in diverse cellular signaling pathways. PKC also serve as major receptors for phorbol esters, a class of tumor promoters. Each member of the PKC family has a specific expression profile and is believed to play distinct roles in cells. The protein …

**Accessions** — [HGNC:9402](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:9402) · Entrez [5582](https://www.ncbi.nlm.nih.gov/gene/5582) · UniProt [P05129](https://www.uniprot.org/uniprotkb/P05129) · Ensembl [ENSG00000126583](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000126583)

## Data

Gene col 4747: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4747); `tables/drug_effects.parquet` (16 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4747, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4747]; `tensor/DDL_lfc|DDL_z.npy` [4747]; `embed/gene_vectors.npy` [4747]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4747 or target_col == 4747). Every well: [[PRKCG — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. The written part above is `tahoemap/vault_seed/genes/PRKCG.md`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
