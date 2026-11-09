---
symbol: "TLNRD1"
type: "gene"
col: 6406
ensembl_id: "ENSG00000140406"
name: "talin rod domain containing 1"
location: "15q25.1"
module: 17
arm: "-"
pooled_cpm: 21.72
n_lines_expressing: 50
n_dd_up: 11
n_dd_down: 12
n_dd_up_clean: 5
n_dd_down_clean: 10
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/017"]
generated_by: "tahoemap"
---

# TLNRD1

*talin rod domain containing 1* — 15q25.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 11 drug-doses (6 with an alert ⚠); the strongest is [[Topotecan (hydrochloride) (drug)]] 5 µM: 1.73× (z +6.1, q 8e-07, up in 26 of 42 measured lines) ⚠ toxic. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.27× (z +3.8, q 0.011, up in 20 of 46 measured lines).
> Pooled over the cell lines (median), lowered significantly by 12 drug-doses (2 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 0.5 µM: 0.336× (z -12.6, q 1e-33, down in 46 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CLCF1]] (+0.66, fdr 7e-06), [[ZNF710]] (+0.65, fdr 2e-05), [[AGO2]] (+0.64, fdr 1e-05); moves opposite to [[SKIC3]] (-0.69, fdr 7e-06), [[NIPSNAP1]] (-0.64, fdr 9e-06), [[ATP6V1A]] (-0.64, fdr 1e-05).
> It sits in the **-** arm of [[Module 017]] (Intraflagellar transport).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[DYNC2H1]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 7 with an alert ⚠. 11 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6406.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.73×** | +6.1 | 8e-07 | 26/42 (KATO III, SW1417, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.65×** | +5.7 | 3e-06 | 28/44 (HOP62, CFPAC-1, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~15% here); position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.58×** | +5.1 | 7e-05 | 17/31 (NCI-H1792, SW1417, …) | rises with dose | cell-cycle shift (explains ~1% here); composition shift; position effect removed |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.13× | +4.8 | 2e-04 | 6/48 (Hs 766T, HT-29, …) | inconsistent across doses |  |
| [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | **1.41×** | +4.0 | 0.008 | 20/47 (NCI-H460, HT-29, …) | rises with dose | position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.27×** | +3.8 | 0.011 | 20/46 (NCI-H460, A498, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Peretinoin (drug)]] 5 µM |  | **1.40×** | +3.7 | 0.016 | 20/47 (NCI-H460, NCI-H23, …) | all doses, stronger at high dose |  |
| [[Peretinoin (drug)]] 0.5 µM |  | **1.37×** | +3.7 | 0.017 | 18/47 (NCI-H460, NCI-H1792, …) | all doses, stronger at high dose |  |
| [[Daptomycin (drug)]] 0.5 µM | ⚠ unreliable plate only | **1.36×** | +3.5 | 0.024 | 20/47 (NCI-H460, COLO 205, …) | rises with dose | position effect removed |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **1.36×** | +3.5 | 0.024 | 12/44 (MIA PaCa-2, Panc 03.27, …) | all doses, flat |  |
| [[LY-2584702 (tosylate salt) (drug)]] 5 µM | ⚠ toxic | **1.69×** | +3.2 | 0.080 | 7/34 (NCI-H460, HEC-1-A, …) | top dose only | noisy plate (z scaled) |
| [[vincristine (drug)]] 0.5 µM |  | **1.46×** | +3.1 | 0.084 | 18/44 (NCI-H460, COLO 205, …) | two highest doses | low cells (technical?); noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 2 with an alert ⚠. 12 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 6406.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 0.5 µM |  | **0.336×** | -12.6 | 1e-33 | 46/48 (SW480, HT-29, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.340×** | -12.4 | 4e-33 | 44/48 (SW480, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.388×** | -10.9 | 1e-25 | 43/47 (HT-29, SW480, …) | rises with dose | cell-cycle shift (explains ~1% here) |
| [[Selinexor (drug)]] 0.5 µM |  | **0.658×** | -4.8 | 2e-04 | 25/47 (KATO III, CFPAC-1, …) | two highest doses | cell-cycle shift (explains ~16% here) |
| [[Verteporfin (drug)]] 5 µM |  | **0.651×** | -4.8 | 2e-04 | 28/47 (SW 900, A-427, …) | top dose only |  |
| [[Brivudine (drug)]] 5 µM |  | **0.462×** | -4.7 | 3e-04 | 26/48 (BT-474, PANC-1, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.669×** | -4.6 | 3e-04 | 26/48 (HepG2/C3A, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[NG25 (drug)]] 5 µM |  | **0.489×** | -4.3 | 0.001 | 23/45 (LS 180, KATO III, …) | top dose only | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **0.785×** | -4.0 | 0.005 | 24/48 (AsPC-1, Hs 766T, …) | two highest doses | low cells (technical?) |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **0.555×** | -3.6 | 0.021 | 20/38 (NCI-H1573, KATO III, …) | all doses, flat | cell-cycle shift (explains ~13% here); noisy plate (z scaled); position effect removed |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | **0.723×** | -3.5 | 0.027 | 19/47 (SW480, NCI-H23, …) | all doses, flat |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.736×** | -3.4 | 0.038 | 14/47 (C32, PANC-1, …) | all doses, flat | cell-cycle shift (explains ~18% here); position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.10 per unit of S-phase module lfc, +0.19 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6406. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A549 (line)]] | wt | 29.4 | 0 | 4 (1 ⚠) | — | [[Belinostat (drug)]] 5 µM 0.209× (z -10.4) |
| [[HT-29 (line)]] | alt | 37.0 | 0 | 3 | — | [[Belinostat (drug)]] 5 µM 0.156× (z -13.1) |
| [[KATO III (line)]] | alt | 36.0 | 0 | 3 | — | [[Panobinostat (drug)]] 5 µM 0.200× (z -12.8) |
| [[SW480 (line)]] | alt | 28.2 | 0 | 3 | — | [[Panobinostat (drug)]] 5 µM 0.186× (z -14.4) |
| [[A-172 (line)]] | wt | 18.5 | 0 | 2 | — | [[Belinostat (drug)]] 5 µM 0.249× (z -9.0) |
| [[LS 180 (line)]] | wt | 35.3 | 0 | 2 | — | [[Panobinostat (drug)]] 5 µM 0.149× (z -12.2) |
| [[RKO (line)]] | wt | 18.7 | 0 | 2 | — | [[Panobinostat (drug)]] 5 µM 0.122× (z -11.5) |
| [[SNU-423 (line)]] | alt | 7.64 | 0 | 2 | — | [[Hydroxyurea (drug)]] 0.5 µM 0.0721× (z -10.7) |
| [[A-427 (line)]] | wt | 19.1 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.117× (z -12.1) ⚠ cell-cycle shift, explains ~0% of this change |
| [[BT-474 (line)]] | alt | 24.0 | 0 | 1 | — | [[Panobinostat (drug)]] 0.5 µM 0.212× (z -8.9) |
| [[COLO 205 (line)]] | alt | 31.3 | 0 | 1 | — | [[Panobinostat (drug)]] 5 µM 0.178× (z -9.1) |
| [[HEC-1-A (line)]] | alt | 18.5 | 0 | 1 | — | [[Panobinostat (drug)]] 5 µM 0.207× (z -10.5) |
| [[Hs 766T (line)]] | wt | 20.4 | 0 | 1 | — | [[Panobinostat (drug)]] 0.5 µM 0.168× (z -10.0) |
| [[LoVo (line)]] | wt | 47.8 | 0 | 1 | — | [[Panobinostat (drug)]] 5 µM 0.328× (z -8.9) |
| [[MIA PaCa-2 (line)]] | alt | 12.1 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.146× (z -9.4) ⚠ cell-cycle shift, explains ~0% of this change |
| [[NCI-H1573 (line)]] | alt | 27.9 | 0 | 1 (1 ⚠) | — | [[Bortezomib (drug)]] 5 µM 0.0544× (z -10.0) ⚠ toxic |
| [[NCI-H2030 (line)]] | alt | 31.7 | 0 | 1 | — | [[Harringtonine (drug)]] 5 µM 0.161× (z -10.9) |
| [[NCI-H460 (line)]] | wt | 13.6 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.86× (z +10.0) | — |
| [[Panc 03.27 (line)]] | alt | 14.6 | 0 | 1 | — | [[Panobinostat (drug)]] 0.5 µM 0.188× (z -8.8) |
| [[PANC-1 (line)]] | alt | 21.5 | 0 | 1 | — | [[Panobinostat (drug)]] 5 µM 0.360× (z -9.0) |
| [[SW1417 (line)]] | alt | 30.6 | 0 | 1 | — | [[Panobinostat (drug)]] 0.5 µM 0.234× (z -10.2) |
| [[A498 (line)]] | wt | 16.7 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 18.3 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 25.2 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 19.8 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 23.6 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 25.8 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 8.91 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 18.6 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 17.1 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 15.2 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 17.6 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 8.77 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 14.7 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 21.7 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 22.0 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 11.5 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 27.0 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 14.7 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 12.3 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 20.3 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 12.5 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 16.5 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 17.2 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 18.9 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 13.5 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 12.6 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 17.2 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 12.2 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 29.9 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6406), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*47 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CLCF1]] | +0.66 | +0.68 / +0.60 | both halves | 7e-06 |  |
| [[ZNF710]] | +0.65 | +0.47 / +0.69 | both halves | 2e-05 |  |
| [[AGO2]] | +0.64 | +0.70 / +0.51 | both halves | 1e-05 |  |
| [[ZNF800]] | +0.63 | +0.56 / +0.53 | both halves | 1e-05 |  |
| [[CRK]] | +0.62 | +0.64 / +0.59 | both halves | 7e-06 |  |
| [[EPOP]] | +0.62 | +0.56 / +0.54 | both halves | 1e-05 |  |
| [[PHLPP2]] | +0.60 | +0.49 / +0.52 | both halves | 1e-05 |  |
| [[KHNYN]] | +0.60 | +0.50 / +0.59 | both halves | 1e-05 |  |
| [[GCNT4]] | +0.59 | +0.41 / +0.54 | both halves | 4e-05 |  |
| [[NACC2]] | +0.59 | +0.46 / +0.60 | both halves | 3e-05 |  |
| [[TECPR2]] | +0.59 | +0.47 / +0.55 | both halves | 2e-05 |  |
| [[RIPK1]] | +0.59 | +0.53 / +0.51 | both halves | 1e-05 |  |

## Genes that move opposite

*53 of its nearest partners move opposite, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SKIC3]] | -0.69 | -0.65 / -0.69 | both halves | 7e-06 |  |
| [[NIPSNAP1]] | -0.64 | -0.57 / -0.61 | both halves | 9e-06 |  |
| [[ATP6V1A]] | -0.64 | -0.52 / -0.73 | both halves | 1e-05 |  |
| [[TMEM9]] | -0.63 | -0.54 / -0.56 | both halves | 1e-05 |  |
| [[CAT]] | -0.63 | -0.69 / -0.55 | both halves | 1e-05 |  |
| [[USP30]] | -0.62 | -0.60 / -0.52 | both halves | 1e-05 |  |
| [[SCP2]] | -0.62 | -0.55 / -0.67 | both halves | 1e-05 |  |
| [[ATP5F1C]] | -0.62 | -0.60 / -0.55 | both halves | 1e-05 |  |
| [[DYNC2H1]] | -0.61 | -0.51 / -0.55 | both halves | 1e-05 |  |
| [[DYNC2LI1]] | -0.61 | -0.62 / -0.51 | both halves | 1e-05 |  |
| [[CDC73]] | -0.61 | -0.59 / -0.59 | both halves | 7e-06 |  |
| [[CYB5R4]] | -0.60 | -0.49 / -0.59 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[DYNC2H1]] | B | DYNC2H1 activity lowers TLNRD1's level | lines that do not express DYNC2H1 (8) vs lines expressing it (42) | 1.61× higher at baseline in the lines without DYNC2H1 | 0.073 | ⚠ within organs, on part of the lines; also absent: FJX1, GIHCG, LINC02798 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 017]] — Intraflagellar transport; 202 genes; this gene is in the **-** arm (projection on the module's main direction -0.585). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.28).
- **Nodal map** (x, y) = (-3.3, -7.0); signed map (7.2, 12.9). **Vector** length 98.7, 24.3% of its response variance represented; |z| ≥ 3 in 1,019 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +8.0 | +3.8 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +6.4 | +6.1 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | +4.9 | -1.6 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | +4.4 | +0.4 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift | +4.3 | +1.4 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | +3.8 | +2.3 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +3.3 | -0.2 |
|  | [[Peretinoin (drug)]] 0.5 µM |  | +3.3 | +3.7 |
|  | [[Peretinoin (drug)]] 5 µM |  | +3.2 | +3.7 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | +3.0 | +2.7 |
| fall | [[NG25 (drug)]] 5 µM |  | -4.0 | -4.3 |
|  | [[Selinexor (drug)]] 0.5 µM |  | -3.3 | -4.8 |
|  | [[Radotinib (drug)]] 5 µM |  | -3.3 | -2.4 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -2.9 | -3.5 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | -2.9 | -12.6 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -2.6 | -2.8 |
|  | [[Binimetinib (drug)]] 0.5 µM |  | -2.5 | -2.1 |
|  | [[Cobimetinib (drug)]] 5 µM |  | -2.4 | -3.0 |

## What is on record

|  |  |
|---|---|
| Name | talin rod domain containing 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 15q25.1 — chr15:81,000,923-81,005,788 (+) |
| Ensembl biotype | protein_coding |
| Also known as | MGC99595; previously MESDC1 |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9H1K6](https://www.uniprot.org/uniprotkb/Q9H1K6) (Talin rod domain-containing protein 1):

> Actin-binding protein which may have an oncogenic function and regulates cell proliferation, migration and invasion in cancer cells.

**Summary**, from NCBI Gene [59274](https://www.ncbi.nlm.nih.gov/gene/59274):

> This gene encodes a protein that is regulated by micro RNA MiR-574-3, and is thought to have an oncogenic function in human bladder cancer. A similar gene in mouse is located in a chromosomal region critical for differentiation of mesoderm, which affects embryo patterning and the formation of heart, muscle, blood, skeleton and the urogenital system. The mouse gene is expressed in early development, and in the adult. [provided by RefSeq, Nov 2016]

**Accessions** — [HGNC:13519](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:13519) · Entrez [59274](https://www.ncbi.nlm.nih.gov/gene/59274) · UniProt [Q9H1K6](https://www.uniprot.org/uniprotkb/Q9H1K6) · Ensembl [ENSG00000140406](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000140406)

## Data

Gene col 6406: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6406); `tables/drug_effects.parquet` (24 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6406, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6406]; `tensor/DDL_lfc|DDL_z.npy` [6406]; `embed/gene_vectors.npy` [6406]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6406 or target_col == 6406). Every well: [[TLNRD1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TLNRD1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
