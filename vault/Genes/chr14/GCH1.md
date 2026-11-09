---
symbol: "GCH1"
type: "gene"
col: 5263
ensembl_id: "ENSG00000131979"
name: "GTP cyclohydrolase 1"
location: "14q22.2"
module: 93
arm: "+"
pooled_cpm: 29.52
n_lines_expressing: 48
n_dd_up: 29
n_dd_down: 4
n_dd_up_clean: 16
n_dd_down_clean: 3
in_vector_space: true
direction_upstream: 5
direction_downstream: 0
tags: ["gene", "module/093"]
generated_by: "tahoemap"
---

# GCH1

*GTP cyclohydrolase 1* — 14q22.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 29 drug-doses (13 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 3.42× (z +24.1, q 0e+00, up in 42 of 44 measured lines).
> Pooled over the cell lines (median), lowered significantly by 4 drug-doses (1 with an alert ⚠); the strongest is [[NG25 (drug)]] 5 µM: 0.524× (z -4.7, q 0.001, down in 19 of 43 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ABHD5]] (+0.60, fdr 7e-06), [[TLE4]] (+0.60, fdr 7e-06), [[FAM222A]] (+0.59, fdr 7e-06); moves opposite to [[ZNF133]] (-0.55, fdr 1e-05), [[XPO7]] (-0.51, fdr 3e-05), [[ZNF875]] (-0.50, fdr 3e-05).
> It is in [[Module 093]], a single-armed module (TNF-alpha signaling via NF-kB).
> Probable direction (from the cell lines, not proof of direct regulation): 5 arrows point to it, the strongest [[OVOL1]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 29 in all, 13 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 29 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 13 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5263.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **3.42×** | +24.1 | 0e+00 | 42/44 (SW480, BT-474, …) | rises with dose | cell-cycle shift (explains ~13% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **2.91×** | +20.9 | 0e+00 | 43/45 (NCI-H460, CFPAC-1, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~36% of this change | **2.90×** | +14.9 | 0e+00 | 44/46 (NCI-H2030, SW480, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **3.10×** | +14.5 | 3e-45 | 44/46 (NCI-H2030, SW480, …) | all doses, stronger at high dose |  |
| [[Tucidinostat (drug)]] 5 µM |  | **2.02×** | +13.7 | 1e-40 | 39/46 (NCI-H2030, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Harringtonine (drug)]] 5 µM |  | **2.56×** | +12.6 | 1e-34 | 40/45 (NCI-H460, Panc 03.27, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~39% of this change | **2.29×** | +11.5 | 6e-29 | 43/46 (NCI-H2030, A-427, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **2.06×** | +10.1 | 3e-22 | 40/46 (NCI-H2030, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~38% of this change | **1.92×** | +8.7 | 2e-16 | 30/45 (SW480, SW48, …) | rises with dose |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.55×** | +8.5 | 1e-15 | 27/46 (HOP62, MIA PaCa-2, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.83×** | +8.5 | 1e-15 | 35/46 (NCI-H460, SW 900, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~37% of this change | **1.82×** | +8.0 | 4e-14 | 30/46 (SW480, SW48, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~39% of this change | **1.74×** | +7.7 | 6e-13 | 27/45 (SW480, HCT15, …) | all doses, stronger at high dose |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.64×** | +6.9 | 3e-10 | 25/46 (NCI-H460, BT-474, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.59×** | +6.5 | 3e-09 | 23/44 (NCI-H460, A498, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.55×** | +6.1 | 4e-08 | 25/45 (RKO, A498, …) | rises with dose | cell-cycle shift (explains ~20% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.47×** | +5.4 | 2e-06 | 23/46 (SW48, SK-MEL-2, …) | rises with dose |  |
| [[HI-TOPK-032 (drug)]] 5 µM |  | **1.65×** | +3.6 | 0.007 | 14/44 (A-427, SW480, …) | top dose only | noisy plate (z scaled) |
| [[Epirubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.26×** | +3.2 | 0.033 | 8/46 (SNU-423, RKO, …) | rises with dose |  |
| [[Gemcitabine (drug)]] 0.5 µM |  | **1.24×** | +3.1 | 0.051 | 9/46 (RKO, J82, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Binimetinib (drug)]] 5 µM |  | **1.23×** | +3.0 | 0.063 | 13/46 (MIA PaCa-2, HOP62, …) | rises with dose | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, 1 with an alert ⚠. 4 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 5263.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[NG25 (drug)]] 5 µM |  | **0.524×** | -4.7 | 0.001 | 19/43 (J82, SNU-423, …) | top dose only | cell-cycle shift (explains ~23% here); noisy plate (z scaled) |
| [[Bosentan (hydrate) (drug)]] 5 µM |  | **0.753×** | -3.8 | 0.035 | 18/45 (HOP62, HS-578T, …) | top dose only |  |
| [[Ponatinib (drug)]] 5 µM |  | **0.766×** | -3.7 | 0.035 | 17/46 (SNU-423, J82, …) | top dose only |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **0.778×** | -3.5 | 0.058 | 16/43 (HepG2/C3A, J82, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Belumosudil (drug)]] 5 µM |  | 0.787× | -3.2 | 0.14 | 17/46 (NCI-H2347, RKO, …) | top dose only |  |
| [[Pasireotide (acetate) (drug)]] 5 µM |  | 0.856× | -3.1 | 0.20 | 7/47 (RPMI-7951, NCI-H1573, …) | top dose only |  |
| [[Diammonium Glycyrrhizinate (drug)]] 0.05 µM |  | 0.808× | -3.0 | 0.22 | 8/46 (LS 180, BT-474, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.64 per unit of S-phase module lfc, -0.22 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5263. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 36.4 | 12 (4 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 9.62× (z +24.9) | — |
| [[NCI-H2030 (line)]] | alt | 29.8 | 7 (3 ⚠) | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 8.00× (z +15.1) ⚠ cell-cycle shift, explains ~36% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 3.88× (z +13.8) | [[Digitoxin (drug)]] 5 µM 0.240× (z -10.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~52% of this change |
| [[SW480 (line)]] | alt | 27.6 | 7 (5 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.21× (z +17.7) | — |
| [[BT-474 (line)]] | alt | 53.0 | 5 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.15× (z +15.2) | — |
| [[MIA PaCa-2 (line)]] | alt | 28.8 | 5 (2 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.78× (z +11.5) | — |
| [[NCI-H23 (line)]] | alt | 15.9 | 5 (3 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 8.95× (z +11.9) ⚠ cell-cycle shift, explains ~36% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.41× (z +9.3) | — |
| [[SW48 (line)]] | wt | 63.5 | 3 (1 ⚠) | 2 (2 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.99× (z +10.3) | [[Dinaciclib (drug)]] 5 µM 0.137× (z -12.9) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[A-427 (line)]] | wt | 27.5 | 4 (3 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 5.02× (z +11.9) ⚠ cell-cycle shift, explains ~36% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 2.35× (z +8.8) | — |
| [[HOP62 (line)]] | alt | 15.4 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 11.1× (z +16.5) | — |
| [[CFPAC-1 (line)]] | alt | 53.2 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 7.24× (z +17.8) | — |
| [[H4 (line)]] | wt | 19.7 | 1 | 2 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.56× (z +9.1) | [[Glycyrrhizic acid (drug)]] 0.05 µM 0.0785× (z -8.9) |
| [[LOX-IMVI (line)]] | wt | 7.70 | 3 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.37× (z +10.9) | — |
| [[Panc 03.27 (line)]] | alt | 48.2 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.77× (z +14.4) | — |
| [[RKO (line)]] | wt | 32.1 | 2 | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.43× (z +11.4) | [[Homoharringtonine (drug)]] 0.5 µM 0.195× (z -10.9) |
| [[SK-MEL-2 (line)]] | alt | 13.7 | 3 (1 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 8.92× (z +9.9) ⚠ cell-cycle shift, explains ~36% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.15× (z +9.0) | — |
| [[SW 900 (line)]] | alt | 18.7 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 7.34× (z +12.7) | — |
| [[A549 (line)]] | wt | 33.1 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.23× (z +12.5) | — |
| [[HT-29 (line)]] | alt | 46.6 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.32× (z +10.5) | — |
| [[hTERT-HPNE (line)]] | wt | 26.8 | 1 | 1 | [[Homoharringtonine (drug)]] 5 µM 9.91× (z +11.3) | [[Lidocaine (hydrochloride) (drug)]] 0.05 µM 0.0640× (z -9.7) |
| [[LoVo (line)]] | wt | 58.4 | 2 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.88× (z +14.6) | — |
| [[LS 180 (line)]] | wt | 41.3 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.25× (z +14.3) | [[Dinaciclib (drug)]] 5 µM 0.0957× (z -19.7) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[NCI-H2347 (line)]] | alt | 48.5 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.18× (z +13.6) | — |
| [[SNU-423 (line)]] | alt | 23.7 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.98× (z +11.4) | — |
| [[A-172 (line)]] | wt | 12.7 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.99× (z +11.1) | — |
| [[A498 (line)]] | wt | 24.8 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.04× (z +13.6) | — |
| [[AsPC-1 (line)]] | alt | 16.0 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 8.40× (z +13.8) | — |
| [[C-33 A (line)]] | alt | 16.4 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.19× (z +11.2) | — |
| [[HCT15 (line)]] | alt | 39.3 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.88× (z +9.3) | — |
| [[HEC-1-A (line)]] | alt | 11.8 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.51× (z +12.2) | — |
| [[KATO III (line)]] | alt | 25.6 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.97× (z +10.5) | — |
| [[NCI-H1573 (line)]] | alt | 45.2 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.37× (z +8.5) | — |
| [[SHP-77 (line)]] | alt | 36.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.220× (z -10.0) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[SW1417 (line)]] | alt | 51.5 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.16× (z +12.2) | — |
| [[AN3 CA (line)]] | alt | 22.0 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 7.25 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 12.7 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 20.0 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 47.5 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 17.3 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 10.6 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 81.7 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 11.0 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 43.9 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 30.5 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 28.8 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 6.59 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 8.62 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 11.4 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 25.8 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 60.7 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5263), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*79 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ABHD5]] | +0.60 | +0.63 / +0.64 | both halves | 7e-06 |  |
| [[TLE4]] | +0.60 | +0.62 / +0.58 | both halves | 7e-06 |  |
| [[FAM222A]] | +0.59 | +0.63 / +0.58 | both halves | 7e-06 |  |
| [[GADD45B]] | +0.57 | +0.48 / +0.60 | both halves | 2e-05 | pathway: HALLMARK_APOPTOSIS |
| [[SLC9A1]] | +0.56 | +0.54 / +0.56 | both halves | 1e-05 |  |
| [[IRF1]] | +0.56 | +0.55 / +0.54 | both halves | 1e-05 | pathway: HALLMARK_APOPTOSIS |
| [[KLHL15]] | +0.56 | +0.52 / +0.52 | both halves | 1e-05 |  |
| [[ABTB2]] | +0.55 | +0.45 / +0.59 | both halves | 3e-05 |  |
| [[BCL6]] | +0.55 | +0.55 / +0.51 | both halves | 1e-05 | pathway: HALLMARK_TNFA_SIGNALING_VIA_NFKB |
| [[NFKBIZ]] | +0.55 | +0.55 / +0.53 | both halves | 1e-05 |  |
| [[MAFB]] | +0.55 | +0.52 / +0.54 | both halves | 1e-05 |  |
| [[DISP3]] | +0.54 | +0.47 / +0.60 | both halves | 2e-05 |  |

## Genes that move opposite

*21 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZNF133]] | -0.55 | -0.57 / -0.49 | both halves | 1e-05 |  |
| [[XPO7]] | -0.51 | -0.56 / -0.45 | both halves | 3e-05 |  |
| [[ZNF875]] | -0.50 | -0.47 / -0.43 | both halves | 3e-05 |  |
| [[MRPS27]] | -0.49 | -0.49 / -0.40 | both halves | 5e-05 |  |
| [[NUDCD3]] | -0.49 | -0.49 / -0.44 | both halves | 3e-05 |  |
| [[RFT1]] | -0.48 | -0.49 / -0.44 | both halves | 3e-05 |  |
| [[MRPS35]] | -0.48 | -0.47 / -0.49 | both halves | 2e-05 |  |
| [[TRMT61B]] | -0.47 | -0.34 / -0.47 | both halves | 1e-04 |  |
| [[PSMF1]] | -0.47 | -0.45 / -0.43 | both halves | 3e-05 |  |
| [[PWP1]] | -0.46 | -0.42 / -0.48 | both halves | 4e-05 |  |
| [[DIS3L2]] | -0.46 | -0.37 / -0.43 | both halves | 9e-05 | same gene group |
| [[XPNPEP3]] | -0.46 | -0.39 / -0.44 | both halves | 5e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*5 arrows, 5 of them with an alert ⚠; grade A 0, B 5, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[OVOL1]] | B | OVOL1 activity weakens GCH1's drug response | lines that do not express OVOL1 (31) vs lines expressing it (15) | the lines without OVOL1 respond 1.11× as strongly (z diff -0.86); strongest at Tucidinostat 5 µM: 2.48x vs 1.46x (z diff -3.5) | 0.006 | ⚠ within organs, on part of the lines; co-absent genes; also absent: GRHL2, ST14, TMEM30B; target measured in part of the lines; artifact flags |
| [[ELOVL7]] | B | ELOVL7 activity raises GCH1's level | lines that do not express ELOVL7 (11) vs lines expressing it (39) | 2.28× lower at baseline in the lines without ELOVL7 | 0.007 | ⚠ within organs, on part of the lines; also absent: KRT86; maybe low, not absent |
| [[TOP2A]] | B | TOP2A activity lowers GCH1's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 5.0% of all compounds | 0.032 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[OVOL1]] | B | OVOL1 activity raises GCH1's level | lines that do not express OVOL1 (33) vs lines expressing it (17) | 1.80× lower at baseline in the lines without OVOL1 | 0.086 | ⚠ within organs, on part of the lines; co-absent genes; also absent: GRHL2, ST14, TMEM30B |
| [[SRC]] | B | SRC activity raises GCH1's level | compounds that target SRC: 2 of 3 lower it (NG25, Ponatinib) | 67% of the class's compounds vs 1.1% of all compounds | 0.095 | ⚠ off-target possible; 2 compounds; shared targets; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 093]] — TNF-alpha signaling via NF-kB; 49 genes; every member is in the + arm (projection on the module's main direction 0.691). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (29.4, -27.2); signed map (4.0, 17.7). **Vector** length 97.8, 24.9% of its response variance represented; |z| ≥ 3 in 1,239 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +5.8 | +13.7 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +4.9 | +8.5 |
|  | [[PF-06260933 (drug)]] 5 µM |  | +3.5 | +2.2 |
|  | [[Harringtonine (drug)]] 5 µM |  | +3.1 | +12.6 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +2.9 | +24.1 |
|  | [[Betamethasone dipropionate (drug)]] 5 µM |  | +2.5 | +1.2 |
|  | [[Binimetinib (drug)]] 5 µM |  | +2.2 | +3.0 |
|  | [[Cytarabine (drug)]] 0.05 µM |  | +2.1 | +2.0 |
| fall | [[NG25 (drug)]] 5 µM |  | -3.9 | -4.7 |
|  | [[Ponatinib (drug)]] 5 µM |  | -3.5 | -3.7 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change | -3.3 | +1.3 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift | -3.3 | +0.7 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -3.0 | -0.1 |
|  | [[Tofacitinib (drug)]] 5 µM |  | -2.6 | -1.9 |
|  | [[PH-797804 (drug)]] 5 µM |  | -2.4 | -0.5 |
|  | [[Belumosudil (drug)]] 5 µM |  | -2.4 | -3.2 |

## What is on record

|  |  |
|---|---|
| Name | GTP cyclohydrolase 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 14q22.2 — chr14:54,842,008-54,902,826 (-) |
| Ensembl biotype | protein_coding |
| Also known as | GTPCH1, DYT5a; previously GCH, DYT5, DYT14 |
| Gene groups (HGNC) | MicroRNA protein coding host genes |
| Hallmark sets | INFLAMMATORY_RESPONSE, APOPTOSIS, UV_RESPONSE_UP, XENOBIOTIC_METABOLISM, INTERFERON_GAMMA_RESPONSE, TNFA_SIGNALING_VIA_NFKB |
| Reactome | 3 pathways, smallest: Tetrahydrobiopterin (BH4) synthesis, recycling, salvage and regulation; Metabolism of cofactors; Metabolism of vitamins and cofactors |
| Matched by | ensembl_id |

**Function**, from UniProt [P30793](https://www.uniprot.org/uniprotkb/P30793) (GTP cyclohydrolase 1):

> Positively regulates nitric oxide synthesis in umbilical vein endothelial cells (HUVECs). May be involved in dopamine synthesis. May modify pain sensitivity and persistence. Isoform GCH-1 is the functional enzyme, the potential function of the enzymatically inactive isoforms remains unknown.

**Summary**, from NCBI Gene [2643](https://www.ncbi.nlm.nih.gov/gene/2643):

> This gene encodes a member of the GTP cyclohydrolase family. The encoded protein is the first and rate-limiting enzyme in tetrahydrobiopterin (BH4) biosynthesis, catalyzing the conversion of GTP into 7,8-dihydroneopterin triphosphate. BH4 is an essential cofactor required by aromatic amino acid hydroxylases as well as nitric oxide synthases. Mutations in this gene are associated with malignant hyperphenylalaninemia and dopa-responsive dystonia. Several alternatively spliced transcript variants …

**Accessions** — [HGNC:4193](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:4193) · Entrez [2643](https://www.ncbi.nlm.nih.gov/gene/2643) · UniProt [P30793](https://www.uniprot.org/uniprotkb/P30793) · Ensembl [ENSG00000131979](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000131979)

## Data

Gene col 5263: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5263); `tables/drug_effects.parquet` (36 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5263, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5263]; `tensor/DDL_lfc|DDL_z.npy` [5263]; `embed/gene_vectors.npy` [5263]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5263 or target_col == 5263). Every well: [[GCH1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/GCH1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
