---
symbol: "RFX3-DT"
type: "gene"
col: 13836
ensembl_id: "ENSG00000232104"
name: "RFX3 divergent transcript"
location: "9p24.2"
module: 23
arm: "+"
pooled_cpm: 27.33
n_lines_expressing: 47
n_dd_up: 14
n_dd_down: 22
n_dd_up_clean: 13
n_dd_down_clean: 13
in_vector_space: true
direction_upstream: 4
direction_downstream: 16
tags: ["gene", "module/023"]
generated_by: "tahoemap"
---

# RFX3-DT

*RFX3 divergent transcript* — 9p24.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 14 drug-doses (1 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 2.57× (z +15.6, q 0e+00, up in 36 of 44 measured lines).
> Pooled over the cell lines (median), lowered significantly by 22 drug-doses (9 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 0.5 µM: 0.469× (z -8.8, q 7e-16, down in 34 of 45 measured lines) ⚠ cell-cycle shift, explains ~31% of this change. The strongest without an alert is [[Ixazomib citrate (drug)]] 5 µM: 0.504× (z -8.0, q 3e-13, down in 34 of 44 measured lines).
> Its strongest partners by |cos| (97 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 3 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[WARS2-AS1]] (+0.87, fdr 1e-05), [[ANKRD17-DT]] (+0.85, fdr 1e-05), [[CHD1-DT]] (+0.85, fdr 7e-06); moves opposite to [[MAST3]] (-0.73, fdr 1e-04), [[ANKRD27]] (-0.71, fdr 9e-04, ⚠ one half only (not replicated)), [[SLC27A1]] (-0.71, fdr 4e-04), [[WASF3]] (-0.69, fdr 1e-04).
> It sits in the **+** arm of [[Module 023]].
> Probable direction (from the cell lines, not proof of direct regulation): 4 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); 16 go from it, the strongest it → [[C12orf60]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 1 with an alert ⚠. 14 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 13836.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **2.57×** | +15.6 | 0e+00 | 36/44 (NCI-H460, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.75×** | +9.2 | 9e-18 | 30/43 (Panc 03.27, CFPAC-1, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.12×** | +8.8 | 4e-16 | 36/43 (LoVo, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.85×** | +6.9 | 7e-10 | 29/43 (HS-578T, MIA PaCa-2, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.54×** | +5.0 | 6e-05 | 31/45 (NCI-H460, LoVo, …) | all doses, stronger at high dose |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.33×** | +4.7 | 2e-04 | 22/45 (A-172, NCI-H460, …) | rises with dose |  |
| [[Ponatinib (drug)]] 5 µM |  | **1.49×** | +4.6 | 3e-04 | 26/45 (LoVo, KATO III, …) | rises with dose |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.50×** | +4.6 | 3e-04 | 24/45 (HT-29, MIA PaCa-2, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~75% of this change | **1.31×** | +4.4 | 6e-04 | 22/45 (J82, A549, …) | top dose only | low cells (technical?) |
| [[Auranofin (drug)]] 5 µM |  | **1.41×** | +4.0 | 0.003 | 23/44 (HT-29, C32, …) | top dose only |  |
| [[Cobimetinib (drug)]] 5 µM |  | **1.41×** | +3.8 | 0.006 | 18/43 (SW480, RKO, …) | rises with dose |  |
| [[Bimiralisib (drug)]] 5 µM |  | **1.74×** | +3.4 | 0.036 | 13/44 (RPMI-7951, SW480, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Dihydroartemisinin (drug)]] 0.05 µM |  | **1.35×** | +3.1 | 0.076 | 15/44 (HOP62, PANC-1, …) | inconsistent across doses |  |
| [[5-Azacytidine (drug)]] 5 µM |  | **1.30×** | +3.0 | 0.097 | 13/44 (NCI-H1573, C-33 A, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 22 in all, 9 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 22 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 13836.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **0.469×** | -8.8 | 7e-16 | 34/45 (H4, SW480, …) | all doses, stronger at high dose |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~35% of this change | **0.479×** | -8.6 | 3e-15 | 33/44 (LoVo, SW480, …) | all doses, stronger at high dose |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.504×** | -8.0 | 3e-13 | 34/44 (PANC-1, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **0.515×** | -7.7 | 1e-12 | 35/42 (SW 900, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~42% of this change | **0.526×** | -7.5 | 9e-12 | 31/45 (SW480, LoVo, …) | all doses, stronger at high dose |  |
| [[PH-797804 (drug)]] 5 µM |  | **0.316×** | -7.0 | 2e-10 | 29/42 (NCI-H1573, KATO III, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.554×** | -6.9 | 5e-10 | 29/45 (SW480, PANC-1, …) | rises with dose |  |
| [[TAK-901 (drug)]] 5 µM |  | **0.344×** | -6.5 | 6e-09 | 31/45 (NCI-H1573, LS 180, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~18% here); composition shift; noisy plate (z scaled) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~34% of this change | **0.562×** | -6.5 | 6e-09 | 27/42 (HepG2/C3A, PANC-1, …) | rises with dose |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~55% of this change | **0.609×** | -5.8 | 4e-07 | 25/43 (PANC-1, H4, …) | rises with dose |  |
| [[NG25 (drug)]] 5 µM |  | **0.505×** | -4.2 | 0.002 | 25/42 (NCI-H1573, H4, …) | top dose only | cell-cycle shift (explains ~23% here); noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~83% of this change | **0.716×** | -3.9 | 0.005 | 17/45 (PANC-1, KATO III, …) | rises with dose | composition shift |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.707×** | -3.8 | 0.006 | 24/45 (PANC-1, HCT15, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Niclosamide (olamine) (drug)]] 0.5 µM |  | **0.722×** | -3.8 | 0.006 | 20/45 (AN3 CA, NCI-H1573, …) | rises with dose |  |
| [[S-Adenosyl-L-methionine (disulfate tosylate) (drug)]] 0.05 µM |  | **0.726×** | -3.7 | 0.008 | 20/45 (A-172, HEC-1-A, …) | all doses, flat |  |
| [[Bortezomib (drug)]] 0.5 µM |  | **0.682×** | -3.2 | 0.049 | 15/45 (PANC-1, NCI-H23, …) | all doses, flat | noisy plate (z scaled) |
| [[S-Adenosyl-L-methionine (disulfate tosylate) (drug)]] 5 µM |  | **0.828×** | -3.1 | 0.058 | 11/45 (HCT15, HOP62, …) | all doses, flat |  |
| [[Radotinib (drug)]] 5 µM |  | **0.831×** | -3.1 | 0.063 | 16/45 (SW480, NCI-H1573, …) | top dose only |  |
| [[Ranolazine (drug)]] 0.5 µM |  | **0.776×** | -3.0 | 0.081 | 12/45 (AN3 CA, J82, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.37 per unit of S-phase module lfc, -0.29 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 13836. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 24.1 | 1 | 9 (6 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.20× (z +12.7) | [[Digitoxin (drug)]] 5 µM 0.196× (z -12.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~55% of this change · without an alert: [[Ixazomib citrate (drug)]] 5 µM 0.213× (z -12.0) |
| [[NCI-H1573 (line)]] | alt | 56.7 | 2 | 7 (6 ⚠) | [[Homoharringtonine (drug)]] 5 µM 5.00× (z +20.7) | [[Dinaciclib (drug)]] 5 µM 0.195× (z -14.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change · without an alert: [[PH-797804 (drug)]] 5 µM 0.126× (z -9.8) |
| [[LoVo (line)]] | wt | 40.0 | 3 (1 ⚠) | 5 (4 ⚠) | [[Homoharringtonine (drug)]] 5 µM 6.33× (z +21.1) | [[Belinostat (drug)]] 5 µM 0.175× (z -14.1) ⚠ cell-cycle shift, explains ~35% of this change · without an alert: [[Ixazomib citrate (drug)]] 5 µM 0.352× (z -8.5) |
| [[SW480 (line)]] | alt | 35.2 | 1 | 5 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.70× (z +12.3) | [[Belinostat (drug)]] 5 µM 0.217× (z -13.3) ⚠ cell-cycle shift, explains ~35% of this change · without an alert: [[Ixazomib citrate (drug)]] 0.5 µM 0.270× (z -11.4) |
| [[H4 (line)]] | wt | 40.7 | 0 | 4 (4 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.105× (z -11.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~55% of this change |
| [[C32 (line)]] | wt | 7.62 | 1 | 2 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 9.44× (z +12.8) | [[Sunitinib (drug)]] 5 µM 0.0748× (z -10.4) ⚠ toxic · without an alert: [[Lidocaine (hydrochloride) (drug)]] 0.05 µM 0.120× (z -8.5) |
| [[KATO III (line)]] | alt | 54.9 | 0 | 3 (3 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.265× (z -11.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~55% of this change |
| [[NCI-H460 (line)]] | wt | 19.0 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 8.00× (z +22.1) | — |
| [[HCT15 (line)]] | alt | 35.1 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 7.72× (z +14.4) | [[Panobinostat (drug)]] 0.5 µM 0.161× (z -9.0) ⚠ cell-cycle shift, explains ~31% of this change |
| [[HepG2_C3A (line)]] | wt | 30.1 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.40× (z +9.2) | [[Niclosamide (olamine) (drug)]] 5 µM 0.0793× (z -13.0) ⚠ toxic; cell-cycle shift, explains ~34% of this change |
| [[HOP62 (line)]] | alt | 53.8 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.56× (z +9.2) | [[Digitoxin (drug)]] 5 µM 0.249× (z -9.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~55% of this change |
| [[HS-578T (line)]] | alt | 14.0 | 2 | 0 | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 8.33× (z +9.8) | — |
| [[J82 (line)]] | alt | 12.0 | 2 (1 ⚠) | 0 | [[Selinexor (drug)]] 5 µM 3.62× (z +9.8) ⚠ cell-cycle shift, explains ~75% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 3.42× (z +9.3) | — |
| [[LOX-IMVI (line)]] | wt | 43.8 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.01× (z +10.2) | [[Panobinostat (drug)]] 0.5 µM 0.203× (z -10.4) ⚠ cell-cycle shift, explains ~31% of this change |
| [[RKO (line)]] | wt | 50.4 | 0 | 2 (2 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.278× (z -9.0) ⚠ cell-cycle shift, explains ~31% of this change |
| [[SW48 (line)]] | wt | 30.3 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.08× (z +8.5) | [[Digitoxin (drug)]] 5 µM 0.0912× (z -10.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~55% of this change |
| [[C-33 A (line)]] | alt | 21.3 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.27× (z +10.9) | — |
| [[CFPAC-1 (line)]] | alt | 8.26 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.95× (z +9.0) | — |
| [[HT-29 (line)]] | alt | 14.2 | 1 | 0 | [[Auranofin (drug)]] 5 µM 5.37× (z +9.8) | — |
| [[hTERT-HPNE (line)]] | wt | 17.3 | 0 | 1 (1 ⚠) | — | [[Docetaxel (drug)]] 0.05 µM 0.125× (z -9.3) ⚠ transcription drop; cell-cycle shift, explains ~75% of this change |
| [[MIA PaCa-2 (line)]] | alt | 21.3 | 0 | 1 (1 ⚠) | — | [[Belinostat (drug)]] 5 µM 0.216× (z -8.7) ⚠ cell-cycle shift, explains ~35% of this change |
| [[NCI-H2030 (line)]] | alt | 18.4 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 8.15× (z +14.3) | — |
| [[Panc 03.27 (line)]] | alt | 11.9 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.99× (z +9.7) | — |
| [[RPMI-7951 (line)]] | alt | 37.5 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.13× (z +9.9) | — |
| [[SHP-77 (line)]] | alt | 42.0 | 0 | 1 | — | [[Belinostat (drug)]] 0.5 µM 0.258× (z -8.5) |
| [[SK-MEL-2 (line)]] | alt | 85.6 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.432× (z -8.6) |
| [[SNU-1 (line)]] | wt | 16.1 | 0 | 1 (1 ⚠) | — | [[Belinostat (drug)]] 5 µM 0.129× (z -8.8) ⚠ cell-cycle shift, explains ~35% of this change |
| [[SW 900 (line)]] | alt | 22.4 | 0 | 1 | — | [[Belinostat (drug)]] 0.5 µM 0.116× (z -11.4) |
| [[SW1417 (line)]] | alt | 12.8 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.52× (z +9.0) | — |
| [[A-172 (line)]] | wt | 31.5 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 10.0 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 41.9 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 18.8 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 36.9 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 5.65 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 6.08 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 21.3 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 51.9 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 32.5 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 12.5 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 46.8 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 8.76 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 27.8 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 12.5 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 3.95 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 28.8 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 12.8 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 25.0 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 20.2 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 16.8 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 13836), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*96 of its nearest partners move with it, 2 of them with an alert (⚠; 2 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[WARS2-AS1]] | +0.87 | +0.87 / +0.52 | both halves | 1e-05 |  |
| [[ANKRD17-DT]] | +0.85 | +0.90 / +0.56 | both halves | 1e-05 | same gene group |
| [[CHD1-DT]] | +0.85 | +0.87 / +0.62 | both halves | 7e-06 | same gene group |
| [[MAD2L1-DT]] | +0.84 | +0.81 / +0.57 | both halves | 1e-05 | same gene group |
| [[PPP1R12A-AS2]] | +0.82 | +0.85 / +0.45 | both halves | 3e-05 |  |
| [[HEXIM2-AS1]] | +0.82 | +0.81 / +0.54 | both halves | 1e-05 |  |
| [[RAB30-DT]] | +0.81 | +0.84 / +0.54 | both halves | 1e-05 | same gene group |
| [[PCNX4-DT]] | +0.81 | +0.81 / +0.45 | both halves | 3e-05 | same gene group |
| [[ST7L]] | +0.81 | +0.83 / +0.49 | both halves | 1e-05 |  |
| [[OXA1L-DT]] | +0.81 | +0.83 / +0.47 | both halves | 2e-05 | same gene group |
| [[UFL1-AS1]] | +0.81 | +0.77 / +0.55 | both halves | 1e-05 |  |
| [[PPP1R3F]] | +0.81 | +0.79 / +0.52 | both halves | 1e-05 |  |

## Genes that move opposite

*4 of its nearest partners move opposite, 1 of them with an alert (⚠; 1 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MAST3]] | -0.73 | -0.63 / -0.33 | both halves | 1e-04 |  |
| [[ANKRD27]] | -0.71 | -0.71 / -0.18 | ⚠ one half (not replicated) | 9e-04 |  |
| [[SLC27A1]] | -0.71 | -0.67 / -0.25 | both halves | 4e-04 |  |
| [[WASF3]] | -0.69 | -0.69 / -0.33 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 3, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers RFX3-DT's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 3.4% of all compounds | 0.015 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[FSIP2-AS1]] | B | FSIP2-AS1 activity raises RFX3-DT's level | lines that do not express FSIP2-AS1 (6) vs lines expressing it (44) | 2.10× lower at baseline in the lines without FSIP2-AS1 | 0.021 | ⚠ within organs, on part of the lines; also absent: PMFBP1, SPATA17, ENSG00000287621; maybe low, not absent |
| [[CBX2]] | B | CBX2 activity raises RFX3-DT's level | lines that do not express CBX2 (6) vs lines expressing it (44) | 2.31× lower at baseline in the lines without CBX2 | 0.035 | ⚠ within organs, on part of the lines; also absent: CCNP, CTXN1, ADGRL1; maybe low, not absent |
| [[WARS2-AS1]] | C | WARS2-AS1 activity raises RFX3-DT's level | lines that do not express WARS2-AS1 (3) vs lines expressing it (47) | 2.39× lower at baseline in the lines without WARS2-AS1 | 0.089 | ⚠ few lines (3 vs 47); within organs, on part of the lines; co-absent genes; also absent: WWOX, MPP4, CDHR3; maybe low, not absent; co-absent with the target; its own permutation p |

### Downstream of this gene

*16 arrows, 16 of them with an alert ⚠; grade A 0, B 0, C 16. Shown: the 12 strongest; 4 more arrows (4 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[C12orf60]] | C | RFX3-DT activity raises C12orf60's level | lines that do not express RFX3-DT (3) vs lines expressing it (47) | 2.34× lower at baseline in the lines without RFX3-DT | 0.060 | ⚠ few lines (3 vs 47); within organs, on part of the lines; co-absent genes; also absent: POGLUT2, ANAPC1P4, WDR35; maybe low, not absent; its own permutation p |
| [[CARF]] | C | [[CCDC171]], RFX3-DT activity raises CARF's level | lines that do not express CCDC171, RFX3-DT (3) vs lines expressing them (47) | 2.33× lower at baseline in the lines without CCDC171, RFX3-DT | 0.060 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: POGLUT2, ANAPC1P4, WDR35; maybe low, not absent; its own permutation p; co-absent genes |
| [[DARS1-AS1]] | C | RFX3-DT activity raises DARS1-AS1's level | lines that do not express RFX3-DT (3) vs lines expressing it (47) | 1.98× lower at baseline in the lines without RFX3-DT | 0.060 | ⚠ few lines (3 vs 47); within organs, on part of the lines; co-absent genes; also absent: POGLUT2, ANAPC1P4, WDR35; maybe low, not absent; its own permutation p |
| [[SYNGR1]] | C | RFX3-DT activity raises SYNGR1's level | lines that do not express RFX3-DT (3) vs lines expressing it (47) | 1.97× lower at baseline in the lines without RFX3-DT | 0.060 | ⚠ few lines (3 vs 47); within organs, on part of the lines; co-absent genes; also absent: POGLUT2, ANAPC1P4, WDR35; maybe low, not absent; its own permutation p |
| [[AHI1-DT]] | C | RFX3-DT activity raises AHI1-DT's level | lines that do not express RFX3-DT (3) vs lines expressing it (47) | 1.80× lower at baseline in the lines without RFX3-DT | 0.060 | ⚠ few lines (3 vs 47); within organs, on part of the lines; co-absent genes; also absent: POGLUT2, ANAPC1P4, WDR35; maybe low, not absent; its own permutation p |
| [[SLC25A11]] | C | RFX3-DT activity raises SLC25A11's level | lines that do not express RFX3-DT (3) vs lines expressing it (47) | 1.68× lower at baseline in the lines without RFX3-DT | 0.060 | ⚠ few lines (3 vs 47); within organs, on part of the lines; co-absent genes; also absent: POGLUT2, ANAPC1P4, WDR35; maybe low, not absent; its own permutation p |
| [[PCNX4-DT]] | C | RFX3-DT activity raises PCNX4-DT's level | lines that do not express RFX3-DT (3) vs lines expressing it (47) | 1.64× lower at baseline in the lines without RFX3-DT | 0.067 | ⚠ few lines (3 vs 47); within organs, on part of the lines; co-absent genes; also absent: POGLUT2, ANAPC1P4, WDR35; maybe low, not absent |
| [[ITFG2-AS1]] | C | RFX3-DT activity raises ITFG2-AS1's level | lines that do not express RFX3-DT (3) vs lines expressing it (47) | 2.15× lower at baseline in the lines without RFX3-DT | 0.072 | ⚠ few lines (3 vs 47); within organs, on part of the lines; co-absent genes; also absent: POGLUT2, ANAPC1P4, WDR35; maybe low, not absent |
| [[EPM2A-DT]] | C | RFX3-DT activity raises EPM2A-DT's level | lines that do not express RFX3-DT (3) vs lines expressing it (47) | 2.14× lower at baseline in the lines without RFX3-DT | 0.072 | ⚠ few lines (3 vs 47); within organs, on part of the lines; co-absent genes; also absent: POGLUT2, ANAPC1P4, WDR35; maybe low, not absent |
| [[APLF]] | C | RFX3-DT activity raises APLF's level | lines that do not express RFX3-DT (3) vs lines expressing it (47) | 2.35× lower at baseline in the lines without RFX3-DT | 0.074 | ⚠ few lines (3 vs 47); within organs, on part of the lines; co-absent genes; also absent: POGLUT2, ANAPC1P4, WDR35; maybe low, not absent |
| [[ARRB2]] | C | RFX3-DT activity raises ARRB2's level | lines that do not express RFX3-DT (3) vs lines expressing it (47) | 2.56× lower at baseline in the lines without RFX3-DT | 0.077 | ⚠ few lines (3 vs 47); within organs, on part of the lines; co-absent genes; also absent: POGLUT2, ANAPC1P4, WDR35; maybe low, not absent |
| [[DNAH12]] | C | RFX3-DT activity lowers DNAH12's level | lines that do not express RFX3-DT (3) vs lines expressing it (47) | 1.16× higher at baseline in the lines without RFX3-DT | 0.084 | ⚠ few lines (3 vs 47); within organs, on part of the lines; co-absent genes; also absent: POGLUT2, ANAPC1P4, WDR35; maybe low, not absent |

## Where it sits

- **Module**: [[Module 023]]; 179 genes; this gene is in the **+** arm (projection on the module's main direction 0.835). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.34).
- **Nodal map** (x, y) = (5.4, 16.1); signed map (26.0, -8.9). **Vector** length 118, 33.2% of its response variance represented; |z| ≥ 3 in 1,148 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 0.5 µM |  | +12.1 | +8.8 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +10.8 | +15.6 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +5.9 | +5.0 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | +5.6 | +6.9 |
|  | [[Auranofin (drug)]] 5 µM |  | +5.5 | +4.0 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +5.0 | +4.7 |
|  | [[GSK1059615 (drug)]] 5 µM |  | +3.4 | +2.4 |
|  | [[Filgotinib (drug)]] 5 µM |  | +3.1 | +2.8 |
| fall | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~35% of this change | -8.4 | -8.6 |
|  | [[Belinostat (drug)]] 0.5 µM |  | -8.3 | -7.7 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~31% of this change | -7.8 | -8.8 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~42% of this change | -6.7 | -7.5 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~33% of this change | -6.6 | -3.1 |
|  | [[Brivudine (drug)]] 5 µM |  | -4.7 | -2.2 |
|  | [[PH-797804 (drug)]] 5 µM |  | -3.2 | -7.0 |
|  | [[Radotinib (drug)]] 5 µM |  | -2.8 | -3.1 |
|  | [[Niclosamide (olamine) (drug)]] 0.5 µM |  | -2.5 | -3.8 |
|  | [[Brivudine (drug)]] 0.5 µM |  | -2.4 | -1.6 |

## What is on record

|  |  |
|---|---|
| Name | RFX3 divergent transcript |
| Locus type | RNA, long non-coding (non-coding RNA) |
| Location | 9p24.2 — chr9:3,526,459-3,691,814 (+) |
| Ensembl biotype | lncRNA |
| Also known as | ; previously RFX3-AS1 |
| Gene groups (HGNC) | Divergent transcripts |
| Matched by | ensembl_id |

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:51197](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:51197) · Entrez [101929302](https://www.ncbi.nlm.nih.gov/gene/101929302) · Ensembl [ENSG00000232104](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000232104)

## Data

Gene col 13836: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 13836); `tables/drug_effects.parquet` (36 rows, flagged included); `relations/gene_relations.parquet` (col_a == 13836, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 13836]; `tensor/DDL_lfc|DDL_z.npy` [13836]; `embed/gene_vectors.npy` [13836]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 13836 or target_col == 13836). Every well: [[RFX3-DT — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/RFX3-DT.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
