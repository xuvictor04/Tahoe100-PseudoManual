---
symbol: "ITPKA"
type: "gene"
col: 6080
ensembl_id: "ENSG00000137825"
name: "inositol-trisphosphate 3-kinase A"
location: "15q15.1"
module: 63
arm: "+"
pooled_cpm: 4.26
n_lines_expressing: 46
n_dd_up: 15
n_dd_down: 0
n_dd_up_clean: 9
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/063"]
generated_by: "tahoemap"
---

# ITPKA

*inositol-trisphosphate 3-kinase A* — 15q15.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 15 drug-doses (6 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 2.17× (z +8.9, q 2e-16, up in 20 of 32 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 9 here, 7 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 4 lines (CFPAC-1 0.108×, NCI-H2347 0.158×, COLO 205 0.225×, HT-29 0.143×; ⚠ cell-cycle shift, explains ~0% of this change); [[Homoharringtonine (drug)]] 0.5 µM in 2 lines (CFPAC-1 0.0413×, HT-29 0.0297×; ⚠ cell-cycle shift, explains ~34% of this change); [[Harringtonine (drug)]] 5 µM in 2 lines (CFPAC-1 0.0492×, SW48 0.0341×); [[Ouabain (Octahydrate) (drug)]] 5 µM in 1 line (COLO 205 0.115×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[MKNK2]] (+0.65, fdr 7e-06), [[IL17RA]] (+0.62, fdr 1e-05), [[GPT2]] (+0.58, fdr 2e-05); moves opposite to [[TPM1]] (-0.53, fdr 1e-04), [[CDK6]] (-0.52, fdr 1e-04), [[BBOX1-AS1]] (-0.52, fdr 5e-05).
> It is in [[Module 063]], a single-armed module (ISR ATF4).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 6 with an alert ⚠. 15 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6080.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.17×** | +8.9 | 2e-16 | 20/32 (NCI-H460, LOX-IMVI, …) | top dose only | cell-cycle shift (explains ~17% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.98×** | +5.6 | 6e-06 | 20/40 (COLO 205, A498, …) | inconsistent across doses |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~46% of this change | **1.89×** | +5.2 | 4e-05 | 4/17 (A-172, HepG2/C3A, …) | two highest doses | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~47% of this change | **1.80×** | +4.6 | 5e-04 | 0/4 | two highest doses | composition shift |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~56% of this change | **1.76×** | +4.6 | 5e-04 | 13/43 (PANC-1, LOX-IMVI, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~51% of this change | **1.70×** | +4.3 | 0.001 | 12/40 (PANC-1, NCI-H2030, …) | all doses, stronger at high dose |  |
| [[Sapanisertib (drug)]] 0.5 µM |  | **2.02×** | +4.1 | 0.003 | 11/35 (A498, KATO III, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Belinostat (drug)]] 0.5 µM |  | **1.65×** | +4.1 | 0.003 | 8/30 (A-172, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~16% here) |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~55% of this change | **1.63×** | +4.0 | 0.004 | 13/40 (PANC-1, NCI-H2030, …) | rises with dose |  |
| [[Abemaciclib (drug)]] 5 µM |  | **2.52×** | +4.0 | 0.004 | 11/33 (CFPAC-1, A498, …) | rises with dose | noisy plate (z scaled) |
| [[Budesonide (drug)]] 0.5 µM |  | **1.57×** | +3.7 | 0.011 | 11/40 (A498, NCI-H2347, …) | inconsistent across doses |  |
| [[Triamcinolone (drug)]] 5 µM |  | **1.33×** | +3.3 | 0.050 | 10/40 (A498, CFPAC-1, …) | rises with dose |  |
| [[Neratinib (maleate) (drug)]] 0.5 µM |  | **1.46×** | +3.1 | 0.085 | 10/33 (CFPAC-1, LoVo, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.68×** | +3.0 | 0.092 | 2/25 (SW48, NCI-H1792) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Clobetasol propionate (drug)]] 0.5 µM |  | **1.45×** | +3.0 | 0.092 | 10/39 (A498, NCI-H2347, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 4 in all, none with an alert. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 6080.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 9 here, 7 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 4 lines (CFPAC-1 0.108×, NCI-H2347 0.158×, COLO 205 0.225×, HT-29 0.143×; ⚠ cell-cycle shift, explains ~0% of this change); [[Homoharringtonine (drug)]] 0.5 µM in 2 lines (CFPAC-1 0.0413×, HT-29 0.0297×; ⚠ cell-cycle shift, explains ~34% of this change); [[Harringtonine (drug)]] 5 µM in 2 lines (CFPAC-1 0.0492×, SW48 0.0341×); [[Ouabain (Octahydrate) (drug)]] 5 µM in 1 line (COLO 205 0.115×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Cobimetinib (drug)]] 0.5 µM |  | 0.645× | -3.6 | 0.19 | 13/39 (SW480, Hs 766T, …) | inconsistent across doses | position effect removed |
| [[Digitoxin (drug)]] 0.5 µM |  | 0.667× | -3.3 | 0.19 | 11/39 (HT-29, NCI-H2030, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | 0.657× | -3.3 | 0.19 | 16/36 (CFPAC-1, SW48, …) | rises with dose | cell-cycle shift (explains ~3% here); composition shift |
| [[TAK-901 (drug)]] 5 µM |  | 0.491× | -3.0 | 0.35 | 12/35 (LS 180, COLO 205, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.54 per unit of S-phase module lfc, -0.23 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6080. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[COLO 205 (line)]] | alt | 24.2 | 3 (1 ⚠) | 3 (2 ⚠) | [[Vinblastine (sulfate) (drug)]] 5 µM 4.89× (z +10.2) | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.115× (z -9.8) |
| [[CFPAC-1 (line)]] | alt | 25.1 | 0 | 4 (3 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0413× (z -14.5) ⚠ cell-cycle shift, explains ~34% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.0492× (z -13.2) |
| [[HT-29 (line)]] | alt | 5.09 | 0 | 3 (3 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0297× (z -12.0) ⚠ cell-cycle shift, explains ~34% of this change |
| [[NCI-H2347 (line)]] | alt | 11.2 | 0 | 2 (2 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.133× (z -12.8) ⚠ cell-cycle shift, explains ~0% of this change |
| [[SW48 (line)]] | wt | 9.38 | 0 | 1 | — | [[Harringtonine (drug)]] 5 µM 0.0341× (z -9.1) |
| [[SW480 (line)]] | alt | 5.54 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.163× (z -8.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~46% of this change |
| [[A-172 (line)]] | wt | 5.28 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 2.43 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 6.90 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 1.29 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 7.57 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 1.63 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 0.804 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 3.28 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 0.989 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 1.13 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 3.02 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 4.27 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 1.61 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 8.34 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 2.75 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 1.30 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 0.787 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.49 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 2.16 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 7.65 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 5.55 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 2.53 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 2.82 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 1.91 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 1.04 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 5.39 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 1.65 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 3.81 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 1.53 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 1.88 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 3.38 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 3.51 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 1.21 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 1.55 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 7.26 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 2.75 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 2.46 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 2.25 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 2.28 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 1.72 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 1.80 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 4.29 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 3.21 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 3.34 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6080), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*78 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MKNK2]] | +0.65 | +0.60 / +0.62 | both halves | 7e-06 |  |
| [[IL17RA]] | +0.62 | +0.50 / +0.64 | both halves | 1e-05 |  |
| [[GPT2]] | +0.58 | +0.48 / +0.57 | both halves | 2e-05 |  |
| [[AKNA]] | +0.55 | +0.52 / +0.49 | both halves | 1e-05 |  |
| [[TRIB3]] | +0.54 | +0.44 / +0.54 | both halves | 3e-05 |  |
| [[FKBP1B]] | +0.54 | +0.54 / +0.46 | both halves | 3e-05 |  |
| [[RAB43]] | +0.53 | +0.47 / +0.53 | both halves | 2e-05 |  |
| [[SLC66A2]] | +0.52 | +0.42 / +0.45 | both halves | 4e-05 |  |
| [[ANKRD11]] | +0.52 | +0.48 / +0.49 | both halves | 2e-05 |  |
| [[BAHD1]] | +0.52 | +0.41 / +0.51 | both halves | 4e-05 |  |
| [[PMM1]] | +0.51 | +0.38 / +0.49 | both halves | 7e-05 |  |
| [[INPP5B]] | +0.51 | +0.43 / +0.47 | both halves | 3e-05 | pathway: Inositol phosphate metabolism |

## Genes that move opposite

*22 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TPM1]] | -0.53 | -0.35 / -0.57 | both halves | 1e-04 |  |
| [[CDK6]] | -0.52 | -0.34 / -0.56 | both halves | 1e-04 |  |
| [[BBOX1-AS1]] | -0.52 | -0.40 / -0.46 | both halves | 5e-05 |  |
| [[NHLRC2]] | -0.49 | -0.40 / -0.48 | both halves | 5e-05 |  |
| [[ZNF624]] | -0.48 | -0.42 / -0.52 | both halves | 4e-05 |  |
| [[SLC39A10]] | -0.48 | -0.36 / -0.42 | both halves | 1e-04 |  |
| [[MOK]] | -0.47 | -0.44 / -0.52 | both halves | 3e-05 |  |
| [[ZBTB33]] | -0.46 | -0.36 / -0.45 | both halves | 1e-04 |  |
| [[TBCEL]] | -0.46 | -0.35 / -0.47 | both halves | 1e-04 |  |
| [[SLC36A4]] | -0.46 | -0.24 / -0.46 | both halves | 5e-04 |  |
| [[DCAF8]] | -0.46 | -0.31 / -0.45 | both halves | 2e-04 |  |
| [[ATF7IP]] | -0.45 | -0.35 / -0.41 | both halves | 1e-04 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 063]] — ISR ATF4; 77 genes; every member is in the + arm (projection on the module's main direction 0.447). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.33; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-19.1, 50.6); signed map (-25.8, 7.1). **Vector** length 70.6, 12.6% of its response variance represented; |z| ≥ 3 in 914 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +3.8 | +8.9 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +3.2 | +5.6 |
|  | [[Abemaciclib (drug)]] 5 µM |  | +2.4 | +4.0 |
|  | [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift | +2.2 | +2.6 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~55% of this change | +2.2 | +4.0 |
|  | [[Clobetasol propionate (drug)]] 0.05 µM |  | +2.1 | +1.9 |
|  | [[Betamethasone dipropionate (drug)]] 0.5 µM |  | +2.1 | +2.7 |
|  | [[Triamcinolone (drug)]] 5 µM |  | +2.1 | +3.3 |
|  | [[Sapanisertib (drug)]] 0.5 µM |  | +2.1 | +4.1 |
| fall | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -3.2 | -2.5 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -2.7 | -0.8 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -2.6 | -2.8 |
|  | [[Harringtonine (drug)]] 5 µM |  | -2.1 | -3.3 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~34% of this change | -1.9 | -2.4 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -1.8 | -2.1 |
|  | [[Cobimetinib (drug)]] 5 µM |  | -1.7 | -0.7 |
|  | [[Cobimetinib (drug)]] 0.5 µM |  | -1.5 | -3.6 |
|  | [[Binimetinib (drug)]] 0.5 µM |  | -1.4 | -1.0 |

## What is on record

|  |  |
|---|---|
| Name | inositol-trisphosphate 3-kinase A |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 15q15.1 — chr15:41,493,393-41,503,551 (+) |
| Ensembl biotype | protein_coding |
| Also known as | IP3KA, IP3-3KA |
| Gene groups (HGNC) | Inositol-trisphosphate 3-kinase family |
| Reactome | 2 pathways, smallest: Synthesis of IP3 and IP4 in the cytosol; Inositol phosphate metabolism |
| Matched by | ensembl_id |

**Function**, from UniProt [P23677](https://www.uniprot.org/uniprotkb/P23677) (Inositol-trisphosphate 3-kinase A):

> Catalyzes the phosphorylation of 1D-myo-inositol 1,4,5-trisphosphate (InsP3) into 1D-myo-inositol 1,3,4,5-tetrakisphosphate and participates to the regulation of calcium homeostasis.

**Summary**, from NCBI Gene [3706](https://www.ncbi.nlm.nih.gov/gene/3706):

> Regulates inositol phosphate metabolism by phosphorylation of second messenger inositol 1,4,5-trisphosphate to Ins(1,3,4,5)P4. The activity of the inositol 1,4,5-trisphosphate 3-kinase is responsible for regulating the levels of a large number of inositol polyphosphates that are important in cellular signaling. Both calcium/calmodulin and protein phosphorylation mechanisms control its activity. It is also a substrate for the cyclic AMP-dependent protein kinase, calcium/calmodulin- dependent …

**Accessions** — [HGNC:6178](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:6178) · Entrez [3706](https://www.ncbi.nlm.nih.gov/gene/3706) · UniProt [P23677](https://www.uniprot.org/uniprotkb/P23677) · Ensembl [ENSG00000137825](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000137825)

## Data

Gene col 6080: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6080); `tables/drug_effects.parquet` (19 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6080, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6080]; `tensor/DDL_lfc|DDL_z.npy` [6080]; `embed/gene_vectors.npy` [6080]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6080 or target_col == 6080). Every well: [[ITPKA — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ITPKA.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
