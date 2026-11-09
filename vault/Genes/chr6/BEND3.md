---
symbol: "BEND3"
type: "gene"
col: 10926
ensembl_id: "ENSG00000178409"
name: "BEN domain containing 3"
location: "6q21"
module: 5
arm: "+"
pooled_cpm: 5.07
n_lines_expressing: 50
n_dd_up: 10
n_dd_down: 16
n_dd_up_clean: 4
n_dd_down_clean: 11
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/005"]
generated_by: "tahoemap"
---

# BEND3

*BEN domain containing 3* — 6q21

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 10 drug-doses (6 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 3.23× (z +19.8, q 0e+00, up in 37 of 40 measured lines).
> Pooled over the cell lines (median), lowered significantly by 16 drug-doses (5 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.614× (z -5.8, q 3e-06, down in 19 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ADCY3]] (+0.78, fdr 7e-06), [[PIGW]] (+0.73, fdr 7e-06), [[NSUN2]] (+0.69, fdr 7e-06); moves opposite to [[SIRT2]] (-0.65, fdr 1e-05), [[GABARAP]] (-0.64, fdr 1e-05, ⚠ GABARAP in the vector space only through flagged drug-doses), [[MOSPD2]] (-0.63, fdr 1e-05), [[DCTN3]] (-0.60, fdr 3e-05).
> It sits in the **+** arm of [[Module 005]] (MYC targets v2).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[WNK2]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 6 with an alert ⚠. 10 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10926.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **3.23×** | +19.8 | 0e+00 | 37/40 (PANC-1, HEC-1-A, …) | top dose only | cell-cycle shift (explains ~6% here) |
| [[Auranofin (drug)]] 5 µM |  | **2.06×** | +8.6 | 2e-15 | 30/46 (HOP62, MIA PaCa-2, …) | top dose only |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.05×** | +8.3 | 3e-14 | 2/7 (NCI-H2347, HOP62) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here); composition shift |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.83×** | +7.2 | 7e-11 | 26/47 (NCI-H460, MIA PaCa-2, …) | inconsistent across doses |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.50×** | +4.5 | 7e-04 | 4/9 (PANC-1, MIA PaCa-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.40×** | +4.0 | 0.006 | 9/23 (LoVo, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here); composition shift |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **1.40×** | +3.9 | 0.009 | 11/38 (PANC-1, SW480, …) | top dose only |  |
| [[Belinostat (drug)]] 0.5 µM |  | **1.37×** | +3.8 | 0.012 | 11/40 (LOX-IMVI, SW 900, …) | inconsistent across doses | cell-cycle shift (explains ~9% here) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~43% of this change | **1.24×** | +3.7 | 0.015 | 9/46 (PANC-1, SK-MEL-2, …) | top dose only | low cells (technical?) |
| [[Peretinoin (drug)]] 5 µM |  | **1.36×** | +3.5 | 0.024 | 8/45 (MIA PaCa-2, CFPAC-1, …) | rises with dose |  |
| [[S-Adenosyl-L-methionine (disulfate tosylate) (drug)]] 5 µM |  | 1.20× | +3.1 | 0.11 | 5/47 (PANC-1, CFPAC-1, …) | top dose only | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 16 in all, 5 with an alert ⚠; shown: the 15 strongest. 16 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 10926.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.614×** | -5.8 | 3e-06 | 19/47 (J82, A-427, …) | rises with dose | cell-cycle shift (explains ~11% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.628×** | -5.6 | 8e-06 | 20/41 (A-427, RKO, …) | rises with dose | cell-cycle shift (explains ~6% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.637×** | -5.4 | 1e-05 | 22/46 (PANC-1, A-427, …) | rises with dose | cell-cycle shift (explains ~6% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.670×** | -4.8 | 2e-04 | 16/46 (SNU-1, NCI-H23, …) | rises with dose | cell-cycle shift (explains ~5% here) |
| [[Artesunate (drug)]] 5 µM |  | **0.761×** | -4.6 | 4e-04 | 15/47 (SHP-77, HCT15, …) | rises with dose | cell-cycle shift (explains ~5% here) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~68% of this change | **0.762×** | -4.6 | 4e-04 | 18/40 (A-427, A498, …) | rises with dose | composition shift |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **0.676×** | -4.5 | 5e-04 | 16/44 (PANC-1, A498, …) | top dose only | composition shift |
| [[Ponatinib (drug)]] 5 µM |  | **0.697×** | -4.3 | 0.001 | 10/47 (RKO, SW 1271, …) | all doses, stronger at high dose | position effect removed |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | **0.705×** | -4.2 | 0.002 | 11/46 (SW480, NCI-H23, …) | two highest doses |  |
| [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **0.526×** | -4.0 | 0.003 | 7/35 (SHP-77, BT-474, …) | top dose only | noisy plate (z scaled) |
| [[Pitavastatin (Calcium) (drug)]] 5 µM |  | **0.709×** | -4.0 | 0.004 | 10/42 (A549, SNU-1, …) | rises with dose | cell-cycle shift (explains ~6% here) |
| [[Trametinib (drug)]] 5 µM |  | **0.763×** | -3.8 | 0.006 | 10/47 (C-33 A, NCI-H2030, …) | rises with dose | cell-cycle shift (explains ~1% here); noisy plate (z scaled) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.727×** | -3.8 | 0.006 | 20/46 (SW48, SW1417, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.734×** | -3.7 | 0.009 | 17/46 (SW480, C-33 A, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Binimetinib (drug)]] 0.5 µM |  | **0.798×** | -3.2 | 0.054 | 14/45 (SW480, NCI-H2347, …) | inconsistent across doses | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.28 per unit of S-phase module lfc, -0.32 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10926. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW48 (line)]] | wt | 45.8 | 0 | 4 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0779× (z -14.9) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.217× (z -8.9) |
| [[RKO (line)]] | wt | 9.50 | 0 | 3 (2 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 0.05 µM 0.0743× (z -9.1) |
| [[A-427 (line)]] | wt | 13.1 | 0 | 2 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.107× (z -11.0) ⚠ toxic; transcription drop |
| [[HEC-1-A (line)]] | alt | 4.14 | 1 | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.36× (z +9.5) | [[Cobimetinib (drug)]] 0.05 µM 0.0929× (z -8.8) |
| [[PANC-1 (line)]] | alt | 5.97 | 1 | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.45× (z +10.2) | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.230× (z -8.5) |
| [[A498 (line)]] | wt | 3.84 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.230× (z -8.9) ⚠ cell-cycle shift, explains ~68% of this change |
| [[AsPC-1 (line)]] | alt | 2.79 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.103× (z -8.8) ⚠ cell-cycle shift, explains ~68% of this change |
| [[HT-29 (line)]] | alt | 3.05 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 7.01× (z +8.5) | — |
| [[J82 (line)]] | alt | 8.17 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.180× (z -8.6) |
| [[MIA PaCa-2 (line)]] | alt | 5.59 | 0 | 1 (1 ⚠) | — | [[Adagrasib (drug)]] 0.05 µM 0.510× (z -8.9) ⚠ position not correctable |
| [[NCI-H2030 (line)]] | alt | 4.32 | 0 | 1 (1 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.0908× (z -8.8) ⚠ cell-cycle shift, explains ~31% of this change |
| [[NCI-H460 (line)]] | wt | 3.43 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.44× (z +9.1) | — |
| [[SHP-77 (line)]] | alt | 11.9 | 0 | 1 | — | [[Lidocaine (hydrochloride) (drug)]] 0.5 µM 0.0936× (z -10.6) |
| [[A-172 (line)]] | wt | 2.72 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 2.65 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 12.4 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 5.62 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 12.7 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 2.60 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 2.13 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 3.93 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 2.63 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 3.08 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 4.82 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 2.81 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 3.68 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 1.96 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 3.11 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 2.85 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 5.04 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 5.25 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 2.62 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 4.23 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 2.45 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 2.91 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 4.34 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 7.80 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 2.40 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 4.04 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 9.82 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 3.87 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 3.70 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 5.00 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 6.44 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 1.83 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 3.15 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 4.58 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 2.82 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 4.46 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 7.85 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10926), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*82 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ADCY3]] | +0.78 | +0.74 / +0.74 | both halves | 7e-06 |  |
| [[PIGW]] | +0.73 | +0.65 / +0.68 | both halves | 7e-06 |  |
| [[NSUN2]] | +0.69 | +0.67 / +0.66 | both halves | 7e-06 |  |
| [[EEF1AKMT1]] | +0.68 | +0.56 / +0.63 | both halves | 1e-05 |  |
| [[WDR4]] | +0.67 | +0.69 / +0.61 | both halves | 7e-06 |  |
| [[NOP2]] | +0.67 | +0.67 / +0.60 | both halves | 7e-06 |  |
| [[DHX33]] | +0.67 | +0.66 / +0.56 | both halves | 1e-05 |  |
| [[MRM1]] | +0.65 | +0.65 / +0.49 | both halves | 2e-05 |  |
| [[PALD1]] | +0.64 | +0.63 / +0.65 | both halves | 7e-06 |  |
| [[BCL2]] | +0.64 | +0.56 / +0.63 | both halves | 1e-05 |  |
| [[NOP16]] | +0.63 | +0.70 / +0.53 | both halves | 1e-05 |  |
| [[MACROD1]] | +0.63 | +0.56 / +0.62 | both halves | 1e-05 |  |

## Genes that move opposite

*18 of its nearest partners move opposite, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SIRT2]] | -0.65 | -0.69 / -0.50 | both halves | 1e-05 |  |
| [[GABARAP]] ⚠ | -0.64 | -0.63 / -0.54 | both halves | 1e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[MOSPD2]] | -0.63 | -0.52 / -0.54 | both halves | 1e-05 |  |
| [[DCTN3]] | -0.60 | -0.60 / -0.43 | both halves | 3e-05 |  |
| [[KIDINS220]] | -0.59 | -0.54 / -0.51 | both halves | 1e-05 |  |
| [[NEU1]] | -0.58 | -0.60 / -0.47 | both halves | 2e-05 |  |
| [[CTNND1]] | -0.57 | -0.55 / -0.49 | both halves | 1e-05 |  |
| [[RNF114]] | -0.57 | -0.56 / -0.47 | both halves | 2e-05 |  |
| [[OPTN]] | -0.56 | -0.61 / -0.49 | both halves | 1e-05 |  |
| [[DNAL4]] | -0.56 | -0.45 / -0.53 | both halves | 3e-05 |  |
| [[TBC1D17]] | -0.56 | -0.46 / -0.51 | both halves | 2e-05 |  |
| [[MAP3K13]] | -0.55 | -0.60 / -0.45 | both halves | 3e-05 |  |
| [[ALAD]] | -0.55 | -0.40 / -0.53 | both halves | 5e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[WNK2]] | B | WNK2 activity raises BEND3's level | lines that do not express WNK2 (16) vs lines expressing it (34) | 1.64× lower at baseline in the lines without WNK2 | 0.084 | ⚠ within organs, on part of the lines; also absent: NUP210, SLC27A2, CHDH |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 005]] — MYC targets v2; 244 genes; this gene is in the **+** arm (projection on the module's main direction 0.726). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.29).
- **Nodal map** (x, y) = (-0.2, -34.2); signed map (0.6, -52.2). **Vector** length 81.3, 14.3% of its response variance represented; |z| ≥ 3 in 1,058 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *MYC targets v2* (hallmark, mean cos +0.54 to 13); *ribosome biogenesis* (control, mean cos +0.51 to 6); *tRNA modification in the nucleus and cytosol* (reactome, mean cos +0.56 to 7).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +8.3 | +19.8 |
|  | [[Auranofin (drug)]] 5 µM |  | +6.1 | +8.6 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +4.8 | +7.2 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +3.3 | +4.5 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | +3.2 | +3.9 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.7 | +1.4 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | +2.4 | +2.5 |
|  | [[EX229 (drug)]] 5 µM |  | +2.3 | +1.4 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | +2.3 | +2.7 |
| fall | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | -3.8 | -5.8 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | -2.9 | -5.6 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | -2.6 | -3.8 |
|  | [[Artesunate (drug)]] 5 µM |  | -2.5 | -4.6 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -2.4 | -2.8 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -2.3 | -4.2 |
|  | [[Binimetinib (drug)]] 5 µM |  | -2.1 | -1.9 |
|  | [[Binimetinib (drug)]] 0.5 µM |  | -2.0 | -3.2 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | -2.0 | -2.3 |

## What is on record

|  |  |
|---|---|
| Name | BEN domain containing 3 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 6q21 — chr6:107,065,182-107,115,515 (-) |
| Ensembl biotype | protein_coding |
| Also known as | ; previously KIAA1553 |
| Gene groups (HGNC) | BEN domain containing |
| Matched by | ensembl_id |

**Function**, from UniProt [Q5T5X7](https://www.uniprot.org/uniprotkb/Q5T5X7) (BEN domain-containing protein 3):

> Transcriptional repressor which associates with the NoRC (nucleolar remodeling complex) complex and plays a key role in repressing rDNA transcription. The sumoylated form modulates the stability of the NoRC complex component BAZ2A/TIP5 by controlling its USP21-mediated deubiquitination. Binds to unmethylated major satellite DNA and is involved in the recruitment of the Polycomb repressive complex 2 (PRC2) to major satellites (By similarity). Stimulates the ERCC6L translocase and ATPase …

**Summary**, from NCBI Gene [57673](https://www.ncbi.nlm.nih.gov/gene/57673):

> Enables rDNA binding activity. Involved in several processes, including heterochromatin formation; positive regulation of ATP metabolic process; and protein homooligomerization. Located in heterochromatin and nucleolus. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:23040](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:23040) · Entrez [57673](https://www.ncbi.nlm.nih.gov/gene/57673) · UniProt [Q5T5X7](https://www.uniprot.org/uniprotkb/Q5T5X7) · Ensembl [ENSG00000178409](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000178409)

## Data

Gene col 10926: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10926); `tables/drug_effects.parquet` (27 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10926, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10926]; `tensor/DDL_lfc|DDL_z.npy` [10926]; `embed/gene_vectors.npy` [10926]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10926 or target_col == 10926). Every well: [[BEND3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/BEND3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
