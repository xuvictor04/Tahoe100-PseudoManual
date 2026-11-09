---
symbol: "KPNA5"
type: "gene"
col: 12300
ensembl_id: "ENSG00000196911"
name: "karyopherin subunit alpha 5"
location: "6q22.1"
module: 17
arm: "+"
pooled_cpm: 56.11
n_lines_expressing: 50
n_dd_up: 10
n_dd_down: 9
n_dd_up_clean: 6
n_dd_down_clean: 3
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/017"]
generated_by: "tahoemap"
---

# KPNA5

*karyopherin subunit alpha 5* — 6q22.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 10 drug-doses (4 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 1.67× (z +17.7, q 0e+00, up in 42 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 9 drug-doses (6 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.550× (z -20.6, q 0e+00, down in 43 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ZDHHC17]] (+0.72, fdr 7e-06), [[NDUFA5]] (+0.67, fdr 7e-06), [[NBDY]] (+0.64, fdr 4e-05); moves opposite to [[FBXW7]] (-0.65, fdr 7e-06), [[PDCD6]] (-0.64, fdr 7e-06), [[ARPC5L]] (-0.64, fdr 2e-05).
> It sits in the **+** arm of [[Module 017]] (Intraflagellar transport).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 7 with an alert ⚠. 10 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 12300.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **1.67×** | +17.7 | 0e+00 | 42/48 (NCI-H1573, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.85×** | +15.0 | 0e+00 | 35/48 (HOP62, NCI-H460, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.55×** | +10.6 | 4e-24 | 38/48 (A-172, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.40×** | +7.8 | 7e-13 | 28/43 (HOP62, SHP-77, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **1.38×** | +7.5 | 7e-12 | 31/48 (NCI-H460, HOP62, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.36×** | +7.0 | 2e-10 | 26/45 (HOP62, NCI-H2030, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~18% of this change | **1.32×** | +6.9 | 5e-10 | 28/48 (NCI-H2347, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Tucidinostat (drug)]] 5 µM |  | **1.21×** | +6.5 | 6e-09 | 22/48 (HOP62, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~15% of this change | 1.18× | +5.7 | 7e-07 | 21/48 (NCI-H2347, KATO III, …) | rises with dose | low cells (technical?) |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~29% of this change | 1.20× | +4.4 | 6e-04 | 16/48 (SW480, KATO III, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 0.05 µM |  | 1.17× | +3.8 | 0.007 | 12/48 (RKO, NCI-H2347, …) | all doses, stronger at high dose |  |
| [[TAK-901 (drug)]] 5 µM |  | **1.33×** | +3.7 | 0.011 | 16/49 (NCI-H1573, SW480, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[NG25 (drug)]] 5 µM |  | **1.31×** | +3.4 | 0.029 | 13/47 (SW480, LoVo, …) | top dose only | cell-cycle shift (explains ~15% here); noisy plate (z scaled) |
| [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~42% of this change | 1.14× | +3.2 | 0.052 | 8/50 (MIA PaCa-2, AsPC-1, …) | rises with dose | noisy plate (z scaled) |
| [[Glycyrrhizic acid (drug)]] 5 µM |  | 1.14× | +3.1 | 0.066 | 6/48 (NCI-H2030, NCI-H661, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 24 in all, 13 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 9 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 12300.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.550×** | -20.6 | 0e+00 | 43/48 (NCI-H23, HEC-1-A, …) | top dose only | cell-cycle shift (explains ~13% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **0.657×** | -9.8 | 2e-20 | 36/50 (AN3 CA, HEC-1-A, …) | top dose only |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **0.663×** | -9.6 | 1e-19 | 34/48 (SNU-423, LOX-IMVI, …) | inconsistent across doses |  |
| [[Auranofin (drug)]] 5 µM |  | **0.713×** | -8.2 | 3e-14 | 32/48 (SW480, MIA PaCa-2, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~52% of this change | **0.725×** | -7.8 | 6e-13 | 28/48 (PANC-1, LOX-IMVI, …) | two highest doses |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~63% of this change | **0.763×** | -6.6 | 5e-09 | 26/48 (LOX-IMVI, HepG2/C3A, …) | rises with dose |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~75% of this change | **0.766×** | -6.5 | 7e-09 | 26/48 (PANC-1, LOX-IMVI, …) | two highest doses |  |
| [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **0.810×** | -5.1 | 2e-05 | 21/48 (SNU-423, PANC-1, …) | rises with dose |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 0.864× | -5.0 | 4e-05 | 23/48 (NCI-H2030, HEC-1-A, …) | top dose only |  |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.948× | -4.4 | 5e-04 | 1/49 (SW 1088) | inconsistent across doses |  |
| [[5-Azacytidine (drug)]] 5 µM |  | 0.845× | -4.1 | 0.002 | 17/48 (SW48, SW480, …) | top dose only |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~12% of this change | 0.847× | -4.0 | 0.003 | 18/48 (hTERT-HPNE, SW 1271, …) | inconsistent across doses | low cells (technical?) |
| [[vincristine (drug)]] 5 µM |  | **0.731×** | -4.0 | 0.003 | 16/46 (RPMI-7951, H4, …) | rises with dose | noisy plate (z scaled) |
| [[Peretinoin (drug)]] 0.5 µM |  | 0.850× | -4.0 | 0.003 | 12/47 (MIA PaCa-2, RPMI-7951, …) | two highest doses |  |
| [[Darinaparsin (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~37% of this change | 0.908× | -3.3 | 0.035 | 7/48 (MIA PaCa-2, NCI-H2347, …) | top dose only |  |
| [[S-Adenosyl-L-methionine (disulfate tosylate) (drug)]] 5 µM |  | 0.910× | -3.2 | 0.040 | 6/49 (RKO, KATO III, …) | top dose only |  |
| [[vincristine (drug)]] 0.5 µM |  | 0.835× | -3.1 | 0.055 | 14/48 (MIA PaCa-2, HEC-1-A, …) | rises with dose | low cells (technical?); noisy plate (z scaled) |
| [[Thymol (drug)]] 5 µM |  | 0.914× | -3.1 | 0.057 | 5/48 (CHP-212, Panc 03.27, …) | rises with dose |  |
| [[Glycyrrhizic acid (drug)]] 0.05 µM |  | 0.872× | -3.1 | 0.060 | 8/47 (SW48, CHP-212, …) | inconsistent across doses |  |
| [[Triamcinolone (drug)]] 0.05 µM |  | 0.884× | -3.0 | 0.069 | 6/48 (SNU-423, Panc 03.27, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.32 per unit of S-phase module lfc, +0.07 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 12300. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 40.5 | 6 (3 ⚠) | 2 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 4.33× (z +19.2) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 2.00× (z +12.8) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.413× (z -16.3) |
| [[LOX-IMVI (line)]] | wt | 93.8 | 1 | 6 (5 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.06× (z +12.8) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.406× (z -15.8) |
| [[HEC-1-A (line)]] | alt | 84.8 | 0 | 6 (5 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.408× (z -17.0) |
| [[NCI-H2030 (line)]] | alt | 55.9 | 3 (2 ⚠) | 2 (1 ⚠) | [[Dinaciclib (drug)]] 0.05 µM 3.76× (z +14.0) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 2.01× (z +11.3) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.479× (z -11.9) |
| [[PANC-1 (line)]] | alt | 148 | 3 (2 ⚠) | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.64× (z +10.5) | [[Panobinostat (drug)]] 5 µM 0.524× (z -9.6) ⚠ cell-cycle shift, explains ~75% of this change |
| [[A-172 (line)]] | wt | 36.7 | 3 (1 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 5 µM 3.70× (z +10.8) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 2.39× (z +10.6) | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.310× (z -9.6) ⚠ cell-cycle shift, explains ~30% of this change |
| [[AN3 CA (line)]] | alt | 107 | 0 | 4 (2 ⚠) | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.111× (z -14.3) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.294× (z -11.7) |
| [[HOP62 (line)]] | alt | 32.9 | 4 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 12.9× (z +21.0) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 2.84× (z +12.1) | — |
| [[J82 (line)]] | alt | 35.7 | 4 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 9.80× (z +15.0) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 2.83× (z +9.7) | — |
| [[RKO (line)]] | wt | 59.2 | 1 (1 ⚠) | 3 (2 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 3.79× (z +13.6) ⚠ toxic; transcription drop | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.358× (z -14.9) |
| [[HepG2_C3A (line)]] | wt | 67.0 | 0 | 3 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.311× (z -15.4) |
| [[NCI-H2347 (line)]] | alt | 41.3 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.64× (z +9.7) ⚠ toxic; transcription drop | — |
| [[Panc 03.27 (line)]] | alt | 45.2 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.20× (z +13.6) ⚠ toxic; transcription drop | — |
| [[RPMI-7951 (line)]] | alt | 59.8 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.05 µM 4.77× (z +11.7) ⚠ toxic; transcription drop | — |
| [[SNU-423 (line)]] | alt | 88.0 | 0 | 3 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.457× (z -13.4) |
| [[SW480 (line)]] | alt | 79.4 | 0 | 3 (1 ⚠) | — | [[Auranofin (drug)]] 5 µM 0.426× (z -12.2) |
| [[A-427 (line)]] | wt | 58.8 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.410× (z -10.2) |
| [[BT-474 (line)]] | alt | 68.3 | 1 | 1 | [[Homoharringtonine (drug)]] 5 µM 2.79× (z +10.1) | [[Medroxyprogesterone acetate (drug)]] 0.5 µM 0.226× (z -10.3) |
| [[hTERT-HPNE (line)]] | wt | 34.8 | 1 (1 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 5 µM 3.86× (z +9.1) ⚠ toxic; transcription drop | [[Docetaxel (drug)]] 0.05 µM 0.203× (z -11.1) ⚠ transcription drop; cell-cycle shift, explains ~12% of this change |
| [[NCI-H1573 (line)]] | alt | 50.0 | 1 | 1 | [[Homoharringtonine (drug)]] 5 µM 2.25× (z +13.3) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.535× (z -10.2) |
| [[NCI-H23 (line)]] | alt | 58.2 | 1 | 1 | [[Homoharringtonine (drug)]] 5 µM 1.79× (z +9.0) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.311× (z -18.0) |
| [[SHP-77 (line)]] | alt | 88.7 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.85× (z +15.4) ⚠ toxic; transcription drop | — |
| [[A498 (line)]] | wt | 23.0 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.77× (z +11.3) | — |
| [[A549 (line)]] | wt | 53.0 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.498× (z -10.0) |
| [[AsPC-1 (line)]] | alt | 17.5 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.26× (z +8.8) ⚠ toxic; transcription drop | — |
| [[C32 (line)]] | wt | 33.2 | 0 | 1 (1 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.259× (z -9.0) ⚠ cell-cycle shift, explains ~30% of this change |
| [[CFPAC-1 (line)]] | alt | 42.6 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.469× (z -10.9) |
| [[H4 (line)]] | wt | 36.3 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.309× (z -9.3) |
| [[HCT15 (line)]] | alt | 95.0 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.477× (z -9.9) |
| [[Hs 766T (line)]] | wt | 49.0 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.09× (z +8.9) | — |
| [[HS-578T (line)]] | alt | 40.3 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.411× (z -10.9) |
| [[HT-29 (line)]] | alt | 28.4 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.55× (z +10.5) | — |
| [[KATO III (line)]] | alt | 26.0 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.25× (z +8.5) | — |
| [[MIA PaCa-2 (line)]] | alt | 56.5 | 0 | 1 | — | [[Auranofin (drug)]] 5 µM 0.368× (z -10.4) |
| [[NCI-H1792 (line)]] | alt | 62.8 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.569× (z -8.6) |
| [[SW 1271 (line)]] | alt | 110 | 0 | 1 (1 ⚠) | — | [[Docetaxel (drug)]] 0.05 µM 0.127× (z -10.1) ⚠ transcription drop; cell-cycle shift, explains ~12% of this change |
| [[SW48 (line)]] | wt | 33.5 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.05 µM 5.59× (z +9.0) ⚠ toxic; transcription drop | — |
| [[C-33 A (line)]] | alt | 115 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 91.0 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 28.2 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 35.5 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 15.9 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 47.0 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 66.0 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 108 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 56.2 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 74.5 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 52.6 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 60.5 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 14.1 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 12300), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*69 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZDHHC17]] | +0.72 | +0.67 / +0.66 | both halves | 7e-06 |  |
| [[NDUFA5]] | +0.67 | +0.65 / +0.66 | both halves | 7e-06 |  |
| [[NBDY]] | +0.64 | +0.42 / +0.70 | both halves | 4e-05 |  |
| [[ZNF385C]] | +0.64 | +0.62 / +0.60 | both halves | 7e-06 |  |
| [[TAB2]] | +0.64 | +0.59 / +0.60 | both halves | 7e-06 |  |
| [[OCIAD1]] | +0.61 | +0.52 / +0.60 | both halves | 1e-05 |  |
| [[CHIC1]] | +0.61 | +0.57 / +0.61 | both halves | 9e-06 |  |
| [[CC2D2A]] | +0.60 | +0.54 / +0.60 | both halves | 1e-05 |  |
| [[ZNF428]] | +0.60 | +0.62 / +0.47 | both halves | 2e-05 |  |
| [[XPA]] | +0.59 | +0.60 / +0.54 | both halves | 1e-05 |  |
| [[ELAPOR2]] | +0.59 | +0.60 / +0.55 | both halves | 1e-05 |  |
| [[PMPCB]] | +0.59 | +0.59 / +0.54 | both halves | 1e-05 |  |

## Genes that move opposite

*31 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[FBXW7]] | -0.65 | -0.60 / -0.62 | both halves | 7e-06 |  |
| [[PDCD6]] | -0.64 | -0.61 / -0.63 | both halves | 7e-06 |  |
| [[ARPC5L]] | -0.64 | -0.47 / -0.66 | both halves | 2e-05 |  |
| [[SLC35C1]] | -0.63 | -0.55 / -0.63 | both halves | 1e-05 |  |
| [[MAD1L1]] | -0.63 | -0.50 / -0.64 | both halves | 1e-05 |  |
| [[TRAPPC10]] | -0.63 | -0.58 / -0.58 | both halves | 8e-06 |  |
| [[SENP5]] | -0.60 | -0.52 / -0.59 | both halves | 1e-05 | STRING 406 |
| [[PGP]] | -0.59 | -0.55 / -0.58 | both halves | 1e-05 |  |
| [[SNTB2]] | -0.59 | -0.53 / -0.58 | both halves | 1e-05 |  |
| [[PAQR4]] | -0.58 | -0.54 / -0.59 | both halves | 1e-05 |  |
| [[LRRC8A]] | -0.58 | -0.48 / -0.61 | both halves | 2e-05 |  |
| [[FBH1]] | -0.57 | -0.47 / -0.55 | both halves | 2e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity raises KPNA5's level | compounds that target TOP2A: 3 of 5 lower it (Doxorubicin, Epirubicin, Idarubicin) | 60% of the class's compounds vs 2.0% of all compounds | 0.044 | ⚠ off-target possible; 3 compounds; artifact flags |
| [[HDAC6]] | B | HDAC6 activity raises KPNA5's level | compounds that target HDAC6: 2 of 2 lower it (Belinostat, Panobinostat) | 100% of the class's compounds vs 2.0% of all compounds | 0.095 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 017]] — Intraflagellar transport; 202 genes; this gene is in the **+** arm (projection on the module's main direction 0.532). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.28).
- **Nodal map** (x, y) = (-22.1, 2.6); signed map (9.0, -25.3). **Vector** length 124, 33.3% of its response variance represented; |z| ≥ 3 in 1,192 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM |  | +9.0 | +17.7 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +7.8 | +10.6 |
|  | [[Harringtonine (drug)]] 5 µM |  | +7.6 | +7.5 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~18% of this change | +6.4 | +6.9 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +5.5 | +6.5 |
|  | [[Ponatinib (drug)]] 5 µM |  | +4.4 | +2.9 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | +4.0 | +3.8 |
|  | [[Radotinib (drug)]] 5 µM |  | +3.6 | +2.5 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +3.1 | +2.1 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -9.8 | -20.6 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | -7.8 | -9.6 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | -6.9 | -9.8 |
|  | [[Auranofin (drug)]] 5 µM |  | -6.5 | -8.2 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -4.8 | -5.0 |
|  | [[vincristine (drug)]] 0.5 µM |  | -3.2 | -3.1 |
|  | [[Peretinoin (drug)]] 0.5 µM |  | -3.1 | -4.0 |
|  | [[vincristine (drug)]] 5 µM |  | -2.9 | -4.0 |

## What is on record

|  |  |
|---|---|
| Name | karyopherin subunit alpha 5 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 6q22.1 — chr6:116,681,187-116,741,867 (+) |
| Ensembl biotype | protein_coding |
| Also known as | SRP6, IPOA6 |
| Gene groups (HGNC) | Armadillo repeat containing; Importins |
| Reactome | 10 pathways, smallest: NS1 Mediated Effects on Host Pathways; Maturation of DENV proteins; ISG15 antiviral mechanism |
| Matched by | ensembl_id |

**Function**, from UniProt [O15131](https://www.uniprot.org/uniprotkb/O15131) (Importin subunit alpha-6):

> Functions in nuclear protein import as an adapter protein for nuclear receptor KPNB1. Binds specifically and directly to substrates containing either a simple or bipartite NLS motif. Docking of the importin/substrate complex to the nuclear pore complex (NPC) is mediated by KPNB1 through binding to nucleoporin FxFG repeats and the complex is subsequently translocated through the pore by an energy requiring, Ran-dependent mechanism. At the nucleoplasmic side of the NPC, Ran binds to importin-beta …

**Summary**, from NCBI Gene [3841](https://www.ncbi.nlm.nih.gov/gene/3841):

> The transport of molecules between the nucleus and the cytoplasm in eukaryotic cells is mediated by the nuclear pore complex (NPC) which consists of 60-100 proteins and is probably 120 million daltons in molecular size. Small molecules (up to 70 kD) can pass through the nuclear pore by nonselective diffusion; larger molecules are transported by an active process. Most nuclear proteins contain short basic amino acid sequences known as nuclear localization signals (NLSs). KPNA5 protein belongs to …

**Accessions** — [HGNC:6398](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:6398) · Entrez [3841](https://www.ncbi.nlm.nih.gov/gene/3841) · UniProt [O15131](https://www.uniprot.org/uniprotkb/O15131) · Ensembl [ENSG00000196911](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000196911)

## Data

Gene col 12300: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 12300); `tables/drug_effects.parquet` (39 rows, flagged included); `relations/gene_relations.parquet` (col_a == 12300, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 12300]; `tensor/DDL_lfc|DDL_z.npy` [12300]; `embed/gene_vectors.npy` [12300]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 12300 or target_col == 12300). Every well: [[KPNA5 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/KPNA5.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
