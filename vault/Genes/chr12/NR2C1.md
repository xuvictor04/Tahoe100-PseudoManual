---
symbol: "NR2C1"
type: "gene"
col: 4221
ensembl_id: "ENSG00000120798"
name: "nuclear receptor subfamily 2 group C member 1"
location: "12q22"
module: 10
arm: "-"
pooled_cpm: 67.0
n_lines_expressing: 50
n_dd_up: 3
n_dd_down: 16
n_dd_up_clean: 3
n_dd_down_clean: 13
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/010"]
generated_by: "tahoemap"
---

# NR2C1

*nuclear receptor subfamily 2 group C member 1* — 12q22

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 3 drug-doses (none with an alert); the strongest is [[Belinostat (drug)]] 5 µM: 1.25× (z +5.3, q 6e-05, up in 25 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 16 drug-doses (3 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.616× (z -15.0, q 0e+00, down in 43 of 48 measured lines).
> Its strongest partners by |cos| (98 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CRLF3]] (+0.68, fdr 8e-06), [[CKLF]] (+0.68, fdr 2e-05), [[PBX4]] (+0.65, fdr 3e-05); moves opposite to [[TSGA10]] (-0.69, fdr 2e-04), [[LINC00571]] (-0.67, fdr 4e-05), [[EIF4G2]] (-0.66, fdr 1e-05).
> It sits in the **-** arm of [[Module 010]].
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 6 with an alert ⚠. 3 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4221.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Belinostat (drug)]] 5 µM |  | **1.25×** | +5.3 | 6e-05 | 25/48 (CFPAC-1, SW480, …) | rises with dose | cell-cycle shift (explains ~4% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.23×** | +5.0 | 1e-04 | 21/48 (SNU-423, SW 900, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 5 µM |  | 1.16× | +4.4 | 0.002 | 12/48 (NCI-H2347, LoVo, …) | all doses, stronger at high dose |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~22% of this change | 1.19× | +4.0 | 0.007 | 17/47 (AsPC-1, KATO III, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.17× | +3.7 | 0.021 | 18/48 (CFPAC-1, LS 180, …) | all doses, flat |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~10% of this change | 1.17× | +3.7 | 0.021 | 19/48 (CFPAC-1, NCI-H2347, …) | all doses, flat |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~12% of this change | 1.16× | +3.5 | 0.028 | 18/48 (LoVo, SW480, …) | all doses, flat |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~24% of this change | 1.16× | +3.5 | 0.028 | 11/48 (AsPC-1, NCI-H2347, …) | rises with dose |  |
| [[Brivudine (drug)]] 5 µM |  | **1.32×** | +3.5 | 0.028 | 13/49 (SNU-1, RKO, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.15× | +3.3 | 0.046 | 16/47 (C-33 A, SW480, …) | inconsistent across doses | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 21 in all, 6 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 16 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 4221.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.616×** | -15.0 | 0e+00 | 43/48 (NCI-H1573, LS 180, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.621×** | -14.6 | 1e-45 | 40/48 (AsPC-1, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.628×** | -10.6 | 3e-24 | 34/43 (LoVo, SNU-1, …) | all doses, flat | cell-cycle shift (explains ~1% here); composition shift |
| [[Auranofin (drug)]] 5 µM |  | **0.647×** | -10.4 | 4e-23 | 37/48 (NCI-H23, MIA PaCa-2, …) | top dose only |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.641×** | -9.8 | 1e-20 | 31/45 (SNU-1, NCI-H1792, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.670×** | -9.5 | 1e-19 | 33/49 (NCI-H23, SNU-1, …) | all doses, flat | cell-cycle shift (explains ~3% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.684×** | -9.0 | 1e-17 | 31/48 (A-427, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.716×** | -7.6 | 1e-12 | 34/48 (hTERT-HPNE, HOP62, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.735×** | -7.3 | 2e-11 | 34/48 (AN3 CA, C32, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here); position effect removed |
| [[Harringtonine (drug)]] 5 µM |  | **0.734×** | -7.1 | 1e-10 | 32/48 (C32, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here); composition shift; position effect removed |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.790×** | -6.9 | 3e-10 | 23/48 (A-427, HOP62, …) | top dose only |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.747×** | -6.7 | 1e-09 | 32/50 (LS 180, C-33 A, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.761×** | -6.5 | 4e-09 | 30/48 (NCI-H1573, NCI-H460, …) | top dose only | cell-cycle shift (explains ~13% here); composition shift |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.940× | -5.4 | 2e-06 | 0/49 | inconsistent across doses |  |
| [[Belumosudil (drug)]] 5 µM |  | **0.831×** | -4.2 | 1e-03 | 20/48 (NCI-H1792, A498, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | 0.862× | -3.5 | 0.015 | 17/48 (NCI-H460, HEC-1-A, …) | all doses, stronger at high dose |  |
| [[TAK-733 (drug)]] 5 µM |  | **0.758×** | -3.4 | 0.018 | 12/48 (HEC-1-A, AsPC-1, …) | top dose only | noisy plate (z scaled) |
| [[Diammonium Glycyrrhizinate (drug)]] 0.5 µM |  | 0.872× | -3.2 | 0.036 | 13/48 (HOP62, HS-578T, …) | inconsistent across doses |  |
| [[Abemaciclib (drug)]] 5 µM |  | **0.775×** | -3.2 | 0.044 | 15/48 (KATO III, MIA PaCa-2, …) | top dose only | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.06 per unit of S-phase module lfc, -0.13 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4221. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[C32 (line)]] | wt | 46.1 | 0 | 9 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.241× (z -16.0) |
| [[NCI-H1573 (line)]] | alt | 70.5 | 0 | 8 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.305× (z -17.2) |
| [[NCI-H2030 (line)]] | alt | 117 | 0 | 5 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.339× (z -11.9) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.458× (z -11.6) |
| [[NCI-H460 (line)]] | wt | 57.8 | 0 | 5 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.430× (z -14.3) |
| [[LoVo (line)]] | wt | 92.8 | 0 | 4 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.113× (z -27.1) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.419× (z -14.5) |
| [[MIA PaCa-2 (line)]] | alt | 78.7 | 0 | 4 (1 ⚠) | — | [[Auranofin (drug)]] 5 µM 0.373× (z -10.9) |
| [[NCI-H1792 (line)]] | alt | 88.4 | 0 | 4 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.363× (z -15.1) |
| [[J82 (line)]] | alt | 68.2 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.382× (z -10.6) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.537× (z -9.5) |
| [[LS 180 (line)]] | wt | 72.0 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.434× (z -11.8) |
| [[NCI-H23 (line)]] | alt | 82.5 | 0 | 3 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.103× (z -26.2) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.320× (z -16.9) |
| [[SNU-1 (line)]] | wt | 98.1 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0913× (z -22.0) ⚠ toxic; transcription drop |
| [[A549 (line)]] | wt | 83.9 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.337× (z -11.9) ⚠ toxic; transcription drop |
| [[AN3 CA (line)]] | alt | 58.4 | 0 | 2 (1 ⚠) | — | [[Harringtonine (drug)]] 0.5 µM 0.0748× (z -14.4) |
| [[AsPC-1 (line)]] | alt | 90.4 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.257× (z -18.1) |
| [[C-33 A (line)]] | alt | 136 | 0 | 2 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.486× (z -9.4) |
| [[Panc 03.27 (line)]] | alt | 44.8 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.378× (z -9.0) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.490× (z -9.0) |
| [[SW 900 (line)]] | alt | 72.9 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.457× (z -9.9) |
| [[A-172 (line)]] | wt | 34.6 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.378× (z -12.4) |
| [[A-427 (line)]] | wt | 58.2 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.252× (z -14.3) |
| [[A498 (line)]] | wt | 48.7 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.529× (z -8.6) |
| [[CHP-212 (line)]] | wt | 66.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.174× (z -9.6) ⚠ toxic; transcription drop |
| [[COLO 205 (line)]] | alt | 53.1 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.409× (z -9.2) |
| [[HEC-1-A (line)]] | alt | 102 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.536× (z -10.3) |
| [[HOP62 (line)]] | alt | 45.9 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.513× (z -9.6) |
| [[HS-578T (line)]] | alt | 37.3 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.409× (z -11.0) |
| [[hTERT-HPNE (line)]] | wt | 33.1 | 0 | 1 | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.262× (z -8.6) |
| [[KATO III (line)]] | alt | 63.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.316× (z -12.6) ⚠ toxic; transcription drop |
| [[LOX-IMVI (line)]] | wt | 60.7 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.494× (z -10.3) |
| [[NCI-H2347 (line)]] | alt | 44.7 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.551× (z -9.0) |
| [[NCI-H596 (line)]] | alt | 64.9 | 0 | 1 (1 ⚠) | — | [[Pentoxifylline (drug)]] 0.05 µM 0.178× (z -11.8) ⚠ transcription drop |
| [[SW48 (line)]] | wt | 66.5 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.284× (z -9.1) |
| [[SW480 (line)]] | alt | 83.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.578× (z -8.6) ⚠ toxic; transcription drop |
| [[BT-474 (line)]] | alt | 49.3 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 40.4 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 44.9 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 61.6 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 62.3 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 55.9 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 58.0 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 55.1 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 71.2 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 86.3 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 55.5 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 41.3 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 77.0 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 37.0 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 45.9 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 42.4 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 78.8 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 77.3 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4221), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*48 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CRLF3]] | +0.68 | +0.67 / +0.58 | both halves | 8e-06 |  |
| [[CKLF]] | +0.68 | +0.65 / +0.47 | both halves | 2e-05 |  |
| [[PBX4]] | +0.65 | +0.62 / +0.46 | both halves | 3e-05 |  |
| [[TECPR1]] | +0.64 | +0.54 / +0.48 | both halves | 2e-05 |  |
| [[BRAT1]] | +0.63 | +0.54 / +0.51 | both halves | 1e-05 |  |
| [[ABHD6]] | +0.62 | +0.45 / +0.52 | both halves | 3e-05 |  |
| [[BCR]] | +0.62 | +0.63 / +0.41 | both halves | 4e-05 |  |
| [[DPY30]] | +0.60 | +0.57 / +0.42 | both halves | 4e-05 |  |
| [[DENND6A]] | +0.60 | +0.56 / +0.52 | both halves | 1e-05 |  |
| [[WRAP73]] | +0.60 | +0.51 / +0.41 | both halves | 4e-05 |  |
| [[SLC9A6]] | +0.60 | +0.63 / +0.35 | both halves | 1e-04 |  |
| [[GNA12]] | +0.60 | +0.64 / +0.34 | both halves | 1e-04 |  |

## Genes that move opposite

*52 of its nearest partners move opposite, 2 of them with an alert (⚠; 2 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TSGA10]] | -0.69 | -0.72 / -0.29 | both halves | 2e-04 |  |
| [[LINC00571]] | -0.67 | -0.66 / -0.42 | both halves | 4e-05 |  |
| [[EIF4G2]] | -0.66 | -0.56 / -0.50 | both halves | 1e-05 |  |
| [[PDCL3P4]] | -0.65 | -0.66 / -0.42 | both halves | 4e-05 |  |
| [[CCDC90B-AS1]] | -0.65 | -0.63 / -0.45 | both halves | 3e-05 |  |
| [[PCNX4-DT]] | -0.64 | -0.62 / -0.43 | both halves | 3e-05 |  |
| [[ATXN1L]] | -0.64 | -0.63 / -0.37 | both halves | 8e-05 |  |
| [[PKN2-AS1]] | -0.63 | -0.59 / -0.37 | both halves | 8e-05 |  |
| [[CAPN3]] | -0.62 | -0.59 / -0.45 | both halves | 3e-05 |  |
| [[MMADHC-DT]] | -0.62 | -0.58 / -0.38 | both halves | 6e-05 |  |
| [[TMEM202-AS1]] | -0.62 | -0.61 / -0.30 | both halves | 2e-04 |  |
| [[UBE3B]] | -0.61 | -0.62 / -0.38 | both halves | 7e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity raises NR2C1's level | compounds that target TOP2A: 4 of 5 lower it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 3.4% of all compounds | 0.015 | ⚠ off-target possible; 4 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 010]]; 217 genes; this gene is in the **-** arm (projection on the module's main direction -0.588). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.32).
- **Nodal map** (x, y) = (4.6, 5.0); signed map (-40.8, -10.0). **Vector** length 108, 27.1% of its response variance represented; |z| ≥ 3 in 983 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Belinostat (drug)]] 5 µM |  | +6.0 | +5.3 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~10% of this change | +5.4 | +3.7 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~0% of this change | +5.0 | +3.7 |
|  | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +4.7 | +2.2 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~12% of this change | +4.2 | +3.5 |
|  | [[Brivudine (drug)]] 5 µM |  | +3.8 | +3.5 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +3.5 | +4.4 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +2.8 | +1.3 |
|  | [[Gemcitabine (drug)]] 0.05 µM |  | +1.9 | +1.0 |
|  | [[Brivudine (drug)]] 0.5 µM |  | +1.8 | +2.0 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -8.3 | -15.0 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | -6.9 | -14.6 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -6.4 | -9.0 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -5.8 | -6.9 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | -5.3 | -6.7 |
|  | [[Auranofin (drug)]] 5 µM |  | -4.0 | -10.4 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -3.1 | -2.8 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | -2.9 | -2.3 |
|  | [[Cobimetinib (drug)]] 0.5 µM |  | -2.9 | -0.9 |

## What is on record

|  |  |
|---|---|
| Name | nuclear receptor subfamily 2 group C member 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 12q22 — chr12:95,020,229-95,073,628 (-) |
| Ensembl biotype | protein_coding |
| Also known as | TR2-11; previously TR2 |
| Gene groups (HGNC) | Nuclear receptor subfamily 2 group C |
| Reactome | 4 pathways, smallest: SUMOylation of intracellular receptors; Nuclear Receptor transcription pathway; SUMO E3 ligases SUMOylate target proteins |
| Matched by | ensembl_id |

**Function**, from UniProt [P13056](https://www.uniprot.org/uniprotkb/P13056) (Nuclear receptor subfamily 2 group C member 1):

> Orphan nuclear receptor. Binds the IR7 element in the promoter of its own gene in an autoregulatory negative feedback mechanism. Primarily repressor of a broad range of genes. Binds to hormone response elements (HREs) consisting of two 5'-AGGTCA-3' half site direct repeat consensus sequences. Together with NR2C2, forms the core of the DRED (direct repeat erythroid-definitive) complex that represses embryonic and fetal globin transcription. Also activator of OCT4 gene expression. May be involved …

**Summary**, from NCBI Gene [7181](https://www.ncbi.nlm.nih.gov/gene/7181):

> This gene encodes a nuclear hormone receptor characterized by a highly conserved DNA binding domain (DBD), a variable hinge region, and a carboxy-terminal ligand binding domain (LBD) that is typical for all members of the steroid/thyroid hormone receptor superfamily. This protein also belongs to a large family of ligand-inducible transcription factors that regulate gene expression by binding to specific DNA sequences within promoters of target genes. Multiple alternatively spliced transcript …

**Accessions** — [HGNC:7971](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:7971) · Entrez [7181](https://www.ncbi.nlm.nih.gov/gene/7181) · UniProt [P13056](https://www.uniprot.org/uniprotkb/P13056) · Ensembl [ENSG00000120798](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000120798)

## Data

Gene col 4221: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4221); `tables/drug_effects.parquet` (31 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4221, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4221]; `tensor/DDL_lfc|DDL_z.npy` [4221]; `embed/gene_vectors.npy` [4221]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4221 or target_col == 4221). Every well: [[NR2C1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/NR2C1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
