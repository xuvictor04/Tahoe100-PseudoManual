---
symbol: "DCAF1"
type: "gene"
col: 6953
ensembl_id: "ENSG00000145041"
name: "DDB1 and CUL4 associated factor 1"
location: "3p21.2"
module: 4
arm: "+"
pooled_cpm: 64.4
n_lines_expressing: 50
n_dd_up: 5
n_dd_down: 17
n_dd_up_clean: 3
n_dd_down_clean: 13
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/004"]
generated_by: "tahoemap"
---

# DCAF1

*DDB1 and CUL4 associated factor 1* — 3p21.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 5 drug-doses (2 with an alert ⚠); the strongest is [[TAK-901 (drug)]] 5 µM: 3.88× (z +12.0, q 2e-30, up in 41 of 49 measured lines).
> Pooled over the cell lines (median), lowered significantly by 17 drug-doses (4 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.493× (z -18.6, q 0e+00, down in 47 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[POLR3H]] (+0.71, fdr 7e-06), [[POLR1A]] (+0.70, fdr 1e-05), [[LSG1]] (+0.69, fdr 7e-06); moves opposite to [[CERT1]] (-0.65, fdr 2e-05), [[AAMDC]] (-0.64, fdr 7e-06), [[RSRP1]] (-0.64, fdr 1e-05).
> It sits in the **+** arm of [[Module 004]] (MYC targets v1).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[PSMB5]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 4 with an alert ⚠. 5 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6953.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[TAK-901 (drug)]] 5 µM |  | **3.88×** | +12.0 | 2e-30 | 41/49 (LoVo, HEC-1-A, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **3.22×** | +10.3 | 1e-22 | 40/48 (HEC-1-A, LS 180, …) | inconsistent across doses | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.37×** | +5.8 | 1e-06 | 39/48 (CFPAC-1, NCI-H2347, …) | inconsistent across doses |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.27×** | +4.4 | 0.001 | 26/48 (Hs 766T, Panc 03.27, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.20× | +3.4 | 0.074 | 16/47 (SNU-1, PANC-1, …) | inconsistent across doses |  |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~16% of this change | **1.21×** | +3.4 | 0.074 | 20/48 (CFPAC-1, J82, …) | inconsistent across doses |  |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.18× | +3.1 | 0.16 | 18/48 (HEC-1-A, MIA PaCa-2, …) | inconsistent across doses |  |
| [[TAK-901 (drug)]] 0.05 µM |  | 1.19× | +3.0 | 0.17 | 18/47 (LOX-IMVI, HEC-1-A, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 23 in all, 7 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 17 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 6953.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.493×** | -18.6 | 0e+00 | 47/48 (NCI-H23, AsPC-1, …) | top dose only | cell-cycle shift (explains ~4% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.451×** | -14.3 | 8e-44 | 42/48 (HOP62, NCI-H23, …) | top dose only | cell-cycle shift (explains ~5% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.509×** | -12.1 | 2e-31 | 42/50 (SNU-1, NCI-H460, …) | top dose only | cell-cycle shift (explains ~6% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.656×** | -7.6 | 6e-12 | 29/44 (MIA PaCa-2, SW 900, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here); composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.677×** | -7.0 | 3e-10 | 36/47 (HepG2/C3A, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~8% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | **0.695×** | -6.8 | 1e-09 | 30/49 (SW48, NCI-H460, …) | all doses, stronger at high dose | composition shift |
| [[Panobinostat (drug)]] 5 µM |  | **0.698×** | -6.7 | 2e-09 | 39/48 (A498, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.704×** | -6.5 | 4e-09 | 41/48 (A498, NCI-H2030, …) | rises with dose | cell-cycle shift (explains ~19% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **0.810×** | -5.5 | 2e-06 | 30/48 (A498, MIA PaCa-2, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.745×** | -5.5 | 3e-06 | 34/48 (A498, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **0.750×** | -5.3 | 5e-06 | 35/48 (NCI-H2347, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~23% of this change | **0.769×** | -4.9 | 5e-05 | 29/48 (A498, NCI-H2030, …) | all doses, stronger at high dose |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 0.834× | -4.8 | 8e-05 | 24/48 (HOP62, NCI-H2347, …) | top dose only |  |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.834× | -4.8 | 8e-05 | 25/48 (A-427, LOX-IMVI, …) | rises with dose | low cells (technical?) |
| [[Belinostat (drug)]] 0.5 µM |  | **0.785×** | -4.5 | 3e-04 | 22/48 (A498, NCI-H23, …) | rises with dose | cell-cycle shift (explains ~10% here) |
| [[Ponatinib (drug)]] 5 µM |  | **0.792×** | -4.3 | 5e-04 | 28/48 (NCI-H2030, J82, …) | rises with dose |  |
| [[Lenalidomide (hemihydrate) (drug)]] 0.5 µM |  | 0.836× | -3.3 | 0.028 | 15/48 (NCI-H1792, SHP-77, …) | inconsistent across doses |  |
| [[Entrectinib (drug)]] 5 µM |  | 0.840× | -3.2 | 0.035 | 16/48 (KATO III, SW480, …) | top dose only |  |
| [[XRK3F2 (drug)]] 0.5 µM |  | **0.740×** | -3.2 | 0.044 | 19/47 (NCI-H1792, SK-MEL-2, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Bimiralisib (drug)]] 0.5 µM |  | **0.755×** | -2.9 | 0.084 | 11/48 (AsPC-1, C32, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.12 per unit of S-phase module lfc, -0.03 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6953. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A498 (line)]] | wt | 45.3 | 1 (1 ⚠) | 6 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.98× (z +10.5) ⚠ cell-cycle shift, explains ~90% of this change | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.356× (z -15.9) |
| [[HOP62 (line)]] | alt | 50.0 | 1 | 6 (2 ⚠) | [[TAK-901 (drug)]] 5 µM 5.20× (z +9.1) | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.231× (z -16.4) |
| [[LS 180 (line)]] | wt | 67.1 | 2 | 4 (1 ⚠) | [[PH-797804 (drug)]] 5 µM 6.27× (z +9.2) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.463× (z -11.6) |
| [[NCI-H460 (line)]] | wt | 56.7 | 1 | 5 (2 ⚠) | [[TAK-901 (drug)]] 5 µM 4.30× (z +9.0) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.393× (z -17.3) |
| [[SW48 (line)]] | wt | 80.1 | 0 | 6 (3 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.223× (z -11.4) |
| [[RKO (line)]] | wt | 98.1 | 2 | 3 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 6.12× (z +9.0) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.339× (z -16.0) |
| [[SW480 (line)]] | alt | 85.5 | 2 | 3 | [[TAK-901 (drug)]] 5 µM 4.17× (z +8.9) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.488× (z -13.4) |
| [[HEC-1-A (line)]] | alt | 83.5 | 3 | 1 | [[TAK-901 (drug)]] 5 µM 5.70× (z +10.0) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.496× (z -12.1) |
| [[LOX-IMVI (line)]] | wt | 56.6 | 1 | 3 (1 ⚠) | [[TAK-901 (drug)]] 0.05 µM 2.95× (z +10.4) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.337× (z -15.6) |
| [[MIA PaCa-2 (line)]] | alt | 77.3 | 0 | 4 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.235× (z -13.2) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.471× (z -10.1) |
| [[NCI-H2030 (line)]] | alt | 70.9 | 0 | 4 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.337× (z -15.1) |
| [[NCI-H23 (line)]] | alt | 89.8 | 0 | 4 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.247× (z -21.3) |
| [[SW 900 (line)]] | alt | 59.5 | 0 | 4 (1 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.186× (z -13.8) |
| [[C-33 A (line)]] | alt | 101 | 0 | 3 | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.273× (z -11.3) |
| [[C32 (line)]] | wt | 67.6 | 0 | 3 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.314× (z -13.8) |
| [[HS-578T (line)]] | alt | 81.2 | 0 | 3 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.352× (z -14.3) |
| [[LoVo (line)]] | wt | 73.9 | 1 | 2 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 7.04× (z +10.4) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.437× (z -13.2) |
| [[Panc 03.27 (line)]] | alt | 57.7 | 0 | 3 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.463× (z -11.3) |
| [[SK-MEL-2 (line)]] | alt | 99.4 | 0 | 3 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.237× (z -13.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.453× (z -11.7) |
| [[hTERT-HPNE (line)]] | wt | 43.0 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.246× (z -9.8) ⚠ toxic; transcription drop · without an alert: [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.276× (z -9.0) |
| [[NCI-H2347 (line)]] | alt | 68.8 | 1 (1 ⚠) | 1 | [[Homoharringtonine (drug)]] 5 µM 1.62× (z +8.6) ⚠ cell-cycle shift, explains ~90% of this change | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.504× (z -12.2) |
| [[PANC-1 (line)]] | alt | 58.8 | 0 | 2 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.483× (z -12.0) |
| [[SNU-423 (line)]] | alt | 56.7 | 0 | 2 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.504× (z -9.5) |
| [[SW1417 (line)]] | alt | 53.7 | 0 | 2 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.506× (z -9.5) |
| [[A-172 (line)]] | wt | 42.4 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.486× (z -9.8) |
| [[A549 (line)]] | wt | 48.6 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.98× (z +8.9) ⚠ cell-cycle shift, explains ~90% of this change | — |
| [[AN3 CA (line)]] | alt | 85.3 | 0 | 1 | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.178× (z -9.5) |
| [[AsPC-1 (line)]] | alt | 72.7 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.282× (z -19.6) |
| [[HepG2_C3A (line)]] | wt | 45.5 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.0936× (z -18.1) ⚠ toxic |
| [[Hs 766T (line)]] | wt | 49.1 | 0 | 1 | — | [[Thymol (drug)]] 0.5 µM 0.336× (z -9.7) |
| [[J82 (line)]] | alt | 71.5 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.509× (z -9.3) |
| [[KATO III (line)]] | alt | 53.9 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.405× (z -8.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~97% of this change |
| [[NCI-H1573 (line)]] | alt | 43.9 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.554× (z -8.5) |
| [[NCI-H1792 (line)]] | alt | 55.3 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 6.68× (z +8.9) | — |
| [[RPMI-7951 (line)]] | alt | 84.4 | 0 | 1 | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.275× (z -11.9) |
| [[SHP-77 (line)]] | alt | 78.8 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.440× (z -12.1) |
| [[SNU-1 (line)]] | wt | 103 | 0 | 1 | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.255× (z -11.4) |
| [[SW 1271 (line)]] | alt | 55.4 | 0 | 1 | — | [[Peretinoin (drug)]] 0.05 µM 0.0497× (z -10.1) |
| [[A-427 (line)]] | wt | 87.0 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 45.9 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 26.5 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 68.7 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 36.9 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 55.2 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 98.5 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 47.3 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 53.3 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 61.7 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 60.5 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 50.4 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6953), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*89 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[POLR3H]] | +0.71 | +0.67 / +0.66 | both halves | 7e-06 |  |
| [[POLR1A]] | +0.70 | +0.55 / +0.75 | both halves | 1e-05 |  |
| [[LSG1]] | +0.69 | +0.62 / +0.67 | both halves | 7e-06 |  |
| [[LAS1L]] | +0.67 | +0.53 / +0.67 | both halves | 1e-05 |  |
| [[MRPS27]] | +0.66 | +0.58 / +0.65 | both halves | 7e-06 |  |
| [[MYBBP1A]] | +0.66 | +0.57 / +0.69 | both halves | 1e-05 | same gene group |
| [[NAA15]] | +0.66 | +0.51 / +0.71 | both halves | 1e-05 | same gene group |
| [[SARS2]] | +0.65 | +0.60 / +0.64 | both halves | 7e-06 |  |
| [[DIS3L2]] | +0.65 | +0.62 / +0.60 | both halves | 7e-06 |  |
| [[CLPB]] | +0.65 | +0.59 / +0.64 | both halves | 7e-06 |  |
| [[GCN1]] | +0.64 | +0.65 / +0.64 | both halves | 7e-06 | STRING 453 |
| [[EIF2S1]] | +0.64 | +0.56 / +0.68 | both halves | 1e-05 |  |

## Genes that move opposite

*11 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CERT1]] | -0.65 | -0.48 / -0.57 | both halves | 2e-05 |  |
| [[AAMDC]] | -0.64 | -0.63 / -0.66 | both halves | 7e-06 |  |
| [[RSRP1]] | -0.64 | -0.53 / -0.69 | both halves | 1e-05 |  |
| [[LNX2]] | -0.58 | -0.55 / -0.57 | both halves | 1e-05 |  |
| [[PIK3CA]] | -0.58 | -0.50 / -0.51 | both halves | 1e-05 |  |
| [[ZNF706]] | -0.56 | -0.49 / -0.61 | both halves | 1e-05 |  |
| [[TSC22D4]] | -0.56 | -0.41 / -0.56 | both halves | 4e-05 |  |
| [[ZNF821]] | -0.56 | -0.47 / -0.62 | both halves | 2e-05 |  |
| [[ERO1B]] | -0.55 | -0.55 / -0.52 | both halves | 1e-05 |  |
| [[TRIM36]] | -0.55 | -0.47 / -0.53 | both halves | 2e-05 | pathway: Antigen processing: Ubiquitination & Proteasome degradation |
| [[TXNDC16]] | -0.55 | -0.58 / -0.46 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PSMB5]] | B | PSMB5 activity lowers DCAF1's level | compounds that target PSMB5: 2 of 2 raise it (Bortezomib, Ixazomib / Ixazomib citrate) | 100% of the class's compounds vs 1.4% of all compounds | 0.071 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[TOP2A]] | B | TOP2A activity raises DCAF1's level | compounds that target TOP2A: 3 of 5 lower it (Doxorubicin, Epirubicin, Idarubicin) | 60% of the class's compounds vs 3.4% of all compounds | 0.095 | ⚠ off-target possible; 3 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 004]] — MYC targets v1; 245 genes; this gene is in the **+** arm (projection on the module's main direction 0.702). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.30).
- **Nodal map** (x, y) = (-13.4, -35.6); signed map (-7.7, -46.7). **Vector** length 94.4, 25.9% of its response variance represented; |z| ≥ 3 in 1,079 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[TAK-901 (drug)]] 5 µM |  | +5.5 | +12.0 |
|  | [[PH-797804 (drug)]] 5 µM |  | +4.9 | +10.3 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +4.6 | +5.8 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~23% of this change | +4.0 | -4.9 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | +3.8 | -6.8 |
|  | [[TAK-733 (drug)]] 5 µM |  | +2.9 | +0.8 |
|  | [[EX229 (drug)]] 5 µM |  | +2.8 | +1.7 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | +2.5 | +2.1 |
|  | [[Belumosudil (drug)]] 5 µM |  | +2.4 | -0.0 |
| fall | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | -6.2 | -14.3 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | -5.4 | -12.1 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift | -4.1 | -1.2 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -3.3 | -18.6 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | -3.1 | -5.3 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -3.1 | -5.5 |
|  | [[Ponatinib (drug)]] 5 µM |  | -1.9 | -4.3 |
|  | [[Radotinib (drug)]] 5 µM |  | -1.9 | -2.8 |
|  | [[Cabozantinib (S-malate) (drug)]] 5 µM |  | -1.6 | -1.7 |
|  | [[Cyclosporin A (drug)]] 5 µM |  | -1.5 | -1.0 |

## What is on record

|  |  |
|---|---|
| Name | DDB1 and CUL4 associated factor 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 3p21.2 — chr3:51,395,867-51,500,015 (-) |
| Ensembl biotype | protein_coding |
| Also known as | KIAA0800, MGC102804; previously VPRBP |
| Gene groups (HGNC) | DDB1 and CUL4 associated factors; Armadillo like helical domain containing |
| Reactome | 3 pathways, smallest: Antigen processing: Ubiquitination & Proteasome degradation; Class I MHC mediated antigen processing & presentation; Adaptive Immune System |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9Y4B6](https://www.uniprot.org/uniprotkb/Q9Y4B6) (DDB1- and CUL4-associated factor 1):

> Acts both as a substrate recognition component of E3 ubiquitin-protein ligase complexes and as an atypical serine/threonine-protein kinase, playing key roles in various processes such as cell cycle, telomerase regulation and histone modification. Probable substrate-specific adapter of a DCX (DDB1-CUL4-X-box) E3 ubiquitin-protein ligase complex, named CUL4A-RBX1-DDB1-DCAF1/VPRBP complex, which mediates ubiquitination and proteasome-dependent degradation of proteins such as NF2. Involved in the …

**Summary**, from NCBI Gene [9730](https://www.ncbi.nlm.nih.gov/gene/9730):

> Enables histone H2AT120 kinase activity; nuclear estrogen receptor binding activity; and ubiquitin-like ligase-substrate adaptor activity. Involved in several processes, including cell competition in a multicellular organism; negative regulation of transcription by RNA polymerase II; and positive regulation of protein catabolic process. Located in COP9 signalosome; fibrillar center; and nucleoplasm. Part of Cul4-RING E3 ubiquitin ligase complex. Is active in centrosome. [provided by Alliance of …

**Accessions** — [HGNC:30911](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:30911) · Entrez [9730](https://www.ncbi.nlm.nih.gov/gene/9730) · UniProt [Q9Y4B6](https://www.uniprot.org/uniprotkb/Q9Y4B6) · Ensembl [ENSG00000145041](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000145041)

## Data

Gene col 6953: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6953); `tables/drug_effects.parquet` (31 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6953, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6953]; `tensor/DDL_lfc|DDL_z.npy` [6953]; `embed/gene_vectors.npy` [6953]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6953 or target_col == 6953). Every well: [[DCAF1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/DCAF1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
