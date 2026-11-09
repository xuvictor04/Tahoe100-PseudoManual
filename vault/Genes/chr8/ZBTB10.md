---
symbol: "ZBTB10"
type: "gene"
col: 12955
ensembl_id: "ENSG00000205189"
name: "zinc finger and BTB domain containing 10"
location: "8q21.13"
module: 69
arm: "+"
pooled_cpm: 88.13
n_lines_expressing: 46
n_dd_up: 34
n_dd_down: 19
n_dd_up_clean: 26
n_dd_down_clean: 16
in_vector_space: true
direction_upstream: 2
direction_downstream: 1
tags: ["gene", "module/069"]
generated_by: "tahoemap"
---

# ZBTB10

*zinc finger and BTB domain containing 10* — 8q21.13

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 34 drug-doses (8 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 13.8× (z +56.4, q 0e+00, up in 44 of 44 measured lines).
> Pooled over the cell lines (median), lowered significantly by 19 drug-doses (3 with an alert ⚠); the strongest is [[c-Kit-IN-1 (drug)]] 0.05 µM: 0.500× (z -10.5, q 3e-23, down in 39 of 44 measured lines) ⚠ unreliable plate only. The strongest without an alert is [[TAK-733 (drug)]] 5 µM: 0.435× (z -6.6, q 7e-09, down in 37 of 43 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[NR1D2]] (+0.77, fdr 7e-06), [[CYLD]] (+0.72, fdr 7e-06), [[CREBRF]] (+0.70, fdr 7e-06); moves opposite to [[RNGTT]] (-0.70, fdr 7e-06), [[EIPR1]] (-0.64, fdr 1e-05), [[FUBP3]] (-0.60, fdr 1e-05).
> It is in [[Module 069]], a single-armed module (FOXO-mediated transcription).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[ARID5B]] → it (grade B ⚠); 1 goes from it, the strongest it → [[ZNF706]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 35 in all, 8 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 34 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 12955.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **13.8×** | +56.4 | 0e+00 | 44/44 (PANC-1, C32, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **8.19×** | +30.7 | 0e+00 | 44/44 (PANC-1, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **5.67×** | +26.3 | 0e+00 | 44/44 (PANC-1, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **2.77×** | +15.5 | 0e+00 | 38/44 (PANC-1, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here) |
| [[TAK-901 (drug)]] 5 µM |  | **5.60×** | +13.7 | 2e-40 | 43/45 (PANC-1, NCI-H2347, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~2% here); composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **2.42×** | +13.4 | 4e-39 | 43/44 (PANC-1, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here); composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.96×** | +10.2 | 2e-22 | 40/44 (NCI-H460, BT-474, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.90×** | +9.4 | 4e-19 | 38/43 (NCI-H460, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.55×** | +9.3 | 6e-19 | 35/45 (HOP62, SW480, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.82×** | +9.1 | 6e-18 | 37/43 (NCI-H460, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.81×** | +9.0 | 1e-17 | 40/43 (NCI-H460, BT-474, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.76×** | +8.6 | 5e-16 | 34/44 (NCI-H460, A549, …) | all doses, stronger at high dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **1.51×** | +6.2 | 3e-08 | 29/44 (NCI-H460, BT-474, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.30×** | +5.6 | 8e-07 | 31/44 (C32, SW48, …) | all doses, stronger at high dose |  |
| [[Peretinoin (drug)]] 5 µM |  | **1.44×** | +5.4 | 3e-06 | 29/43 (A-427, SHP-77, …) | rises with dose | position effect removed |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **1.40×** | +5.1 | 1e-05 | 31/43 (NCI-H1792, LOX-IMVI, …) | rises with dose |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **1.27×** | +5.1 | 1e-05 | 27/45 (LOX-IMVI, CFPAC-1, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 19 in all, 3 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 19 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 12955.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.500×** | -10.5 | 3e-23 | 39/44 (NCI-H23, C32, …) | inconsistent across doses |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | **0.618×** | -7.0 | 5e-10 | 27/41 (Panc 03.27, LOX-IMVI, …) | rises with dose | composition shift |
| [[TAK-733 (drug)]] 5 µM |  | **0.435×** | -6.6 | 7e-09 | 37/43 (MIA PaCa-2, C32, …) | inconsistent across doses | noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **0.495×** | -5.6 | 3e-06 | 32/44 (SW 1271, SW 900, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Abemaciclib (drug)]] 5 µM |  | **0.498×** | -5.6 | 3e-06 | 31/44 (BT-474, LoVo, …) | rises with dose | noisy plate (z scaled) |
| [[EX229 (drug)]] 5 µM |  | **0.525×** | -5.1 | 3e-05 | 31/43 (LoVo, SW 1271, …) | rises with dose | noisy plate (z scaled) |
| [[Belzutifan (drug)]] 5 µM |  | **0.549×** | -4.8 | 1e-04 | 28/42 (NCI-H2030, H4, …) | top dose only | noisy plate (z scaled) |
| [[venetoclax (drug)]] 5 µM |  | **0.570×** | -4.5 | 5e-04 | 30/43 (MIA PaCa-2, SW1417, …) | top dose only | noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change | **0.751×** | -4.4 | 8e-04 | 22/44 (NCI-H2347, SK-MEL-2, …) | rises with dose | composition shift |
| [[Gallic acid (hydrate) (drug)]] 0.05 µM |  | **0.768×** | -4.0 | 0.003 | 21/44 (LOX-IMVI, SW48, …) | inconsistent across doses |  |
| [[EX229 (drug)]] 0.5 µM |  | **0.705×** | -3.8 | 0.007 | 24/45 (MIA PaCa-2, HCT15, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Sapanisertib (drug)]] 0.5 µM |  | **0.718×** | -3.6 | 0.015 | 19/44 (SW 1271, Hs 766T, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Diphenhydramine (drug)]] 0.5 µM |  | **0.793×** | -3.5 | 0.017 | 21/44 (hTERT-HPNE, HEC-1-A, …) | inconsistent across doses |  |
| [[Apalutamide (drug)]] 0.5 µM |  | **0.799×** | -3.4 | 0.025 | 18/44 (A498, LOX-IMVI, …) | inconsistent across doses |  |
| [[Palmatine (chloride) (drug)]] 0.05 µM |  | **0.804×** | -3.3 | 0.032 | 21/45 (Hs 766T, NCI-H1573, …) | inconsistent across doses |  |
| [[Tirabrutinib (drug)]] 0.5 µM |  | **0.808×** | -3.3 | 0.037 | 16/44 (SW 1088, A498, …) | inconsistent across doses |  |
| [[Carbamazepine (drug)]] 5 µM |  | **0.808×** | -3.3 | 0.037 | 14/43 (A498, NCI-H2030, …) | top dose only |  |
| [[Berbamine (drug)]] 0.05 µM |  | **0.809×** | -3.2 | 0.038 | 18/44 (NCI-H1573, NCI-H2347, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.38 per unit of S-phase module lfc, +0.35 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 12955. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 55.2 | 15 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 26.9× (z +39.3) | — |
| [[LoVo (line)]] | wt | 117 | 11 (2 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 20.0× (z +38.8) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.395× (z -8.5) ⚠ unreliable plate only |
| [[BT-474 (line)]] | alt | 173 | 11 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 8.08× (z +27.5) | — |
| [[PANC-1 (line)]] | alt | 129 | 11 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 24.1× (z +54.8) | — |
| [[C32 (line)]] | wt | 178 | 8 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 18.8× (z +45.8) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.405× (z -10.1) ⚠ unreliable plate only |
| [[NCI-H2347 (line)]] | alt | 203 | 7 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 19.5× (z +39.2) | [[Dinaciclib (drug)]] 5 µM 0.252× (z -12.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change |
| [[SW 900 (line)]] | alt | 125 | 9 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 14.4× (z +31.4) | — |
| [[A549 (line)]] | wt | 68.2 | 8 | 0 | [[Homoharringtonine (drug)]] 5 µM 33.5× (z +43.7) | — |
| [[HOP62 (line)]] | alt | 64.4 | 8 | 0 | [[Homoharringtonine (drug)]] 5 µM 19.6× (z +36.9) | — |
| [[hTERT-HPNE (line)]] | wt | 50.5 | 8 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 68.9× (z +35.0) | — |
| [[NCI-H1792 (line)]] | alt | 79.0 | 8 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 25.1× (z +40.4) | — |
| [[MIA PaCa-2 (line)]] | alt | 65.2 | 6 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 11.1× (z +26.1) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.329× (z -8.6) ⚠ unreliable plate only |
| [[H4 (line)]] | wt | 56.3 | 6 | 0 | [[Homoharringtonine (drug)]] 5 µM 12.7× (z +22.6) | — |
| [[HEC-1-A (line)]] | alt | 49.9 | 6 | 0 | [[Homoharringtonine (drug)]] 5 µM 10.8× (z +31.6) | — |
| [[HS-578T (line)]] | alt | 87.5 | 6 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 22.2× (z +36.0) | — |
| [[NCI-H1573 (line)]] | alt | 120 | 6 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 22.1× (z +26.6) | — |
| [[SNU-1 (line)]] | wt | 129 | 5 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 6.53× (z +17.2) | [[Dinaciclib (drug)]] 5 µM 0.108× (z -13.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change |
| [[SNU-423 (line)]] | alt | 85.6 | 4 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 26.4× (z +38.3) | [[Dinaciclib (drug)]] 5 µM 0.283× (z -10.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change |
| [[A-172 (line)]] | wt | 51.5 | 5 | 0 | [[Homoharringtonine (drug)]] 5 µM 70.2× (z +41.9) | — |
| [[A498 (line)]] | wt | 134 | 5 | 0 | [[Homoharringtonine (drug)]] 5 µM 49.9× (z +40.9) | — |
| [[J82 (line)]] | alt | 81.2 | 5 | 0 | [[Homoharringtonine (drug)]] 5 µM 42.9× (z +39.4) | — |
| [[NCI-H23 (line)]] | alt | 117 | 4 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.54× (z +17.4) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.353× (z -10.2) ⚠ unreliable plate only |
| [[Panc 03.27 (line)]] | alt | 51.4 | 4 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 38.5× (z +35.1) | [[Dinaciclib (drug)]] 5 µM 0.0972× (z -15.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change |
| [[SK-MEL-2 (line)]] | alt | 87.5 | 3 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 5.98× (z +24.7) | [[Dinaciclib (drug)]] 5 µM 0.368× (z -9.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change |
| [[A-427 (line)]] | wt | 77.2 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.04× (z +21.9) | — |
| [[AN3 CA (line)]] | alt | 135 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.83× (z +15.5) | — |
| [[CFPAC-1 (line)]] | alt | 84.6 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 39.7× (z +38.8) | — |
| [[RPMI-7951 (line)]] | alt | 46.4 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 12.9× (z +20.8) | — |
| [[SW1417 (line)]] | alt | 52.7 | 3 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 6.00× (z +22.9) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.380× (z -8.8) ⚠ unreliable plate only |
| [[SW48 (line)]] | wt | 40.2 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 33.3× (z +24.5) | — |
| [[SW480 (line)]] | alt | 54.8 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.74× (z +20.7) | — |
| [[COLO 205 (line)]] | alt | 68.2 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 16.9× (z +29.7) | — |
| [[HCT15 (line)]] | alt | 79.5 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.26× (z +18.9) | — |
| [[HepG2_C3A (line)]] | wt | 152 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 8.57× (z +26.8) | — |
| [[Hs 766T (line)]] | wt | 79.6 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 9.30× (z +25.0) | — |
| [[LOX-IMVI (line)]] | wt | 125 | 2 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.25× (z +19.9) | [[Dinaciclib (drug)]] 5 µM 0.219× (z -14.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change |
| [[NCI-H2030 (line)]] | alt | 140 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.44× (z +24.2) | — |
| [[C-33 A (line)]] | alt | 104 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.12× (z +15.2) | — |
| [[CHP-212 (line)]] | wt | 87.5 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.76× (z +11.6) | — |
| [[HT-29 (line)]] | alt | 57.0 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 11.8× (z +22.6) | — |
| [[SHP-77 (line)]] | alt | 161 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.14× (z +11.1) | — |
| [[SW 1088 (line)]] | alt | 23.6 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 37.3× (z +9.5) | — |
| [[SW 1271 (line)]] | alt | 194 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 13.3× (z +17.8) | — |
| [[AsPC-1 (line)]] | alt | 13.1 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 5.91 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 6.25 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 101 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 97.8 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 96.7 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 6.54 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 12955), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*80 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NR1D2]] | +0.77 | +0.73 / +0.74 | both halves | 7e-06 |  |
| [[CYLD]] | +0.72 | +0.72 / +0.70 | both halves | 7e-06 |  |
| [[CREBRF]] | +0.70 | +0.65 / +0.65 | both halves | 7e-06 |  |
| [[PIK3IP1]] | +0.66 | +0.53 / +0.70 | both halves | 1e-05 |  |
| [[DRAM1]] | +0.65 | +0.75 / +0.52 | both halves | 1e-05 | pathway: HALLMARK_TNFA_SIGNALING_VIA_NFKB |
| [[CHD2]] | +0.65 | +0.55 / +0.63 | both halves | 1e-05 |  |
| [[OTUD1]] | +0.64 | +0.52 / +0.68 | both halves | 1e-05 |  |
| [[JMY]] | +0.63 | +0.58 / +0.62 | both halves | 7e-06 |  |
| [[GADD45B]] | +0.63 | +0.61 / +0.61 | both halves | 7e-06 | pathway: HALLMARK_TNFA_SIGNALING_VIA_NFKB |
| [[STAT5A]] | +0.63 | +0.58 / +0.60 | both halves | 8e-06 | pathway: HALLMARK_TNFA_SIGNALING_VIA_NFKB |
| [[RAB21]] | +0.63 | +0.61 / +0.59 | both halves | 7e-06 |  |
| [[YTHDC1]] | +0.62 | +0.55 / +0.62 | both halves | 1e-05 |  |

## Genes that move opposite

*20 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RNGTT]] | -0.70 | -0.67 / -0.62 | both halves | 7e-06 |  |
| [[EIPR1]] | -0.64 | -0.56 / -0.62 | both halves | 1e-05 |  |
| [[FUBP3]] | -0.60 | -0.56 / -0.60 | both halves | 1e-05 |  |
| [[NUP214]] | -0.58 | -0.46 / -0.61 | both halves | 3e-05 |  |
| [[NCLN]] | -0.57 | -0.46 / -0.55 | both halves | 3e-05 |  |
| [[TOMM40]] | -0.57 | -0.44 / -0.58 | both halves | 3e-05 |  |
| [[NAPG]] | -0.56 | -0.56 / -0.42 | both halves | 4e-05 |  |
| [[DEPDC5]] | -0.55 | -0.43 / -0.55 | both halves | 3e-05 |  |
| [[GBA2]] | -0.54 | -0.47 / -0.50 | both halves | 2e-05 |  |
| [[EARS2]] | -0.54 | -0.39 / -0.63 | both halves | 5e-05 |  |
| [[SENP5]] | -0.54 | -0.58 / -0.53 | both halves | 1e-05 |  |
| [[DGKG]] | -0.54 | -0.56 / -0.50 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 1, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ARID5B]] | B | ARID5B activity raises ZBTB10's level | lines that do not express ARID5B (6) vs lines expressing it (44) | 2.10× lower at baseline in the lines without ARID5B | 0.042 | ⚠ within organs, on part of the lines; also absent: TNFAIP3, ATXN1, SSUH2 |
| [[CITED2]] | C | CITED2 activity raises ZBTB10's level | lines that do not express CITED2 (3) vs lines expressing it (47) | 5.25× lower at baseline in the lines without CITED2 | 0.015 | ⚠ few lines (3 vs 47); across organs; also absent: RDX, FNBP1, BMS1P23; maybe low, not absent |

### Downstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ZNF706]] | C | ZBTB10 activity lowers ZNF706's level | lines that do not express ZBTB10 (4) vs lines expressing it (46) | 1.84× higher at baseline in the lines without ZBTB10 | 0.089 | ⚠ few lines (4 vs 46); within organs, on part of the lines; co-absent genes; also absent: GGT7, NAT14, SOGA1; its own permutation p |

## Where it sits

- **Module**: [[Module 069]] — FOXO-mediated transcription; 71 genes; every member is in the + arm (projection on the module's main direction 0.675). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.33; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-0.2, -39.2); signed map (-9.9, 11.8). **Vector** length 114, 37.3% of its response variance represented; |z| ≥ 3 in 1,429 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~19% of this change | +7.4 | +3.8 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +7.0 | +5.6 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | +6.6 | +15.5 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +6.3 | +9.3 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +5.9 | +3.6 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +5.8 | +8.6 |
|  | [[Binimetinib (drug)]] 5 µM |  | +5.2 | +2.5 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +4.7 | +0.8 |
| fall | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -10.4 | -10.5 |
|  | [[EX229 (drug)]] 5 µM |  | -6.3 | -5.1 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -6.0 | -5.6 |
|  | [[TAK-733 (drug)]] 5 µM |  | -5.9 | -6.6 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | -5.5 | -5.6 |
|  | [[Abemaciclib (drug)]] 0.5 µM |  | -5.5 | -2.6 |

## What is on record

|  |  |
|---|---|
| Name | zinc finger and BTB domain containing 10 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 8q21.13 — chr8:80,485,619-80,526,265 (+) |
| Ensembl biotype | protein_coding |
| Also known as | RINZF, FLJ12752 |
| Gene groups (HGNC) | Zinc fingers C2H2-type; BTB domain containing |
| Hallmark sets | ANDROGEN_RESPONSE, TNFA_SIGNALING_VIA_NFKB |
| Matched by | ensembl_id |

**Function**, from UniProt [Q96DT7](https://www.uniprot.org/uniprotkb/Q96DT7) (Zinc finger and BTB domain-containing protein 10):

> May be involved in transcriptional regulation.

**Summary**, from NCBI Gene [65986](https://www.ncbi.nlm.nih.gov/gene/65986):

> Enables telomeric repeat DNA binding activity. Predicted to be involved in negative regulation of transcription by RNA polymerase II. Located in chromosome, telomeric region and nucleoplasm. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:30953](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:30953) · Entrez [65986](https://www.ncbi.nlm.nih.gov/gene/65986) · UniProt [Q96DT7](https://www.uniprot.org/uniprotkb/Q96DT7) · Ensembl [ENSG00000205189](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000205189)

## Data

Gene col 12955: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 12955); `tables/drug_effects.parquet` (54 rows, flagged included); `relations/gene_relations.parquet` (col_a == 12955, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 12955]; `tensor/DDL_lfc|DDL_z.npy` [12955]; `embed/gene_vectors.npy` [12955]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 12955 or target_col == 12955). Every well: [[ZBTB10 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ZBTB10.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
