---
symbol: "CDKN3"
type: "gene"
col: 1980
ensembl_id: "ENSG00000100526"
name: "cyclin dependent kinase inhibitor 3"
location: "14q22.2"
module: 22
arm: "+"
pooled_cpm: 21.1
n_lines_expressing: 49
n_dd_up: 23
n_dd_down: 20
n_dd_up_clean: 11
n_dd_down_clean: 10
in_vector_space: true
direction_upstream: 9
direction_downstream: 0
tags: ["gene", "module/022"]
generated_by: "tahoemap"
---

# CDKN3

*cyclin dependent kinase inhibitor 3* — 14q22.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 23 drug-doses (12 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 2.11× (z +10.1, q 2e-21, up in 40 of 46 measured lines) ⚠ cell-cycle shift, would explain all of this change. The strongest without an alert is [[Belinostat (drug)]] 5 µM: 2.15× (z +7.4, q 2e-11, up in 37 of 46 measured lines).
> Pooled over the cell lines (median), lowered significantly by 20 drug-doses (10 with an alert ⚠); the strongest is [[Selinexor (drug)]] 0.5 µM: 0.449× (z -7.7, q 5e-12, down in 36 of 46 measured lines) ⚠ cell-cycle shift, explains ~84% of this change. The strongest without an alert is [[Anethole trithione (drug)]] 0.5 µM: 0.649× (z -4.2, q 0.002, down in 29 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CENPE]] (+0.92, fdr 7e-06), [[CKAP2]] (+0.92, fdr 7e-06), [[DLGAP5]] (+0.91, fdr 7e-06).
> It is in [[Module 022]], a single-armed module (G2/M checkpoint).
> Probable direction (from the cell lines, not proof of direct regulation): 9 arrows point to it, the strongest [[PIMREG]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 23 in all, 12 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 23 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 12 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1980.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | **2.11×** | +10.1 | 2e-21 | 40/46 (NCI-H2030, RKO, …) | rises with dose | composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~54% of this change | **2.73×** | +9.7 | 1e-19 | 30/39 (NCI-H460, PANC-1, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~46% of this change | **2.58×** | +8.8 | 3e-16 | 25/34 (NCI-H460, MIA PaCa-2, …) | all doses, stronger at high dose | composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~74% of this change | **2.26×** | +7.8 | 6e-13 | 35/43 (HOP62, SW 900, …) | all doses, flat | low cells (technical?) |
| [[Belinostat (drug)]] 5 µM |  | **2.15×** | +7.4 | 2e-11 | 37/46 (KATO III, SW480, …) | rises with dose | cell-cycle shift (explains ~19% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **2.14×** | +7.3 | 2e-11 | 36/47 (KATO III, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here) |
| [[Darinaparsin (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~68% of this change | **1.60×** | +6.4 | 1e-08 | 37/47 (NCI-H2347, CFPAC-1, …) | top dose only |  |
| [[Panobinostat (drug)]] 5 µM |  | **1.93×** | +6.3 | 2e-08 | 34/47 (KATO III, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~44% of this change | **1.91×** | +5.8 | 5e-07 | 25/37 (PANC-1, KATO III, …) | all doses, stronger at high dose | composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **1.45×** | +5.1 | 2e-05 | 25/47 (NCI-H2347, J82, …) | rises with dose |  |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | **1.69×** | +4.8 | 7e-05 | 28/47 (RKO, C32, …) | rises with dose | composition shift |
| [[Docetaxel (drug)]] 5 µM |  | **1.35×** | +4.1 | 0.002 | 22/47 (NCI-H2030, HT-29, …) | all doses, flat |  |
| [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | **2.20×** | +4.0 | 0.003 | 22/45 (J82, PANC-1, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~26% of this change | **1.51×** | +4.0 | 0.003 | 23/47 (SW480, KATO III, …) | all doses, stronger at high dose |  |
| [[Belinostat (drug)]] 0.5 µM |  | **1.45×** | +3.6 | 0.012 | 18/46 (LoVo, SW480, …) | rises with dose | cell-cycle shift (explains ~19% here) |
| [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | **1.38×** | +3.1 | 0.061 | 15/46 (SW 900, NCI-H23, …) | inconsistent across doses |  |
| [[Vinblastine (sulfate) (drug)]] 0.05 µM |  | **1.37×** | +3.0 | 0.077 | 13/47 (HOP62, NCI-H460, …) | inconsistent across doses |  |
| [[Mebendazole (drug)]] 0.5 µM |  | **1.37×** | +3.0 | 0.077 | 14/46 (HT-29, H4, …) | rises with dose | position effect removed |
| [[Peretinoin (drug)]] 5 µM |  | **1.38×** | +3.0 | 0.080 | 15/46 (HOP62, NCI-H460, …) | all doses, flat |  |
| [[Sodium Salicylate (drug)]] 5 µM |  | **1.24×** | +2.9 | 0.083 | 11/47 (NCI-H2030, PANC-1, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 20 in all, 10 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 20 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 10 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 1980.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~84% of this change | **0.449×** | -7.7 | 5e-12 | 36/46 (A-427, C32, …) | all doses, stronger at high dose |  |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | **0.582×** | -7.4 | 4e-11 | 35/47 (A-427, A498, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Selinexor (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~64% of this change | **0.560×** | -5.6 | 4e-06 | 37/47 (PANC-1, Hs 766T, …) | all doses, stronger at high dose |  |
| [[Cytarabine (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~67% of this change | **0.604×** | -4.9 | 2e-04 | 24/46 (A549, PANC-1, …) | all doses, flat |  |
| [[Cytarabine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~72% of this change | **0.597×** | -4.8 | 2e-04 | 31/46 (PANC-1, A549, …) | all doses, stronger at high dose |  |
| [[Anethole trithione (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~69% of this change | **0.719×** | -4.5 | 6e-04 | 33/47 (J82, HepG2/C3A, …) | all doses, stronger at high dose | position effect removed |
| [[Anethole trithione (drug)]] 0.5 µM |  | **0.649×** | -4.2 | 0.002 | 29/47 (SW 1088, NCI-H2030, …) | all doses, stronger at high dose | position effect removed |
| [[Cytarabine (hydrochloride) (drug)]] 0.05 µM |  | **0.659×** | -3.7 | 0.012 | 21/46 (NCI-H2030, PANC-1, …) | all doses, flat |  |
| [[Pyridoxine (hydrochloride) (drug)]] 5 µM |  | **0.762×** | -3.7 | 0.012 | 18/47 (HS-578T, J82, …) | all doses, stronger at high dose | position effect removed |
| [[Cytarabine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~73% of this change | **0.686×** | -3.6 | 0.015 | 21/47 (PANC-1, A549, …) | all doses, stronger at high dose |  |
| [[PF-06260933 (drug)]] 5 µM |  | **0.488×** | -3.6 | 0.015 | 20/45 (HCT15, RPMI-7951, …) | top dose only | noisy plate (z scaled) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~93% of this change | **0.705×** | -3.4 | 0.033 | 20/45 (SW48, SNU-1, …) | inconsistent across doses |  |
| [[Amsacrine (drug)]] 5 µM |  | **0.787×** | -3.3 | 0.045 | 18/47 (A498, LS 180, …) | top dose only |  |
| [[EX229 (drug)]] 5 µM |  | **0.541×** | -3.1 | 0.076 | 18/45 (LoVo, NCI-H1573, …) | top dose only | noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | **0.731×** | -3.0 | 0.090 | 16/46 (HEC-1-A, J82, …) | top dose only |  |
| [[Gemcitabine (drug)]] 0.05 µM |  | **0.789×** | -3.0 | 0.090 | 16/47 (LOX-IMVI, PANC-1, …) | inconsistent across doses |  |
| [[Anethole trithione (drug)]] 0.05 µM |  | **0.737×** | -3.0 | 0.097 | 12/47 (CFPAC-1, J82, …) | all doses, stronger at high dose | position effect removed |
| [[Cytarabine (drug)]] 0.05 µM |  | **0.720×** | -2.9 | 0.098 | 16/46 (CHP-212, NCI-H1573, …) | all doses, stronger at high dose |  |
| [[Sapanisertib (drug)]] 5 µM |  | **0.561×** | -2.9 | 0.098 | 9/47 (MIA PaCa-2, SNU-1, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.12 per unit of S-phase module lfc, +1.31 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1980. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-427 (line)]] | wt | 43.9 | 0 | 3 (2 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.0993× (z -21.0) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[TAK-901 (drug)]] 0.05 µM 0.233× (z -8.7) |
| [[LOX-IMVI (line)]] | wt | 15.6 | 0 | 3 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 0.5 µM 0.0303× (z -15.6) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Amsacrine (drug)]] 0.5 µM 0.135× (z -8.9) |
| [[NCI-H460 (line)]] | wt | 17.0 | 2 (2 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 5 µM 6.62× (z +10.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~46% of this change | [[Selinexor (drug)]] 5 µM 0.336× (z -9.0) ⚠ cell-cycle shift, would explain all of this change |
| [[SNU-1 (line)]] | wt | 26.6 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 0.05 µM 0.0487× (z -11.8) |
| [[A498 (line)]] | wt | 17.0 | 0 | 2 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.136× (z -16.5) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Amsacrine (drug)]] 5 µM 0.341× (z -8.9) |
| [[LS 180 (line)]] | wt | 20.9 | 0 | 2 (2 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.226× (z -9.5) ⚠ cell-cycle shift, would explain all of this change |
| [[MIA PaCa-2 (line)]] | alt | 24.5 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 5.20× (z +8.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~54% of this change | [[Lidocaine (hydrochloride) (drug)]] 0.05 µM 0.204× (z -8.5) |
| [[A-172 (line)]] | wt | 13.6 | 0 | 1 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.230× (z -10.1) ⚠ cell-cycle shift, would explain all of this change |
| [[C32 (line)]] | wt | 19.2 | 0 | 1 (1 ⚠) | — | [[Selinexor (drug)]] 0.5 µM 0.0998× (z -11.0) ⚠ cell-cycle shift, explains ~84% of this change |
| [[CFPAC-1 (line)]] | alt | 15.0 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.55× (z +9.1) ⚠ cell-cycle shift, would explain all of this change | — |
| [[HOP62 (line)]] | alt | 27.4 | 1 (1 ⚠) | 0 | [[Docetaxel (drug)]] 0.05 µM 4.47× (z +8.6) ⚠ transcription drop; cell-cycle shift, explains ~74% of this change | — |
| [[KATO III (line)]] | alt | 16.8 | 1 | 0 | [[Belinostat (drug)]] 5 µM 5.43× (z +8.8) | — |
| [[NCI-H1573 (line)]] | alt | 10.6 | 0 | 1 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.247× (z -8.9) ⚠ cell-cycle shift, would explain all of this change |
| [[NCI-H1792 (line)]] | alt | 8.86 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 10.4× (z +8.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~54% of this change | — |
| [[NCI-H2030 (line)]] | alt | 38.1 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.33× (z +13.6) ⚠ cell-cycle shift, would explain all of this change | — |
| [[NCI-H23 (line)]] | alt | 27.1 | 0 | 1 (1 ⚠) | — | [[Selinexor (drug)]] 0.5 µM 0.218× (z -9.1) ⚠ cell-cycle shift, explains ~84% of this change |
| [[NCI-H2347 (line)]] | alt | 26.9 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.75× (z +9.2) ⚠ cell-cycle shift, would explain all of this change | — |
| [[Panc 03.27 (line)]] | alt | 23.8 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.86× (z +12.4) ⚠ cell-cycle shift, would explain all of this change | — |
| [[PANC-1 (line)]] | alt | 16.8 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.13× (z +9.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~54% of this change | — |
| [[RKO (line)]] | wt | 11.7 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 8.12× (z +12.9) ⚠ cell-cycle shift, would explain all of this change | — |
| [[RPMI-7951 (line)]] | alt | 18.8 | 0 | 1 | — | [[Temsirolimus (drug)]] 0.5 µM 0.0937× (z -9.4) |
| [[SK-MEL-2 (line)]] | alt | 27.9 | 0 | 1 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.210× (z -12.1) ⚠ cell-cycle shift, would explain all of this change |
| [[SW 900 (line)]] | alt | 25.1 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.64× (z +8.7) ⚠ cell-cycle shift, would explain all of this change | — |
| [[SW48 (line)]] | wt | 35.4 | 0 | 1 (1 ⚠) | — | [[Mitoxantrone (dihydrochloride) (drug)]] 0.5 µM 0.0462× (z -13.8) ⚠ cell-cycle shift, explains ~93% of this change |
| [[SW480 (line)]] | alt | 29.8 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.85× (z +9.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~54% of this change | — |
| [[A549 (line)]] | wt | 24.1 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 36.4 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 5.00 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 18.4 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 19.9 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 9.80 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 7.45 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 24.1 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 21.5 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 32.2 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 5.58 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 11.2 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 13.6 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 16.8 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 9.34 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 27.6 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 15.9 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 9.94 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 14.1 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 32.1 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 34.7 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 15.7 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 13.6 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 36.6 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 28.5 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1980), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CENPE]] | +0.92 | +0.90 / +0.90 | both halves | 7e-06 | pathway: HALLMARK_E2F_TARGETS; STRING 808 |
| [[CKAP2]] | +0.92 | +0.91 / +0.90 | both halves | 7e-06 | STRING 446 |
| [[DLGAP5]] | +0.91 | +0.86 / +0.90 | both halves | 7e-06 | pathway: HALLMARK_E2F_TARGETS; STRING 962 |
| [[CCNB2]] | +0.89 | +0.87 / +0.89 | both halves | 7e-06 | pathway: HALLMARK_E2F_TARGETS; STRING 893 |
| [[NEK2]] | +0.89 | +0.84 / +0.87 | both halves | 7e-06 | pathway: HALLMARK_G2M_CHECKPOINT; STRING 722 |
| [[CENPF]] | +0.88 | +0.87 / +0.87 | both halves | 7e-06 | pathway: HALLMARK_G2M_CHECKPOINT; STRING 725 |
| [[CCNB1]] | +0.88 | +0.89 / +0.87 | both halves | 7e-06 | STRING 941 |
| [[TOP2A]] | +0.88 | +0.85 / +0.87 | both halves | 7e-06 | pathway: HALLMARK_E2F_TARGETS; STRING 863 |
| [[PTTG1]] | +0.88 | +0.83 / +0.88 | both halves | 7e-06 | pathway: HALLMARK_E2F_TARGETS; STRING 840 |
| [[CDC20]] | +0.87 | +0.84 / +0.86 | both halves | 7e-06 | pathway: HALLMARK_E2F_TARGETS; STRING 885 |
| [[BUB1]] | +0.87 | +0.81 / +0.86 | both halves | 7e-06 | pathway: HALLMARK_G2M_CHECKPOINT; STRING 846 |
| [[KIF4A]] | +0.87 | +0.86 / +0.82 | both halves | 7e-06 | pathway: HALLMARK_E2F_TARGETS; STRING 803 |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*9 arrows, 9 of them with an alert ⚠; grade A 0, B 2, C 7.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PIMREG]] | B | PIMREG activity raises CDKN3's level | lines that do not express PIMREG (6) vs lines expressing it (44) | 2.37× lower at baseline in the lines without PIMREG | 0.003 | ⚠ within organs, on part of the lines; also absent: PBK, AURKB, ENSG00000197332; maybe low, not absent |
| [[NEURL1B]] | B | NEURL1B activity raises CDKN3's level | lines that do not express NEURL1B (7) vs lines expressing it (43) | 2.17× lower at baseline in the lines without NEURL1B | 0.012 | ⚠ within organs, on part of the lines; also absent: PIMREG, WNT9A, ENSG00000267131 |
| [[AURKB]] | C | AURKB activity raises CDKN3's level | lines that do not express AURKB (4) vs lines expressing it (46) | 2.61× lower at baseline in the lines without AURKB | 0.014 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: TCF19, SMARCD3, CDC45; maybe low, not absent |
| [[PBK]] | C | PBK activity raises CDKN3's level | lines that do not express PBK (4) vs lines expressing it (46) | 2.72× lower at baseline in the lines without PBK | 0.016 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: SPDL1, SMARCD3, NCS1; maybe low, not absent |
| [[NDC80]] | C | NDC80 activity raises CDKN3's level | lines that do not express NDC80 (3) vs lines expressing it (47) | 2.43× lower at baseline in the lines without NDC80 | 0.023 | ⚠ few lines (3 vs 47); across organs; also absent: SH3BP5, DSCC1, KLF9; maybe low, not absent |
| [[CDC20]] | C | CDC20 activity raises CDKN3's level | lines that do not express CDC20 (3) vs lines expressing it (47) | 2.56× lower at baseline in the lines without CDC20 | 0.060 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: SPDL1, ARHGAP10, CDC45; maybe low, not absent; its own permutation p |
| [[SAPCD2]] | C | SAPCD2 activity raises CDKN3's level | lines that do not express SAPCD2 (3) vs lines expressing it (47) | 2.46× lower at baseline in the lines without SAPCD2 | 0.060 | ⚠ few lines (3 vs 47); within organs, on part of the lines; co-absent genes; also absent: TLCD3B, CDC25A, DBNDD1; maybe low, not absent; its own permutation p |
| [[ACBD7]] | C | ACBD7 activity raises CDKN3's level | lines that do not express ACBD7 (4) vs lines expressing it (46) | 1.73× lower at baseline in the lines without ACBD7 | 0.062 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: ENSG00000197332, LRP3, PHGDH; maybe low, not absent |
| [[CDCA3]], [[SPDL1]] | C | CDCA3, SPDL1 activity raises CDKN3's level | lines that do not express CDCA3, SPDL1 (3) vs lines expressing them (47) | 3.05× lower at baseline in the lines without CDCA3, SPDL1 | 0.079 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: TBC1D19, PBK, SNPH; maybe low, not absent; its own permutation p; co-absent genes |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 022]] — G2/M checkpoint; 185 genes; every member is in the + arm (projection on the module's main direction 0.897). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.26; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-37.3, -57.2); signed map (-50.9, -42.7). **Vector** length 122, 40.2% of its response variance represented; |z| ≥ 3 in 1,107 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *Mitotic Prometaphase* (reactome, mean cos +0.68 to 48); *Mitotic Metaphase and Anaphase* (reactome, mean cos +0.70 to 41); *Mitotic Anaphase* (reactome, mean cos +0.71 to 40).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | +8.0 | +10.1 |
|  | [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~74% of this change | +4.8 | +7.8 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +4.4 | +5.1 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | +4.4 | +4.8 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~26% of this change | +3.8 | +4.0 |
|  | [[Docetaxel (drug)]] 5 µM |  | +2.7 | +4.1 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | +2.6 | +2.8 |
|  | [[Peretinoin (drug)]] 5 µM |  | +2.5 | +3.0 |
|  | [[HI-TOPK-032 (drug)]] 0.05 µM |  | +2.5 | +2.4 |
| fall | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | -7.5 | -7.4 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~84% of this change | -7.4 | -7.7 |
|  | [[Selinexor (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~64% of this change | -4.9 | -5.6 |
|  | [[Auranofin (drug)]] 5 µM |  | -4.1 | -2.3 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift | -4.1 | -2.3 |
|  | [[Amsacrine (drug)]] 5 µM |  | -3.6 | -3.3 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -3.5 | -0.9 |
|  | [[Cytarabine (hydrochloride) (drug)]] 0.05 µM |  | -3.2 | -3.7 |
|  | [[EX229 (drug)]] 5 µM |  | -3.0 | -3.1 |

## What is on record

|  |  |
|---|---|
| Name | cyclin dependent kinase inhibitor 3 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 14q22.2 — chr14:54,396,849-54,420,218 (+) |
| Ensembl biotype | protein_coding |
| Also known as | KAP, CDI1 |
| Gene groups (HGNC) | CDC14 phosphatases |
| Hallmark sets | SPERMATOGENESIS, G2M_CHECKPOINT, E2F_TARGETS |
| Matched by | ensembl_id |

**Function**, from UniProt [Q16667](https://www.uniprot.org/uniprotkb/Q16667) (Cyclin-dependent kinase inhibitor 3):

> May play a role in cell cycle regulation. Dual specificity CC phosphatase active toward substrates containing either phosphotyrosine or phosphoserine residues. Dephosphorylates CDK2 at 'Thr-160' in a cyclin-dependent manner.

**Summary**, from NCBI Gene [1033](https://www.ncbi.nlm.nih.gov/gene/1033):

> The protein encoded by this gene belongs to the dual specificity protein phosphatase family. It was identified as a cyclin-dependent kinase inhibitor, and has been shown to interact with, and dephosphorylate CDK2 kinase, thus prevent the activation of CDK2 kinase. This gene was reported to be deleted, mutated, or overexpressed in several kinds of cancers. Alternatively spliced transcript variants encoding different isoforms have been found for this gene. [provided by RefSeq, Aug 2008]

**Accessions** — [HGNC:1791](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:1791) · Entrez [1033](https://www.ncbi.nlm.nih.gov/gene/1033) · UniProt [Q16667](https://www.uniprot.org/uniprotkb/Q16667) · Ensembl [ENSG00000100526](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000100526)

## Data

Gene col 1980: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1980); `tables/drug_effects.parquet` (43 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1980, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1980]; `tensor/DDL_lfc|DDL_z.npy` [1980]; `embed/gene_vectors.npy` [1980]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1980 or target_col == 1980). Every well: [[CDKN3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CDKN3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
