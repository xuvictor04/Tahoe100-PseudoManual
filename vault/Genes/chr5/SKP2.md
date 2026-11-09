---
symbol: "SKP2"
type: "gene"
col: 7007
ensembl_id: "ENSG00000145604"
name: "S-phase kinase associated protein 2"
location: "5p13.2"
module: 57
arm: "+"
pooled_cpm: 22.92
n_lines_expressing: 49
n_dd_up: 28
n_dd_down: 17
n_dd_up_clean: 19
n_dd_down_clean: 14
in_vector_space: true
direction_upstream: 12
direction_downstream: 0
tags: ["gene", "module/057"]
generated_by: "tahoemap"
---

# SKP2

*S-phase kinase associated protein 2* — 5p13.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 28 drug-doses (9 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 3.41× (z +17.7, q 0e+00, up in 46 of 47 measured lines) ⚠ cell-cycle shift, explains ~26% of this change. The strongest without an alert is [[Panobinostat (drug)]] 0.5 µM: 3.01× (z +15.9, q 0e+00, up in 45 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 17 drug-doses (3 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.457× (z -16.0, q 0e+00, down in 42 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[RPA1]] (+0.79, fdr 7e-06), [[NUDT21]] (+0.77, fdr 7e-06), [[ELP1]] (+0.76, fdr 7e-06); moves opposite to [[XIAP]] (-0.74, fdr 7e-06), [[OFD1]] (-0.69, fdr 7e-06), [[RAB30-DT]] (-0.68, fdr 1e-05).
> It sits in the **+** arm of [[Module 057]] (Peroxisomal protein import).
> Probable direction (from the cell lines, not proof of direct regulation): 12 arrows point to it, the strongest [[KATNAL1]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 30 in all, 10 with an alert ⚠; shown: the 15 strongest and the 7 next strongest without an alert. 28 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7007.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **3.41×** | +17.7 | 0e+00 | 46/47 (LOX-IMVI, PANC-1, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 0.5 µM |  | **3.01×** | +15.9 | 0e+00 | 45/47 (PANC-1, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~25% here) |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **2.78×** | +14.8 | 0e+00 | 43/47 (J82, PANC-1, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.79×** | +8.4 | 7e-15 | 39/47 (J82, SW1417, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here) |
| [[Ponatinib (drug)]] 5 µM |  | **1.69×** | +7.5 | 6e-12 | 35/47 (NCI-H2030, LOX-IMVI, …) | all doses, stronger at high dose |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~56% of this change | **1.57×** | +6.2 | 5e-08 | 19/34 (LS 180, KATO III, …) | rises with dose | composition shift |
| [[Brivudine (drug)]] 5 µM |  | **2.21×** | +6.0 | 2e-07 | 29/47 (J82, NCI-H2030, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~66% of this change | **1.48×** | +5.6 | 1e-06 | 20/41 (NCI-H1573, LoVo, …) | rises with dose | composition shift |
| [[PH-797804 (drug)]] 5 µM |  | **1.97×** | +5.1 | 2e-05 | 22/46 (SW1417, PANC-1, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~19% of this change | **1.28×** | +5.0 | 3e-05 | 28/47 (SNU-423, J82, …) | top dose only | low cells (technical?) |
| [[Radotinib (drug)]] 5 µM |  | **1.27×** | +4.9 | 4e-05 | 23/47 (NCI-H2030, RKO, …) | rises with dose |  |
| [[NG25 (drug)]] 5 µM |  | **1.83×** | +4.6 | 2e-04 | 19/45 (NCI-H23, J82, …) | top dose only | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **1.35×** | +4.3 | 7e-04 | 20/46 (J82, NCI-H2347, …) | rises with dose |  |
| [[TAK-901 (drug)]] 5 µM |  | **1.72×** | +4.1 | 0.002 | 18/47 (J82, SW1417, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.32×** | +4.0 | 0.002 | 18/47 (A-427, NCI-H23, …) | inconsistent across doses |  |
| [[Flumatinib (mesylate) (drug)]] 5 µM |  | **1.33×** | +4.0 | 0.002 | 19/46 (NCI-H2030, HepG2/C3A, …) | top dose only |  |
| [[Cabozantinib (S-malate) (drug)]] 5 µM |  | **1.32×** | +3.9 | 0.003 | 12/47 (NCI-H2030, NCI-H460, …) | top dose only |  |
| [[Ipatasertib (drug)]] 5 µM |  | **1.61×** | +3.6 | 0.009 | 9/47 (NCI-H2030, SW 900, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Pyridoxine (hydrochloride) (drug)]] 5 µM |  | 1.19× | +3.6 | 0.009 | 14/47 (HCT15, PANC-1, …) | inconsistent across doses |  |
| [[Pyridoxine (hydrochloride) (drug)]] 0.05 µM |  | **1.28×** | +3.6 | 0.010 | 11/47 (J82, HEC-1-A, …) | inconsistent across doses |  |
| [[Ralimetinib dimesylate (drug)]] 5 µM |  | **1.56×** | +3.3 | 0.022 | 8/47 (SW 900, A498, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[TAK-901 (drug)]] 0.05 µM |  | **1.27×** | +3.2 | 0.033 | 12/46 (BT-474, SW1417, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 18 in all, 4 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 17 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 7007.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.457×** | -16.0 | 0e+00 | 42/47 (PANC-1, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.451×** | -11.5 | 3e-28 | 38/47 (NCI-H460, MIA PaCa-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.439×** | -11.5 | 4e-28 | 39/47 (HOP62, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.567×** | -8.2 | 3e-14 | 25/45 (PANC-1, HOP62, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.574×** | -8.0 | 1e-13 | 32/47 (NCI-H460, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.607×** | -7.2 | 5e-11 | 31/47 (PANC-1, RKO, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.608×** | -7.2 | 5e-11 | 29/46 (PANC-1, SW 900, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.650×** | -6.3 | 3e-08 | 29/47 (HOP62, RKO, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.767×** | -5.4 | 3e-06 | 25/47 (HOP62, MIA PaCa-2, …) | rises with dose |  |
| [[Auranofin (drug)]] 5 µM |  | **0.687×** | -5.4 | 3e-06 | 31/47 (C32, SW 900, …) | top dose only |  |
| [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **0.798×** | -4.6 | 2e-04 | 19/47 (SW480, NCI-H460, …) | rises with dose |  |
| [[Entrectinib (drug)]] 5 µM |  | **0.773×** | -3.7 | 0.009 | 16/46 (A498, Panc 03.27, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.784×** | -3.5 | 0.018 | 18/47 (NCI-H460, MIA PaCa-2, …) | all doses, stronger at high dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.848× | -3.4 | 0.029 | 14/47 (C32, NCI-H23, …) | rises with dose |  |
| [[5-Azacytidine (drug)]] 5 µM |  | **0.793×** | -3.4 | 0.029 | 12/46 (J82, Hs 766T, …) | top dose only |  |
| [[PF-06260933 (drug)]] 5 µM |  | **0.663×** | -3.1 | 0.062 | 10/45 (SK-MEL-2, NCI-H2347, …) | top dose only | noisy plate (z scaled) |
| [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM |  | **0.813×** | -3.0 | 0.083 | 12/45 (BT-474, SHP-77, …) | inconsistent across doses | low cells (technical?); position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.57 per unit of S-phase module lfc, -0.34 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7007. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 15.7 | 3 (2 ⚠) | 6 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 3.79× (z +10.5) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 3.32× (z +9.5) | [[Homoharringtonine (drug)]] 5 µM 0.168× (z -19.9) |
| [[A498 (line)]] | wt | 21.2 | 2 (1 ⚠) | 4 | [[Panobinostat (drug)]] 5 µM 3.40× (z +9.3) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 3.09× (z +8.6) | [[Homoharringtonine (drug)]] 0.5 µM 0.180× (z -13.1) |
| [[HOP62 (line)]] | alt | 19.8 | 0 | 5 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.165× (z -17.5) |
| [[LOX-IMVI (line)]] | wt | 18.5 | 3 (2 ⚠) | 2 | [[Panobinostat (drug)]] 5 µM 5.99× (z +10.6) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 4.38× (z +8.8) | [[Homoharringtonine (drug)]] 5 µM 0.271× (z -11.0) |
| [[NCI-H460 (line)]] | wt | 24.4 | 0 | 5 | — | [[Homoharringtonine (drug)]] 5 µM 0.178× (z -19.4) |
| [[NCI-H2030 (line)]] | alt | 27.9 | 2 (2 ⚠) | 2 | [[Panobinostat (drug)]] 5 µM 3.39× (z +8.8) ⚠ cell-cycle shift, explains ~26% of this change | [[Homoharringtonine (drug)]] 5 µM 0.273× (z -13.3) |
| [[A-172 (line)]] | wt | 16.9 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.167× (z -14.6) |
| [[C32 (line)]] | wt | 17.3 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.211× (z -11.6) |
| [[J82 (line)]] | alt | 54.9 | 2 (2 ⚠) | 1 | [[Belinostat (drug)]] 5 µM 3.50× (z +10.1) ⚠ cell-cycle shift, explains ~26% of this change | [[Homoharringtonine (drug)]] 5 µM 0.249× (z -15.9) |
| [[MIA PaCa-2 (line)]] | alt | 32.6 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.195× (z -15.4) |
| [[NCI-H1792 (line)]] | alt | 15.8 | 3 (2 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 6.15× (z +10.2) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 4.74× (z +8.7) | — |
| [[NCI-H23 (line)]] | alt | 48.9 | 2 (1 ⚠) | 1 | [[Panobinostat (drug)]] 5 µM 3.18× (z +9.0) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 3.01× (z +8.6) | [[Homoharringtonine (drug)]] 5 µM 0.196× (z -18.2) |
| [[CFPAC-1 (line)]] | alt | 12.2 | 1 (1 ⚠) | 1 | [[Panobinostat (drug)]] 5 µM 4.69× (z +8.9) ⚠ cell-cycle shift, explains ~26% of this change | [[Homoharringtonine (drug)]] 5 µM 0.284× (z -10.2) |
| [[COLO 205 (line)]] | alt | 13.4 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.125× (z -12.4) |
| [[H4 (line)]] | wt | 24.9 | 0 | 2 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0774× (z -12.0) |
| [[Hs 766T (line)]] | wt | 20.9 | 1 (1 ⚠) | 1 | [[Panobinostat (drug)]] 5 µM 4.29× (z +8.7) ⚠ cell-cycle shift, explains ~26% of this change | [[Homoharringtonine (drug)]] 5 µM 0.204× (z -13.6) |
| [[LoVo (line)]] | wt | 20.1 | 1 (1 ⚠) | 1 | [[Panobinostat (drug)]] 5 µM 3.92× (z +9.3) ⚠ cell-cycle shift, explains ~26% of this change | [[Homoharringtonine (drug)]] 5 µM 0.356× (z -10.2) |
| [[RKO (line)]] | wt | 21.3 | 1 | 1 | [[Panobinostat (drug)]] 0.5 µM 4.76× (z +8.6) | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.186× (z -9.3) |
| [[SW1417 (line)]] | alt | 22.1 | 2 (2 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 4.25× (z +9.6) ⚠ cell-cycle shift, explains ~26% of this change | — |
| [[SW480 (line)]] | alt | 32.8 | 1 (1 ⚠) | 1 | [[Panobinostat (drug)]] 5 µM 2.88× (z +8.7) ⚠ cell-cycle shift, explains ~26% of this change | [[Homoharringtonine (drug)]] 5 µM 0.442× (z -9.6) |
| [[A549 (line)]] | wt | 10.2 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.257× (z -9.8) |
| [[AN3 CA (line)]] | alt | 65.1 | 0 | 1 | — | [[Estrone sulfate (potassium) (drug)]] 0.5 µM 0.158× (z -9.1) |
| [[HEC-1-A (line)]] | alt | 31.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.275× (z -9.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~56% of this change |
| [[HS-578T (line)]] | alt | 14.7 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.156× (z -8.8) |
| [[HT-29 (line)]] | alt | 14.5 | 1 (1 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 5.38× (z +8.9) ⚠ cell-cycle shift, explains ~26% of this change | — |
| [[NCI-H1573 (line)]] | alt | 8.88 | 1 (1 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 7.74× (z +10.0) ⚠ cell-cycle shift, explains ~26% of this change | — |
| [[NCI-H2347 (line)]] | alt | 22.7 | 1 (1 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 3.54× (z +8.5) ⚠ cell-cycle shift, explains ~26% of this change | — |
| [[SNU-423 (line)]] | alt | 12.8 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.261× (z -10.0) |
| [[SW 900 (line)]] | alt | 22.7 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.201× (z -8.6) |
| [[A-427 (line)]] | wt | 34.0 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 4.98 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 12.0 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 40.4 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 34.8 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 29.2 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 10.6 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 9.75 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 14.2 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 21.5 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 18.3 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 23.9 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 55.7 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 23.8 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 13.3 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 72.0 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 5.86 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 24.9 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 27.9 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 24.3 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 32.8 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7007), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*73 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RPA1]] | +0.79 | +0.74 / +0.74 | both halves | 7e-06 | pathway: DNA Replication |
| [[NUDT21]] | +0.77 | +0.75 / +0.70 | both halves | 7e-06 |  |
| [[ELP1]] | +0.76 | +0.64 / +0.79 | both halves | 7e-06 |  |
| [[KDM1A]] | +0.74 | +0.78 / +0.72 | both halves | 7e-06 |  |
| [[CASP2]] | +0.73 | +0.65 / +0.66 | both halves | 7e-06 |  |
| [[SDHAF3]] | +0.73 | +0.70 / +0.61 | both halves | 7e-06 |  |
| [[PAPSS1]] | +0.73 | +0.67 / +0.66 | both halves | 7e-06 |  |
| [[UBAC1]] | +0.72 | +0.73 / +0.55 | both halves | 1e-05 | pathway: Antigen processing: Ubiquitination & Proteasome degradation |
| [[PARP1]] | +0.72 | +0.57 / +0.70 | both halves | 9e-06 | STRING 457 |
| [[NCAPD3]] | +0.71 | +0.68 / +0.65 | both halves | 7e-06 |  |
| [[GTPBP3]] | +0.71 | +0.62 / +0.59 | both halves | 7e-06 |  |
| [[NDRG3]] | +0.70 | +0.69 / +0.58 | both halves | 7e-06 |  |

## Genes that move opposite

*27 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[XIAP]] | -0.74 | -0.68 / -0.71 | both halves | 7e-06 |  |
| [[OFD1]] | -0.69 | -0.68 / -0.66 | both halves | 7e-06 |  |
| [[RAB30-DT]] | -0.68 | -0.67 / -0.57 | both halves | 1e-05 |  |
| [[LINC02307]] | -0.67 | -0.61 / -0.55 | both halves | 1e-05 |  |
| [[LINC01004]] | -0.67 | -0.66 / -0.55 | both halves | 1e-05 |  |
| [[PPP1R12A-AS2]] | -0.67 | -0.58 / -0.57 | both halves | 9e-06 |  |
| [[PLA2G4C]] | -0.67 | -0.66 / -0.48 | both halves | 2e-05 |  |
| [[EIF4EBP3]] | -0.66 | -0.61 / -0.49 | both halves | 1e-05 |  |
| [[CHMP4A]] | -0.66 | -0.77 / -0.57 | both halves | 1e-05 |  |
| [[RNF103-CHMP3]] | -0.66 | -0.63 / -0.53 | both halves | 1e-05 |  |
| [[KRBOX5]] | -0.65 | -0.69 / -0.46 | both halves | 3e-05 |  |
| [[GGPS1]] | -0.65 | -0.58 / -0.56 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*12 arrows, 12 of them with an alert ⚠; grade A 0, B 8, C 4.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[KATNAL1]] | B | KATNAL1 activity raises SKP2's level | lines that do not express KATNAL1 (7) vs lines expressing it (43) | 1.76× lower at baseline in the lines without KATNAL1 | 0.012 | ⚠ within organs, on part of the lines; also absent: BOLA3-DT, STARD9, SPAG17 |
| [[CLCF1]] | B | CLCF1 activity lowers SKP2's level | lines that do not express CLCF1 (7) vs lines expressing it (43) | 1.55× higher at baseline in the lines without CLCF1 | 0.060 | ⚠ within organs, on part of the lines; also absent: SIGIRR, ENSG00000256514, HTATIP2; maybe low, not absent |
| [[HLTF]] | B | HLTF activity raises SKP2's level | lines that do not express HLTF (8) vs lines expressing it (42) | 1.36× lower at baseline in the lines without HLTF | 0.067 | ⚠ within organs, on part of the lines; also absent: HDGFL3, ZNF512B, FERMT2 |
| [[IL32]] | B | IL32 activity lowers SKP2's level | lines that do not express IL32 (18) vs lines expressing it (32) | 1.55× higher at baseline in the lines without IL32 | 0.070 | ⚠ within organs, on part of the lines; also absent: PODXL, APOL1, F3 |
| [[ABL1]] | B | ABL1 activity lowers SKP2's level | compounds that target ABL1: 4 of 6 raise it (Flumatinib, NG25, Ponatinib, Radotinib) | 67% of the class's compounds vs 6.2% of all compounds | 0.071 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[PODXL2]] | B | PODXL2 activity raises SKP2's level | lines that do not express PODXL2 (14) vs lines expressing it (36) | 1.50× lower at baseline in the lines without PODXL2 | 0.079 | ⚠ within organs, on part of the lines |
| [[GGH]] | B | GGH activity raises SKP2's level | lines that do not express GGH (5) vs lines expressing it (45) | 1.47× lower at baseline in the lines without GGH | 0.079 | ⚠ within organs, on part of the lines; also absent: AADAT, LINC01341, HHAT; maybe low, not absent |
| [[RNF103-CHMP3]] | B | RNF103-CHMP3 activity lowers SKP2's level | lines that do not express RNF103-CHMP3 (5) vs lines expressing it (45) | 1.83× higher at baseline in the lines without RNF103-CHMP3 | 0.089 | ⚠ within organs, on part of the lines; also absent: TMEM144, YBX3, DTX4; maybe low, not absent |
| [[DSCC1]] | C | DSCC1 activity raises SKP2's level | lines that do not express DSCC1 (4) vs lines expressing it (46) | 2.38× lower at baseline in the lines without DSCC1 | 0.034 | ⚠ few lines (4 vs 46); across organs; also absent: NDC80, ADGRL1, MYBL2; maybe low, not absent |
| [[GPD1L]] | C | GPD1L activity raises SKP2's level | lines that do not express GPD1L (4) vs lines expressing it (46) | 2.19× lower at baseline in the lines without GPD1L | 0.055 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: ZBED3, DNMT3B, MYBL2; maybe low, not absent |
| [[HACE1]] | C | HACE1 activity raises SKP2's level | lines that do not express HACE1 (3) vs lines expressing it (47) | 2.10× lower at baseline in the lines without HACE1 | 0.060 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: AXDND1, CFL2, ATP6V1E2; maybe low, not absent; its own permutation p |
| [[GSTM4]] | C | GSTM4 activity raises SKP2's level | lines that do not express GSTM4 (4) vs lines expressing it (46) | 1.87× lower at baseline in the lines without GSTM4 | 0.098 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: LINC00888, KIF3C, GGH; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 057]] — Peroxisomal protein import; 86 genes; this gene is in the **+** arm (projection on the module's main direction 0.841). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.30).
- **Nodal map** (x, y) = (-7.4, -13.3); signed map (-38.0, -13.2). **Vector** length 121, 33.8% of its response variance represented; |z| ≥ 3 in 1,206 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | +5.5 | +14.8 |
|  | [[PH-797804 (drug)]] 5 µM |  | +5.4 | +5.1 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | +5.4 | +17.7 |
|  | [[TAK-901 (drug)]] 5 µM |  | +4.8 | +4.1 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | +4.7 | +15.9 |
|  | [[Radotinib (drug)]] 5 µM |  | +4.4 | +4.9 |
|  | [[Ponatinib (drug)]] 5 µM |  | +3.7 | +7.5 |
|  | [[Flumatinib (mesylate) (drug)]] 5 µM |  | +3.2 | +4.0 |
|  | [[Ipatasertib (drug)]] 5 µM |  | +2.9 | +3.6 |
| fall | [[Homoharringtonine (drug)]] 5 µM |  | -10.8 | -16.0 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -10.1 | -11.5 |
|  | [[Harringtonine (drug)]] 5 µM |  | -8.3 | -11.5 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -6.5 | -3.4 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -6.1 | -8.0 |
|  | [[Auranofin (drug)]] 5 µM |  | -5.4 | -5.4 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -4.1 | -5.4 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -4.0 | -3.5 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -3.9 | -3.4 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | -2.6 | -2.8 |

## What is on record

|  |  |
|---|---|
| Name | S-phase kinase associated protein 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 5p13.2 — chr5:36,151,989-36,196,849 (+) |
| Ensembl biotype | protein_coding |
| Also known as | FBXL1, FBL1, p45 |
| Gene groups (HGNC) | F-box and leucine rich repeat proteins; E3 ubiquitin ligases |
| Hallmark sets | WNT_BETA_CATENIN_SIGNALING |
| Reactome | 33 pathways, smallest: Regulation of BACH1 activity; Aberrant regulation of mitotic exit in cancer due to RB1 defects; Aberrant regulation of mitotic cell cycle due to RB1 defects |
| Matched by | ensembl_id |

**Function**, from UniProt [Q13309](https://www.uniprot.org/uniprotkb/Q13309) (S-phase kinase-associated protein 2):

> Substrate recognition component of a SCF (SKP1-CUL1-F-box protein) E3 ubiquitin-protein ligase complex which mediates the ubiquitination and subsequent proteasomal degradation of target proteins involved in cell cycle progression, signal transduction and transcription. The E3 ubiquitin-protein ligase activity is regulated by the COP9 signalosome (CSN), which restores the ligase to its inactive state and resets the ligase for substrate recognition by reversing the activating neddylation on the …

**Summary**, from NCBI Gene [6502](https://www.ncbi.nlm.nih.gov/gene/6502):

> This gene encodes a member of the F-box protein family which is characterized by an approximately 40 amino acid motif, the F-box. The F-box proteins constitute one of the four subunits of ubiquitin protein ligase complex called SCFs (SKP1-cullin-F-box), which function in phosphorylation-dependent ubiquitination. The F-box proteins are divided into 3 classes: Fbws containing WD-40 domains, Fbls containing leucine-rich repeats, and Fbxs containing either different protein-protein interaction …

**Accessions** — [HGNC:10901](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:10901) · Entrez [6502](https://www.ncbi.nlm.nih.gov/gene/6502) · UniProt [Q13309](https://www.uniprot.org/uniprotkb/Q13309) · Ensembl [ENSG00000145604](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000145604)

## Data

Gene col 7007: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7007); `tables/drug_effects.parquet` (48 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7007, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7007]; `tensor/DDL_lfc|DDL_z.npy` [7007]; `embed/gene_vectors.npy` [7007]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7007 or target_col == 7007). Every well: [[SKP2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SKP2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
