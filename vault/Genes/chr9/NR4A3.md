---
symbol: "NR4A3"
type: "gene"
col: 4072
ensembl_id: "ENSG00000119508"
name: "nuclear receptor subfamily 4 group A member 3"
location: "9q31.1"
module: 223
arm: "+"
pooled_cpm: 49.42
n_lines_expressing: 44
n_dd_up: 16
n_dd_down: 37
n_dd_up_clean: 10
n_dd_down_clean: 28
in_vector_space: true
direction_upstream: 3
direction_downstream: 3
tags: ["gene", "module/223"]
generated_by: "tahoemap"
---

# NR4A3

*nuclear receptor subfamily 4 group A member 3* — 9q31.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 16 drug-doses (6 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 3.09× (z +16.1, q 0e+00, up in 33 of 41 measured lines) ⚠ cell-cycle shift, explains ~31% of this change. The strongest without an alert is [[Harringtonine (drug)]] 5 µM: 4.14× (z +13.8, q 4e-41, up in 34 of 41 measured lines).
> Pooled over the cell lines (median), lowered significantly by 37 drug-doses (9 with an alert ⚠); the strongest is [[Ixazomib citrate (drug)]] 5 µM: 0.332× (z -10.7, q 7e-24, down in 32 of 41 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[NR4A2]] (+0.77, fdr 7e-06), [[NR4A1]] (+0.72, fdr 7e-06), [[HES1]] (+0.70, fdr 7e-06); moves opposite to [[RTCA]] (-0.59, fdr 1e-05), [[SVIL-AS1-1]] (-0.58, fdr 2e-05), [[CLCC1]] (-0.54, fdr 1e-05).
> It is in [[Module 223]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[RSPO3]] → it (grade B ⚠); 3 go from it, the strongest it → [[CA8]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 16 in all, 6 with an alert ⚠. 16 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4072.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **3.09×** | +16.1 | 0e+00 | 33/41 (SK-MEL-2, NCI-H1792, …) | rises with dose | composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **4.14×** | +13.8 | 4e-41 | 34/41 (SK-MEL-2, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~21% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **2.07×** | +7.1 | 3e-10 | 22/42 (HOP62, NCI-H460, …) | inconsistent across doses | composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **2.78×** | +5.4 | 9e-06 | 21/43 (SK-MEL-2, NCI-H1792, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~18% here); composition shift; noisy plate (z scaled) |
| [[Filgotinib (drug)]] 5 µM |  | **1.68×** | +5.0 | 5e-05 | 22/42 (NCI-H23, NCI-H460, …) | inconsistent across doses |  |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~43% of this change | **1.50×** | +4.1 | 0.003 | 17/40 (C32, HS-578T, …) | rises with dose |  |
| [[Binimetinib (drug)]] 0.05 µM |  | **1.32×** | +3.9 | 0.007 | 17/43 (HCT15, LoVo, …) | all doses, flat |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.45×** | +3.8 | 0.011 | 14/42 (RKO, LS 180, …) | all doses, flat | cell-cycle shift (explains ~12% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~41% of this change | **1.44×** | +3.7 | 0.014 | 14/42 (HOP62, SNU-1, …) | inconsistent across doses |  |
| [[Panobinostat (drug)]] 5 µM |  | **1.46×** | +3.7 | 0.014 | 15/42 (RKO, SK-MEL-2, …) | all doses, flat | cell-cycle shift (explains ~6% here) |
| [[Gefitinib (drug)]] 5 µM |  | **1.44×** | +3.5 | 0.021 | 16/42 (NCI-H460, C-33 A, …) | top dose only |  |
| [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **1.40×** | +3.4 | 0.031 | 17/41 (SK-MEL-2, C32, …) | rises with dose |  |
| [[Binimetinib (drug)]] 5 µM |  | **1.37×** | +3.3 | 0.046 | 16/43 (LoVo, RKO, …) | all doses, flat | noisy plate (z scaled) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~64% of this change | **1.40×** | +3.3 | 0.046 | 14/41 (SNU-1, HOP62, …) | rises with dose |  |
| [[Canagliflozin (hemihydrate) (drug)]] 5 µM |  | **1.38×** | +3.1 | 0.066 | 13/44 (SHP-77, SW 900, …) | top dose only |  |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.36×** | +3.1 | 0.068 | 16/42 (SK-MEL-2, RKO, …) | all doses, flat | cell-cycle shift (explains ~9% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 37 in all, 9 with an alert ⚠; shown: the 15 strongest and the 7 next strongest without an alert. 37 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 4072.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.332×** | -10.7 | 7e-24 | 32/41 (NCI-H1573, LOX-IMVI, …) | rises with dose | cell-cycle shift (explains ~13% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.373×** | -9.9 | 7e-21 | 32/42 (hTERT-HPNE, NCI-H1573, …) | rises with dose |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **0.595×** | -7.4 | 3e-11 | 33/43 (NCI-H1573, SK-MEL-2, …) | all doses, stronger at high dose |  |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **0.519×** | -6.6 | 5e-09 | 28/41 (NCI-H1573, MIA PaCa-2, …) | all doses, stronger at high dose |  |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~32% of this change | **0.532×** | -6.0 | 2e-07 | 24/42 (NCI-H1573, LOX-IMVI, …) | inconsistent across doses |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.577×** | -5.6 | 3e-06 | 26/42 (SW48, NCI-H460, …) | inconsistent across doses |  |
| [[Daptomycin (drug)]] 0.5 µM | ⚠ unreliable plate only | **0.615×** | -4.9 | 8e-05 | 22/41 (NCI-H1573, LoVo, …) | rises with dose |  |
| [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | **0.634×** | -4.6 | 3e-04 | 23/42 (NCI-H1573, LoVo, …) | rises with dose |  |
| [[Peretinoin (drug)]] 0.5 µM |  | **0.648×** | -4.4 | 8e-04 | 17/41 (NCI-H23, MIA PaCa-2, …) | rises with dose |  |
| [[Peretinoin (drug)]] 5 µM |  | **0.641×** | -4.3 | 9e-04 | 21/41 (NCI-H23, RPMI-7951, …) | rises with dose |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **0.666×** | -4.1 | 0.002 | 21/41 (SW 900, SW 1271, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.663×** | -4.0 | 0.003 | 19/39 (CHP-212, HepG2/C3A, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~92% of this change | **0.771×** | -3.7 | 0.008 | 20/42 (NCI-H1573, LoVo, …) | rises with dose | low cells (technical?) |
| [[Belzutifan (drug)]] 5 µM |  | **0.498×** | -3.7 | 0.008 | 14/40 (hTERT-HPNE, LOX-IMVI, …) | top dose only | noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **0.499×** | -3.7 | 0.008 | 18/41 (hTERT-HPNE, SW48, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Dexamethasone (drug)]] 5 µM |  | **0.685×** | -3.7 | 0.008 | 18/41 (NCI-H1573, SW 900, …) | all doses, flat |  |
| [[Bosentan (hydrate) (drug)]] 5 µM |  | **0.688×** | -3.6 | 0.009 | 16/41 (A-427, SW48, …) | top dose only |  |
| [[Dexamethasone (drug)]] 0.5 µM |  | **0.705×** | -3.5 | 0.013 | 18/41 (NCI-H1573, SHP-77, …) | all doses, flat |  |
| [[Vinblastine (sulfate) (drug)]] 0.05 µM |  | **0.709×** | -3.5 | 0.016 | 16/43 (MIA PaCa-2, SW48, …) | all doses, stronger at high dose |  |
| [[5-Azacytidine (drug)]] 5 µM |  | **0.702×** | -3.4 | 0.017 | 17/41 (NCI-H1573, NCI-H2030, …) | top dose only |  |
| [[Clobetasol propionate (drug)]] 0.5 µM |  | **0.722×** | -3.3 | 0.027 | 20/41 (NCI-H460, NCI-H1573, …) | inconsistent across doses |  |
| [[Pitavastatin (Calcium) (drug)]] 5 µM |  | **0.713×** | -3.3 | 0.027 | 14/41 (SW48, LoVo, …) | top dose only | cell-cycle shift (explains ~12% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.04 per unit of S-phase module lfc, +0.52 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4072. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H1573 (line)]] | alt | 180 | 1 | 9 (4 ⚠) | [[Harringtonine (drug)]] 5 µM 8.02× (z +13.2) | [[Ixazomib citrate (drug)]] 5 µM 0.0747× (z -16.4) |
| [[hTERT-HPNE (line)]] | wt | 178 | 0 | 7 (2 ⚠) | — | [[Ixazomib citrate (drug)]] 5 µM 0.0988× (z -13.0) |
| [[SK-MEL-2 (line)]] | alt | 30.3 | 5 (3 ⚠) | 1 | [[Homoharringtonine (drug)]] 5 µM 20.2× (z +19.5) ⚠ cell-cycle shift, explains ~31% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 20.4× (z +13.3) | [[Vinblastine (sulfate) (drug)]] 5 µM 0.270× (z -8.5) |
| [[SW48 (line)]] | wt | 107 | 0 | 6 (4 ⚠) | — | [[Ixazomib citrate (drug)]] 5 µM 0.0884× (z -10.6) |
| [[HOP62 (line)]] | alt | 33.0 | 4 (3 ⚠) | 1 | [[Homoharringtonine (drug)]] 5 µM 9.17× (z +16.6) ⚠ cell-cycle shift, explains ~31% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 9.21× (z +11.3) | [[Ixazomib citrate (drug)]] 5 µM 0.189× (z -8.5) |
| [[C32 (line)]] | wt | 43.4 | 4 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 9.44× (z +15.5) ⚠ cell-cycle shift, explains ~31% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 10.1× (z +10.9) | — |
| [[HS-578T (line)]] | alt | 18.3 | 4 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 8.61× (z +16.2) ⚠ cell-cycle shift, explains ~31% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 9.02× (z +11.2) | — |
| [[LOX-IMVI (line)]] | wt | 75.0 | 0 | 4 (2 ⚠) | — | [[Ixazomib citrate (drug)]] 5 µM 0.0916× (z -15.8) |
| [[NCI-H460 (line)]] | wt | 199 | 3 (2 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.45× (z +9.9) ⚠ cell-cycle shift, explains ~31% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 5.72× (z +9.5) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.329× (z -8.9) ⚠ cell-cycle shift, explains ~27% of this change |
| [[A-172 (line)]] | wt | 14.6 | 3 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 8.61× (z +14.9) ⚠ cell-cycle shift, explains ~31% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 13.6× (z +12.3) | — |
| [[HepG2_C3A (line)]] | wt | 20.9 | 0 | 3 (1 ⚠) | — | [[Glycyrrhizic acid (drug)]] 0.5 µM 0.0817× (z -10.5) |
| [[NCI-H23 (line)]] | alt | 137 | 1 (1 ⚠) | 2 (1 ⚠) | [[Adagrasib (drug)]] 0.05 µM 1.54× (z +8.6) ⚠ position not correctable | [[Homoharringtonine (drug)]] 0.5 µM 0.133× (z -11.0) ⚠ cell-cycle shift, explains ~43% of this change · without an alert: [[Peretinoin (drug)]] 5 µM 0.196× (z -8.5) |
| [[RPMI-7951 (line)]] | alt | 84.3 | 2 (1 ⚠) | 1 | [[Homoharringtonine (drug)]] 5 µM 6.00× (z +13.7) ⚠ cell-cycle shift, explains ~31% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 10.2× (z +12.1) | [[Ixazomib citrate (drug)]] 5 µM 0.0966× (z -12.1) |
| [[CHP-212 (line)]] | wt | 137 | 0 | 2 (2 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.0376× (z -12.9) ⚠ toxic |
| [[H4 (line)]] | wt | 37.1 | 0 | 2 (1 ⚠) | — | [[Betamethasone dipropionate (drug)]] 0.5 µM 0.0980× (z -9.4) |
| [[J82 (line)]] | alt | 16.7 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 9.02× (z +15.6) ⚠ cell-cycle shift, explains ~31% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 10.8× (z +11.5) | — |
| [[LoVo (line)]] | wt | 77.7 | 0 | 2 | — | [[Ixazomib citrate (drug)]] 0.5 µM 0.207× (z -9.0) |
| [[LS 180 (line)]] | wt | 15.8 | 1 (1 ⚠) | 1 | [[Homoharringtonine (drug)]] 5 µM 7.03× (z +10.8) ⚠ cell-cycle shift, explains ~31% of this change | [[Ixazomib citrate (drug)]] 5 µM 0.0854× (z -9.2) |
| [[NCI-H1792 (line)]] | alt | 30.1 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 11.5× (z +18.7) ⚠ cell-cycle shift, explains ~31% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 6.82× (z +10.0) | — |
| [[SW1417 (line)]] | alt | 15.9 | 1 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 7.87× (z +12.5) ⚠ cell-cycle shift, explains ~31% of this change | [[Dinaciclib (drug)]] 0.05 µM 0.113× (z -8.6) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[AsPC-1 (line)]] | alt | 18.8 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.99× (z +10.5) ⚠ cell-cycle shift, explains ~31% of this change | — |
| [[Hs 766T (line)]] | wt | 23.9 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.04× (z +10.5) ⚠ cell-cycle shift, explains ~31% of this change | — |
| [[SHP-77 (line)]] | alt | 57.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.153× (z -10.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[SNU-1 (line)]] | wt | 13.6 | 1 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 18.9× (z +8.7) ⚠ cell-cycle shift, explains ~33% of this change | — |
| [[SNU-423 (line)]] | alt | 33.9 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 7.89× (z +11.1) ⚠ cell-cycle shift, explains ~31% of this change | — |
| [[A-427 (line)]] | wt | 56.3 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 15.9 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 36.0 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 15.8 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 9.68 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 337 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 10.1 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 5.58 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 40.5 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 12.0 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 16.1 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 13.0 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 28.3 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 76.0 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 68.3 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 16.0 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 78.8 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 38.3 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 34.3 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 11.4 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 14.3 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 20.4 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 140 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 54.2 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 7.58 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4072), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*67 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NR4A2]] | +0.77 | +0.74 / +0.77 | both halves | 7e-06 | same gene group; pathway: HALLMARK_TNFA_SIGNALING_VIA_NFKB; STRING 842 |
| [[NR4A1]] | +0.72 | +0.69 / +0.78 | both halves | 7e-06 | same gene group; pathway: HALLMARK_TNFA_SIGNALING_VIA_NFKB; STRING 817 |
| [[HES1]] | +0.70 | +0.69 / +0.68 | both halves | 7e-06 | pathway: HALLMARK_TNFA_SIGNALING_VIA_NFKB |
| [[KLRK1]] | +0.65 | +0.53 / +0.66 | both halves | 1e-05 |  |
| [[PER2]] | +0.64 | +0.65 / +0.63 | both halves | 7e-06 |  |
| [[KLRC2]] | +0.64 | +0.55 / +0.62 | both halves | 1e-05 |  |
| [[CXXC4]] | +0.64 | +0.60 / +0.57 | both halves | 1e-05 |  |
| [[KLRC4-KLRK1]] | +0.62 | +0.52 / +0.62 | both halves | 1e-05 |  |
| [[KLRC3]] | +0.60 | +0.50 / +0.59 | both halves | 1e-05 |  |
| [[REL]] | +0.59 | +0.57 / +0.59 | both halves | 1e-05 | pathway: HALLMARK_TNFA_SIGNALING_VIA_NFKB |
| [[SNAP25]] | +0.58 | +0.55 / +0.56 | both halves | 1e-05 |  |
| [[TLE4]] | +0.58 | +0.58 / +0.53 | both halves | 1e-05 |  |

## Genes that move opposite

*33 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RTCA]] | -0.59 | -0.58 / -0.54 | both halves | 1e-05 |  |
| [[SVIL-AS1-1]] | -0.58 | -0.63 / -0.47 | both halves | 2e-05 |  |
| [[CLCC1]] | -0.54 | -0.55 / -0.53 | both halves | 1e-05 |  |
| [[POP1]] | -0.53 | -0.53 / -0.50 | both halves | 1e-05 |  |
| [[TOM1L1]] | -0.52 | -0.56 / -0.44 | both halves | 3e-05 |  |
| [[MRPS35]] | -0.52 | -0.56 / -0.38 | both halves | 7e-05 |  |
| [[EDEM2]] | -0.52 | -0.46 / -0.53 | both halves | 3e-05 |  |
| [[SNX4]] | -0.51 | -0.51 / -0.46 | both halves | 3e-05 |  |
| [[C8orf76]] | -0.51 | -0.58 / -0.47 | both halves | 2e-05 |  |
| [[SLC35D2]] | -0.51 | -0.56 / -0.43 | both halves | 3e-05 |  |
| [[ZDHHC6]] | -0.50 | -0.50 / -0.54 | both halves | 1e-05 |  |
| [[RNF14]] | -0.50 | -0.49 / -0.44 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[RSPO3]] | B | RSPO3 activity raises NR4A3's level | lines that do not express RSPO3 (39) vs lines expressing it (11) | 3.19× lower at baseline in the lines without RSPO3 | 0.011 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: SLC15A5, TBXT, GSG1L2 |
| [[HOMER2]] | B | HOMER2 activity lowers NR4A3's level | lines that do not express HOMER2 (11) vs lines expressing it (39) | 1.09× higher at baseline in the lines without HOMER2 | 0.049 | ⚠ within organs, on part of the lines; also absent: ZNF529-AS1, ZNF420, ENSG00000282381; maybe low, not absent |
| [[NPTX1]] | B | NPTX1 activity raises NR4A3's level | lines that do not express NPTX1 (25) vs lines expressing it (25) | 2.67× lower at baseline in the lines without NPTX1 | 0.091 | ⚠ within organs, on part of the lines; also absent: JAM3, SNAP91, CECR2 |

### Downstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CA8]] | B | NR4A3 activity lowers CA8's level | lines that do not express NR4A3 (6) vs lines expressing it (44) | 2.89× higher at baseline in the lines without NR4A3 | 0.022 | ⚠ within organs, on part of the lines; also absent: SLC4A7, SLC16A1; maybe low, not absent |
| [[CLCC1]] | B | NR4A3 activity raises CLCC1's level | lines that do not express NR4A3 (6) vs lines expressing it (44) | 1.33× lower at baseline in the lines without NR4A3 | 0.062 | ⚠ within organs, on part of the lines; also absent: SLC4A7, SLC16A1; maybe low, not absent |
| [[PSMF1]] | B | NR4A3 activity lowers PSMF1's level | lines that do not express NR4A3 (6) vs lines expressing it (44) | 1.22× higher at baseline in the lines without NR4A3 | 0.092 | ⚠ within organs, on part of the lines; also absent: SLC4A7, SLC16A1; maybe low, not absent |

## Where it sits

- **Module**: [[Module 223]]; 10 genes; every member is in the + arm (projection on the module's main direction 0.788). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (34.2, -0.1); signed map (6.7, 27.0). **Vector** length 131, 37.3% of its response variance represented; |z| ≥ 3 in 1,321 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | +6.2 | +16.1 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift | +6.2 | -1.0 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift | +5.7 | +0.4 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | +4.8 | -1.4 |
|  | [[Harringtonine (drug)]] 5 µM |  | +4.2 | +13.8 |
|  | [[Filgotinib (drug)]] 5 µM |  | +3.6 | +5.0 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +3.1 | +1.0 |
|  | [[Entrectinib (drug)]] 5 µM |  | +3.0 | +2.1 |
|  | [[Lactate (calcium) (drug)]] 5 µM |  | +2.6 | +2.6 |
|  | [[PF-06260933 (drug)]] 5 µM |  | +2.4 | +2.9 |
| fall | [[Ixazomib citrate (drug)]] 5 µM |  | -6.9 | -10.7 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~32% of this change | -6.5 | -6.0 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -6.5 | -7.4 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | -6.1 | -6.6 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -4.8 | -5.6 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -4.7 | -9.9 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | -4.5 | -2.6 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -4.4 | -3.5 |

## What is on record

|  |  |
|---|---|
| Name | nuclear receptor subfamily 4 group A member 3 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 9q31.1 — chr9:99,821,855-99,866,891 (+) |
| Ensembl biotype | protein_coding |
| Also known as | CSMF, CHN, NOR1, MINOR |
| Gene groups (HGNC) | Nuclear receptor subfamily 4 group A |
| Hallmark sets | TNFA_SIGNALING_VIA_NFKB |
| Reactome | 3 pathways, smallest: RUNX1 regulates genes involved in megakaryocyte differentiation and platelet function; Nuclear Receptor transcription pathway; Transcriptional regulation by RUNX1 |
| Matched by | ensembl_id |

**Function**, from UniProt [Q92570](https://www.uniprot.org/uniprotkb/Q92570) (Nuclear receptor subfamily 4 group A member 3):

> Transcriptional activator that binds to regulatory elements in promoter regions in a cell- and response element (target)-specific manner. Induces gene expression by binding as monomers to the NR4A1 response element (NBRE) 5'-AAAAGGTCA-3' site and as homodimers to the Nur response element (NurRE) site in the promoter of their regulated target genes (By similarity). Plays a role in the regulation of proliferation, survival and differentiation of many different cell types and also in metabolism …

**Summary**, from NCBI Gene [8013](https://www.ncbi.nlm.nih.gov/gene/8013):

> This gene encodes a member of the steroid-thyroid hormone-retinoid receptor superfamily. The encoded protein may act as a transcriptional activator. The protein can efficiently bind the NGFI-B Response Element (NBRE). Three different versions of extraskeletal myxoid chondrosarcomas (EMCs) are the result of reciprocal translocations between this gene and other genes. The translocation breakpoints are associated with Nuclear Receptor Subfamily 4, Group A, Member 3 (on chromosome 9) and either …

**Accessions** — [HGNC:7982](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:7982) · Entrez [8013](https://www.ncbi.nlm.nih.gov/gene/8013) · UniProt [Q92570](https://www.uniprot.org/uniprotkb/Q92570) · Ensembl [ENSG00000119508](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000119508)

## Data

Gene col 4072: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4072); `tables/drug_effects.parquet` (53 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4072, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4072]; `tensor/DDL_lfc|DDL_z.npy` [4072]; `embed/gene_vectors.npy` [4072]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4072 or target_col == 4072). Every well: [[NR4A3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/NR4A3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
