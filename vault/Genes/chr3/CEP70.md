---
symbol: "CEP70"
type: "gene"
col: 3523
ensembl_id: "ENSG00000114107"
name: "centrosomal protein 70"
location: "3q22.3"
module: 22
arm: "+"
pooled_cpm: 77.86
n_lines_expressing: 50
n_dd_up: 10
n_dd_down: 22
n_dd_up_clean: 9
n_dd_down_clean: 13
in_vector_space: true
direction_upstream: 3
direction_downstream: 0
tags: ["gene", "module/022"]
generated_by: "tahoemap"
---

# CEP70

*centrosomal protein 70* — 3q22.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 10 drug-doses (1 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 0.5 µM: 2.02× (z +14.6, q 3e-45, up in 42 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 22 drug-doses (9 with an alert ⚠); the strongest is [[Harringtonine (drug)]] 0.5 µM: 0.592× (z -10.8, q 1e-24, down in 39 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[GPSM2]] (+0.73, fdr 7e-06), [[MPHOSPH9]] (+0.71, fdr 7e-06), [[KANTR]] (+0.70, fdr 7e-06); moves opposite to [[ITPRIPL2]] (-0.64, fdr 1e-05), [[SPHK1]] (-0.58, fdr 5e-05), [[LINC00571]] (-0.55, fdr 7e-05).
> It is in [[Module 022]], a single-armed module (G2/M checkpoint).
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 3 with an alert ⚠. 10 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3523.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 0.5 µM |  | **2.02×** | +14.6 | 3e-45 | 42/48 (MIA PaCa-2, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 5 µM |  | **1.88×** | +13.1 | 1e-36 | 43/48 (MIA PaCa-2, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM |  | **1.77×** | +11.8 | 1e-29 | 41/48 (SW1417, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.59×** | +9.5 | 2e-19 | 40/48 (SW1417, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Brivudine (drug)]] 5 µM |  | **2.03×** | +7.6 | 3e-12 | 40/48 (HEC-1-A, SW480, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.22×** | +5.7 | 1e-06 | 24/48 (HOP62, HT-29, …) | all doses, stronger at high dose |  |
| [[NG25 (drug)]] 5 µM |  | **1.60×** | +5.1 | 3e-05 | 28/47 (NCI-H23, J82, …) | top dose only | cell-cycle shift (explains ~10% here); noisy plate (z scaled) |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.25×** | +4.3 | 0.001 | 20/48 (PANC-1, LoVo, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **1.21×** | +3.9 | 0.005 | 20/48 (SW480, Panc 03.27, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~13% of this change | **1.21×** | +3.9 | 0.006 | 22/48 (Hs 766T, HOP62, …) | all doses, stronger at high dose |  |
| [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~12% of this change | 1.18× | +3.8 | 0.008 | 17/49 (CFPAC-1, NCI-H23, …) | rises with dose | noisy plate (z scaled) |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.06× | +3.7 | 0.011 | 3/49 (MIA PaCa-2, NCI-H23, …) | inconsistent across doses |  |
| [[Cobimetinib (drug)]] 5 µM |  | 1.19× | +3.5 | 0.018 | 18/47 (NCI-H23, CFPAC-1, …) | rises with dose |  |
| [[Retinoic acid (drug)]] 5 µM |  | 1.12× | +3.2 | 0.047 | 10/49 (CFPAC-1, A-172, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 30 in all, 13 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 22 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 3523.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Harringtonine (drug)]] 0.5 µM |  | **0.592×** | -10.8 | 1e-24 | 39/48 (NCI-H460, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | **0.634×** | -9.4 | 1e-18 | 39/48 (SNU-423, SW480, …) | top dose only |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.738×** | -8.9 | 1e-16 | 37/48 (A498, SNU-1, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.669×** | -8.3 | 1e-14 | 38/48 (NCI-H460, A498, …) | inconsistent across doses |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.679×** | -8.0 | 1e-13 | 31/48 (NCI-H460, NCI-H1792, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.711×** | -6.8 | 1e-09 | 27/48 (NCI-H460, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.716×** | -6.6 | 3e-09 | 26/47 (NCI-H460, SNU-1, …) | top dose only | cell-cycle shift (explains ~8% here) |
| [[Selinexor (drug)]] 5 µM |  | **0.806×** | -6.3 | 2e-08 | 24/48 (H4, NCI-H2347, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~1% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~18% of this change | **0.806×** | -6.3 | 2e-08 | 25/48 (NCI-H460, NCI-H2030, …) | rises with dose |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.728×** | -6.3 | 2e-08 | 25/49 (NCI-H460, HS-578T, …) | top dose only | cell-cycle shift (explains ~17% here) |
| [[PH-797804 (drug)]] 5 µM |  | **0.604×** | -5.5 | 3e-06 | 26/48 (SW 900, PANC-1, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Belumosudil (drug)]] 5 µM |  | **0.767×** | -5.3 | 6e-06 | 26/48 (HS-578T, PANC-1, …) | top dose only |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~24% of this change | **0.775×** | -5.1 | 2e-05 | 26/48 (A-427, NCI-H460, …) | top dose only |  |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~12% of this change | **0.801×** | -4.6 | 2e-04 | 23/48 (PANC-1, A498, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~27% of this change | **0.797×** | -4.5 | 3e-04 | 22/47 (NCI-H460, RKO, …) | rises with dose |  |
| [[Amsacrine (drug)]] 5 µM |  | 0.859× | -4.4 | 3e-04 | 16/48 (PANC-1, LS 180, …) | top dose only |  |
| [[TAK-901 (drug)]] 5 µM |  | **0.678×** | -4.2 | 8e-04 | 19/49 (SNU-1, NCI-H460, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~2% here); composition shift; noisy plate (z scaled) |
| [[PF-06260933 (drug)]] 5 µM |  | **0.710×** | -3.7 | 0.006 | 16/48 (SW480, HT-29, …) | top dose only | noisy plate (z scaled) |
| [[Filgotinib (drug)]] 5 µM |  | 0.845× | -3.5 | 0.013 | 18/48 (SW1417, J82, …) | all doses, stronger at high dose |  |
| [[Peretinoin (drug)]] 5 µM |  | 0.842× | -3.4 | 0.015 | 18/47 (NCI-H1573, SK-MEL-2, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.16 per unit of S-phase module lfc, +0.08 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3523. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A498 (line)]] | wt | 74.0 | 15 | 4 (1 ⚠) | [[Triamcinolone (drug)]] 0.5 µM 2.73× (z +12.3) | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM 0.484× (z -12.5) |
| [[CFPAC-1 (line)]] | alt | 87.3 | 16 | 0 | [[Budesonide (drug)]] 0.5 µM 3.22× (z +11.7) | — |
| [[NCI-H460 (line)]] | wt | 76.0 | 0 | 7 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.324× (z -16.4) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Homoharringtonine (drug)]] 0.05 µM 0.228× (z -15.2) |
| [[SW480 (line)]] | alt | 76.5 | 5 (1 ⚠) | 1 | [[Panobinostat (drug)]] 5 µM 2.15× (z +10.4) | [[Auranofin (drug)]] 5 µM 0.442× (z -11.1) |
| [[SW1417 (line)]] | alt | 86.1 | 5 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.95× (z +10.2) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 2.50× (z +10.0) | — |
| [[AsPC-1 (line)]] | alt | 28.5 | 4 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.61× (z +9.9) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 3.66× (z +9.5) | — |
| [[MIA PaCa-2 (line)]] | alt | 90.3 | 3 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 3.44× (z +13.0) | [[AZD2858 (drug)]] 0.5 µM 0.319× (z -8.6) ⚠ toxic |
| [[PANC-1 (line)]] | alt | 139 | 2 | 2 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 1.99× (z +10.1) | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM 0.648× (z -9.1) |
| [[HEC-1-A (line)]] | alt | 97.0 | 3 | 0 | [[Panobinostat (drug)]] 0.5 µM 2.21× (z +10.1) | — |
| [[HT-29 (line)]] | alt | 43.7 | 2 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.38× (z +10.7) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 2.69× (z +8.6) | [[Lonafarnib (drug)]] 5 µM 0.152× (z -8.6) ⚠ toxic |
| [[A-427 (line)]] | wt | 172 | 0 | 2 (1 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.367× (z -12.0) ⚠ cell-cycle shift, explains ~24% of this change · without an alert: [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM 0.546× (z -10.6) |
| [[H4 (line)]] | wt | 94.2 | 0 | 2 | — | [[Selinexor (drug)]] 5 µM 0.256× (z -13.5) |
| [[Hs 766T (line)]] | wt | 30.1 | 1 | 1 | [[Panobinostat (drug)]] 0.5 µM 3.99× (z +9.4) | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM 0.313× (z -11.1) |
| [[HS-578T (line)]] | alt | 78.6 | 0 | 2 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.357× (z -10.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~15% of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 0.396× (z -9.2) |
| [[LS 180 (line)]] | wt | 59.3 | 2 | 0 | [[Panobinostat (drug)]] 5 µM 2.48× (z +9.8) | — |
| [[Panc 03.27 (line)]] | alt | 88.0 | 1 (1 ⚠) | 1 | [[Homoharringtonine (drug)]] 5 µM 2.25× (z +11.3) ⚠ cell-cycle shift, would explain all of this change | [[Auranofin (drug)]] 5 µM 0.409× (z -8.8) |
| [[RKO (line)]] | wt | 45.2 | 2 | 0 | [[Panobinostat (drug)]] 0.5 µM 2.83× (z +8.9) | — |
| [[SNU-1 (line)]] | wt | 70.8 | 0 | 2 (1 ⚠) | — | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM 0.266× (z -11.8) |
| [[A549 (line)]] | wt | 54.0 | 0 | 1 | — | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM 0.537× (z -8.5) |
| [[AN3 CA (line)]] | alt | 104 | 0 | 1 | — | [[Auranofin (drug)]] 5 µM 0.202× (z -10.0) |
| [[NCI-H1573 (line)]] | alt | 65.7 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.463× (z -11.1) ⚠ cell-cycle shift, explains ~18% of this change |
| [[NCI-H1792 (line)]] | alt | 59.1 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.385× (z -8.7) |
| [[NCI-H2030 (line)]] | alt | 81.7 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.478× (z -11.8) ⚠ cell-cycle shift, explains ~18% of this change |
| [[NCI-H2347 (line)]] | alt | 95.8 | 0 | 1 | — | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM 0.582× (z -8.8) |
| [[NCI-H661 (line)]] | alt | 78.8 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.222× (z -9.1) ⚠ cell-cycle shift, explains ~18% of this change |
| [[SHP-77 (line)]] | alt | 94.1 | 0 | 1 | — | [[Auranofin (drug)]] 5 µM 0.316× (z -10.4) |
| [[SNU-423 (line)]] | alt | 74.4 | 0 | 1 | — | [[Auranofin (drug)]] 5 µM 0.269× (z -11.9) |
| [[SW 1271 (line)]] | alt | 123 | 0 | 1 | — | [[DT-061 (drug)]] 0.05 µM 0.124× (z -8.8) |
| [[A-172 (line)]] | wt | 64.6 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 63.9 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 90.1 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 73.9 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 66.6 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 51.9 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 81.9 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 45.0 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 55.0 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 46.7 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 74.8 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 112 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 48.7 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 22.7 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 49.6 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 99.1 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 56.9 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 79.1 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 128 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 72.5 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 75.4 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 58.5 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3523), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*76 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GPSM2]] | +0.73 | +0.61 / +0.66 | both halves | 7e-06 |  |
| [[MPHOSPH9]] | +0.71 | +0.60 / +0.69 | both halves | 7e-06 |  |
| [[KANTR]] | +0.70 | +0.74 / +0.58 | both halves | 7e-06 |  |
| [[PSRC1]] | +0.65 | +0.60 / +0.54 | both halves | 1e-05 |  |
| [[CEP131]] | +0.63 | +0.52 / +0.53 | both halves | 1e-05 | pathway: AURKA Activation by TPX2; STRING 530 |
| [[IFT122]] | +0.62 | +0.58 / +0.52 | both halves | 1e-05 | pathway: Assembly of the 9+0 primary cilium |
| [[NEURL1B]] | +0.62 | +0.53 / +0.56 | both halves | 1e-05 |  |
| [[CEP57L1]] | +0.62 | +0.49 / +0.54 | both halves | 1e-05 |  |
| [[NEK2]] | +0.62 | +0.57 / +0.55 | both halves | 1e-05 | pathway: AURKA Activation by TPX2 |
| [[PIF1]] | +0.61 | +0.67 / +0.57 | both halves | 1e-05 |  |
| [[DLGAP5]] | +0.61 | +0.57 / +0.55 | both halves | 1e-05 |  |
| [[CDKN3]] | +0.61 | +0.47 / +0.58 | both halves | 2e-05 |  |

## Genes that move opposite

*24 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ITPRIPL2]] | -0.64 | -0.57 / -0.59 | both halves | 1e-05 |  |
| [[SPHK1]] | -0.58 | -0.40 / -0.50 | both halves | 5e-05 |  |
| [[LINC00571]] | -0.55 | -0.41 / -0.37 | both halves | 7e-05 |  |
| [[BCL10-AS1]] | -0.55 | -0.46 / -0.39 | both halves | 5e-05 |  |
| [[CSTF3]] | -0.53 | -0.37 / -0.35 | both halves | 1e-04 |  |
| [[MCPH1]] | -0.53 | -0.37 / -0.34 | both halves | 1e-04 |  |
| [[LIX1-AS1]] | -0.52 | -0.45 / -0.27 | both halves | 3e-04 |  |
| [[NEK8]] | -0.52 | -0.36 / -0.34 | both halves | 1e-04 |  |
| [[MRM1]] | -0.52 | -0.44 / -0.36 | both halves | 1e-04 |  |
| [[HCG17]] | -0.52 | -0.47 / -0.24 | both halves | 5e-04 |  |
| [[MZF1-AS1]] | -0.52 | -0.38 / -0.31 | both halves | 2e-04 |  |
| [[PIGW]] | -0.51 | -0.44 / -0.30 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity raises CEP70's level | compounds that target TOP2A: 4 of 5 lower it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 4.8% of all compounds | 0.028 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[HDAC1]], [[HDAC2]], [[HDAC3]], [[HDAC8]], [[HDAC10]], [[HDAC11]] | B | HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11 activity lowers CEP70's level | compounds that target HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11: 2 of 2 raise it (Panobinostat, Tucidinostat) | 100% of the class's compounds vs 1.7% of all compounds | 0.084 | ⚠ off-target possible; 2 compounds; artifact flags; shared targets |
| [[HDAC6]] | B | HDAC6 activity lowers CEP70's level | compounds that target HDAC6: 2 of 2 raise it (Belinostat, Panobinostat) | 100% of the class's compounds vs 1.7% of all compounds | 0.084 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 022]] — G2/M checkpoint; 185 genes; every member is in the + arm (projection on the module's main direction 0.511). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.26; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-33.1, -54.4); signed map (-47.0, -39.4). **Vector** length 136, 43.4% of its response variance represented; |z| ≥ 3 in 1,457 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *Processing of antigen in germinal center B cells* (reactome, mean cos +0.50 to 9); *MHC class II antigen presentation* (reactome, mean cos +0.50 to 9).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[NG25 (drug)]] 5 µM |  | +5.8 | +5.1 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | +4.8 | +9.5 |
|  | [[Belinostat (drug)]] 5 µM |  | +4.5 | +11.8 |
|  | [[Brivudine (drug)]] 5 µM |  | +4.4 | +7.6 |
|  | [[Belinostat (drug)]] 0.5 µM |  | +3.9 | +3.9 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +3.3 | +2.8 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | +3.2 | +3.0 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.9 | +5.7 |
|  | [[Abemaciclib (drug)]] 0.5 µM |  | +2.3 | +2.2 |
| fall | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -10.0 | -8.9 |
|  | [[Auranofin (drug)]] 5 µM |  | -9.7 | -9.4 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -9.4 | -10.8 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~24% of this change | -8.9 | -5.1 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -8.2 | -8.3 |
|  | [[Belumosudil (drug)]] 5 µM |  | -5.7 | -5.3 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | -4.3 | -3.1 |

## What is on record

|  |  |
|---|---|
| Name | centrosomal protein 70 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 3q22.3 — chr3:138,494,344-138,594,538 (-) |
| Ensembl biotype | protein_coding |
| Also known as | BITE, FLJ13036 |
| Reactome | 17 pathways, smallest: Loss of Nlp from mitotic centrosomes; Loss of proteins required for interphase microtubule organization from the centrosome; AURKA Activation by TPX2 |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8NHQ1](https://www.uniprot.org/uniprotkb/Q8NHQ1) (Centrosomal protein of 70 kDa):

> Plays a role in the organization of both preexisting and nascent microtubules in interphase cells. During mitosis, required for the organization and orientation of the mitotic spindle.

**Summary**, from NCBI Gene [80321](https://www.ncbi.nlm.nih.gov/gene/80321):

> Enables identical protein binding activity. Predicted to be involved in cilium assembly. Predicted to act upstream of or within several processes, including microtubule cytoskeleton organization; single fertilization; and spermatid development. Located in centrosome. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:29972](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:29972) · Entrez [80321](https://www.ncbi.nlm.nih.gov/gene/80321) · UniProt [Q8NHQ1](https://www.uniprot.org/uniprotkb/Q8NHQ1) · Ensembl [ENSG00000114107](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000114107)

## Data

Gene col 3523: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3523); `tables/drug_effects.parquet` (44 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3523, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3523]; `tensor/DDL_lfc|DDL_z.npy` [3523]; `embed/gene_vectors.npy` [3523]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3523 or target_col == 3523). Every well: [[CEP70 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CEP70.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
