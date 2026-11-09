---
symbol: "USP37"
type: "gene"
col: 5775
ensembl_id: "ENSG00000135913"
name: "ubiquitin specific peptidase 37"
location: "2q35"
module: 164
arm: "+"
pooled_cpm: 146.83
n_lines_expressing: 50
n_dd_up: 9
n_dd_down: 21
n_dd_up_clean: 4
n_dd_down_clean: 15
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/164"]
generated_by: "tahoemap"
---

# USP37

*ubiquitin specific peptidase 37* — 2q35

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 9 drug-doses (5 with an alert ⚠); the strongest is [[TAK-901 (drug)]] 5 µM: 4.61× (z +13.0, q 1e-35, up in 44 of 49 measured lines).
> Pooled over the cell lines (median), lowered significantly by 21 drug-doses (6 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 0.416× (z -14.2, q 3e-43, down in 46 of 49 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Selinexor (drug)]] 5 µM: 0.748× (z -6.7, q 3e-09, down in 30 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SPICE1]] (+0.78, fdr 7e-06), [[WDR45B]] (+0.77, fdr 7e-06), [[INSIG2]] (+0.75, fdr 7e-06); moves opposite to [[FKRP]] (-0.59, fdr 1e-05), [[UBE2E3]] (-0.57, fdr 3e-05), [[TACC2]] (-0.57, fdr 2e-05).
> It is in [[Module 164]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 5 with an alert ⚠. 9 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5775.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[TAK-901 (drug)]] 5 µM |  | **4.61×** | +13.0 | 1e-35 | 44/49 (NCI-H23, COLO 205, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~3% here); composition shift; noisy plate (z scaled) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.43×** | +8.2 | 6e-14 | 30/49 (SW1417, LoVo, …) | rises with dose | cell-cycle shift (explains ~17% here) |
| [[PH-797804 (drug)]] 5 µM |  | **2.15×** | +6.5 | 2e-08 | 36/48 (HEC-1-A, SW480, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~42% of this change | **1.38×** | +5.2 | 3e-05 | 30/48 (SW480, Panc 03.27, …) | top dose only |  |
| [[PF-06260933 (drug)]] 5 µM |  | **1.67×** | +4.4 | 0.001 | 29/48 (SHP-77, SNU-423, …) | top dose only | noisy plate (z scaled) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~60% of this change | **1.31×** | +4.3 | 0.001 | 27/48 (SW480, Panc 03.27, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~55% of this change | **1.28×** | +4.0 | 0.005 | 29/48 (Panc 03.27, LoVo, …) | rises with dose |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~41% of this change | **1.28×** | +3.8 | 0.010 | 27/48 (SW48, A-427, …) | rises with dose |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~43% of this change | **1.24×** | +3.3 | 0.061 | 24/50 (SW48, RKO, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 30 in all, 9 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 21 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 5775.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.416×** | -14.2 | 3e-43 | 46/49 (SK-MEL-2, CFPAC-1, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.436×** | -12.9 | 8e-36 | 38/44 (SK-MEL-2, C32, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.446×** | -12.1 | 2e-31 | 41/45 (A-427, C32, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.651×** | -6.7 | 3e-09 | 37/47 (C32, NCI-H1792, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 5 µM |  | **0.748×** | -6.7 | 3e-09 | 30/48 (A-427, C32, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~8% here) |
| [[Belumosudil (drug)]] 5 µM |  | **0.684×** | -5.9 | 3e-07 | 38/48 (NCI-H1573, J82, …) | top dose only |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.691×** | -5.8 | 7e-07 | 33/47 (C32, SW 900, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.766×** | -4.2 | 0.002 | 27/48 (HEC-1-A, LOX-IMVI, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 0.848× | -3.8 | 0.009 | 20/48 (A498, A-172, …) | top dose only |  |
| [[Temsirolimus (drug)]] 0.05 µM |  | **0.792×** | -3.8 | 0.009 | 28/49 (PANC-1, RKO, …) | inconsistent across doses |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.798×** | -3.7 | 0.013 | 26/48 (HEC-1-A, C32, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Megestrol (drug)]] 0.05 µM |  | **0.799×** | -3.6 | 0.013 | 26/48 (LS 180, LOX-IMVI, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[vincristine (drug)]] 0.5 µM |  | **0.739×** | -3.5 | 0.019 | 26/48 (SW 900, SHP-77, …) | inconsistent across doses | low cells (technical?); noisy plate (z scaled) |
| [[Belzutifan (drug)]] 5 µM |  | **0.662×** | -3.5 | 0.019 | 29/47 (HEC-1-A, SK-MEL-2, …) | top dose only | noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 5 µM |  | 0.862× | -3.4 | 0.024 | 14/48 (LOX-IMVI, SW480, …) | rises with dose |  |
| [[Retinoic acid (drug)]] 0.05 µM |  | **0.811×** | -3.4 | 0.024 | 23/48 (LOX-IMVI, Hs 766T, …) | inconsistent across doses |  |
| [[Busulfan (drug)]] 0.05 µM |  | **0.815×** | -3.3 | 0.029 | 26/49 (MIA PaCa-2, SNU-423, …) | inconsistent across doses |  |
| [[Berbamine (drug)]] 0.05 µM |  | **0.818×** | -3.2 | 0.034 | 23/48 (LOX-IMVI, HS-578T, …) | inconsistent across doses |  |
| [[Palmatine (chloride) (drug)]] 0.05 µM |  | **0.821×** | -3.2 | 0.039 | 24/49 (CFPAC-1, NCI-H1792, …) | inconsistent across doses |  |
| [[Gallic acid (hydrate) (drug)]] 0.05 µM |  | **0.822×** | -3.2 | 0.041 | 23/48 (RPMI-7951, J82, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.26 per unit of S-phase module lfc, -0.05 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5775. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[C32 (line)]] | wt | 337 | 0 | 11 (7 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.178× (z -18.3) ⚠ toxic; transcription drop · without an alert: [[Selinexor (drug)]] 5 µM 0.412× (z -13.8) |
| [[HEC-1-A (line)]] | alt | 162 | 2 | 7 (5 ⚠) | [[TAK-901 (drug)]] 5 µM 4.74× (z +12.2) | [[Homoharringtonine (drug)]] 5 µM 0.512× (z -14.1) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.451× (z -11.5) |
| [[A498 (line)]] | wt | 113 | 0 | 7 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.415× (z -17.0) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM 0.614× (z -9.4) |
| [[LOX-IMVI (line)]] | wt | 152 | 1 | 6 (5 ⚠) | [[TAK-901 (drug)]] 5 µM 6.48× (z +9.8) | [[Homoharringtonine (drug)]] 5 µM 0.374× (z -13.9) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.319× (z -11.0) |
| [[NCI-H1792 (line)]] | alt | 194 | 1 | 6 (6 ⚠) | [[TAK-901 (drug)]] 5 µM 6.78× (z +9.8) | [[Homoharringtonine (drug)]] 5 µM 0.283× (z -17.6) ⚠ cell-cycle shift, explains ~0% of this change |
| [[AsPC-1 (line)]] | alt | 139 | 1 | 5 (5 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.73× (z +9.2) | [[Dinaciclib (drug)]] 0.5 µM 0.360× (z -12.3) ⚠ toxic; transcription drop |
| [[SW480 (line)]] | alt | 124 | 3 (1 ⚠) | 3 (3 ⚠) | [[TAK-901 (drug)]] 5 µM 5.24× (z +11.8) | [[Dinaciclib (drug)]] 5 µM 0.469× (z -9.9) ⚠ toxic; transcription drop |
| [[H4 (line)]] | wt | 209 | 2 (1 ⚠) | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.56× (z +10.7) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 8.05× (z +8.7) | [[Dinaciclib (drug)]] 0.5 µM 0.183× (z -13.5) ⚠ toxic; transcription drop |
| [[HOP62 (line)]] | alt | 184 | 2 | 3 (3 ⚠) | [[TAK-901 (drug)]] 5 µM 8.35× (z +10.2) | [[Dinaciclib (drug)]] 0.5 µM 0.274× (z -11.9) ⚠ toxic; transcription drop |
| [[HS-578T (line)]] | alt | 123 | 3 | 2 (2 ⚠) | [[TAK-901 (drug)]] 5 µM 7.18× (z +10.0) | [[Dinaciclib (drug)]] 0.05 µM 0.284× (z -11.3) ⚠ toxic; transcription drop |
| [[NCI-H2347 (line)]] | alt | 113 | 2 | 3 (2 ⚠) | [[TAK-901 (drug)]] 5 µM 3.94× (z +8.9) | [[Dinaciclib (drug)]] 0.5 µM 0.371× (z -12.3) ⚠ toxic; transcription drop · without an alert: [[Selinexor (drug)]] 5 µM 0.546× (z -10.6) |
| [[CFPAC-1 (line)]] | alt | 195 | 0 | 4 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.210× (z -17.9) ⚠ toxic; transcription drop |
| [[MIA PaCa-2 (line)]] | alt | 201 | 1 | 3 (3 ⚠) | [[TAK-901 (drug)]] 5 µM 6.09× (z +10.4) | [[Dinaciclib (drug)]] 0.5 µM 0.305× (z -13.1) ⚠ toxic; transcription drop |
| [[NCI-H2030 (line)]] | alt | 173 | 1 | 3 (3 ⚠) | [[TAK-901 (drug)]] 5 µM 4.12× (z +8.7) | [[Dinaciclib (drug)]] 0.05 µM 0.318× (z -12.4) ⚠ toxic; transcription drop |
| [[NCI-H460 (line)]] | wt | 184 | 1 | 3 (3 ⚠) | [[TAK-901 (drug)]] 5 µM 9.87× (z +12.5) | [[Dinaciclib (drug)]] 5 µM 0.243× (z -14.3) ⚠ toxic; transcription drop |
| [[Panc 03.27 (line)]] | alt | 99.5 | 2 (1 ⚠) | 2 (2 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.82× (z +10.0) | [[Dinaciclib (drug)]] 0.05 µM 0.381× (z -10.6) ⚠ toxic; transcription drop |
| [[SK-MEL-2 (line)]] | alt | 127 | 1 | 3 (3 ⚠) | [[TAK-901 (drug)]] 5 µM 5.39× (z +9.7) | [[Dinaciclib (drug)]] 5 µM 0.0801× (z -26.9) ⚠ toxic; transcription drop |
| [[SNU-423 (line)]] | alt | 224 | 0 | 4 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.221× (z -11.8) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 151 | 1 | 2 (2 ⚠) | [[TAK-901 (drug)]] 5 µM 6.82× (z +9.5) | [[Dinaciclib (drug)]] 0.5 µM 0.331× (z -10.4) ⚠ toxic; transcription drop |
| [[SHP-77 (line)]] | alt | 207 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.343× (z -12.9) ⚠ toxic; transcription drop |
| [[SW 900 (line)]] | alt | 159 | 1 (1 ⚠) | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.96× (z +9.7) ⚠ cell-cycle shift, explains ~0% of this change | [[Dinaciclib (drug)]] 0.05 µM 0.328× (z -10.5) ⚠ toxic; transcription drop |
| [[SW1417 (line)]] | alt | 108 | 2 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.16× (z +14.2) | [[Dinaciclib (drug)]] 0.5 µM 0.487× (z -9.3) ⚠ toxic; transcription drop |
| [[A-427 (line)]] | wt | 133 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.208× (z -16.6) ⚠ toxic; transcription drop · without an alert: [[Selinexor (drug)]] 5 µM 0.372× (z -16.0) |
| [[AN3 CA (line)]] | alt | 152 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.173× (z -12.7) ⚠ toxic; transcription drop |
| [[C-33 A (line)]] | alt | 229 | 1 | 1 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 5.50× (z +8.8) | [[Dinaciclib (drug)]] 0.5 µM 0.205× (z -15.7) ⚠ toxic; transcription drop |
| [[HCT15 (line)]] | alt | 258 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.329× (z -10.0) ⚠ toxic; transcription drop |
| [[HT-29 (line)]] | alt | 81.3 | 2 | 0 | [[TAK-901 (drug)]] 5 µM 5.83× (z +9.8) | — |
| [[KATO III (line)]] | alt | 95.4 | 2 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.94× (z +12.6) ⚠ cell-cycle shift, explains ~78% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 5.34× (z +10.2) | — |
| [[LoVo (line)]] | wt | 75.7 | 2 | 0 | [[TAK-901 (drug)]] 5 µM 9.39× (z +13.2) | — |
| [[LS 180 (line)]] | wt | 83.8 | 2 | 0 | [[TAK-901 (drug)]] 5 µM 6.45× (z +10.4) | — |
| [[NCI-H23 (line)]] | alt | 160 | 1 | 1 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 8.14× (z +13.7) | [[Dinaciclib (drug)]] 0.5 µM 0.323× (z -14.2) ⚠ toxic; transcription drop |
| [[RPMI-7951 (line)]] | alt | 182 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.261× (z -13.4) ⚠ toxic; transcription drop |
| [[SNU-1 (line)]] | wt | 123 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.399× (z -11.3) ⚠ cell-cycle shift, explains ~0% of this change |
| [[SW48 (line)]] | wt | 97.7 | 1 (1 ⚠) | 1 (1 ⚠) | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 4.03× (z +11.5) ⚠ cell-cycle shift, explains ~41% of this change | [[Dinaciclib (drug)]] 0.05 µM 0.304× (z -9.5) ⚠ toxic; transcription drop |
| [[A549 (line)]] | wt | 144 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 8.50× (z +9.0) | — |
| [[COLO 205 (line)]] | alt | 95.6 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 14.5× (z +13.2) | — |
| [[HepG2_C3A (line)]] | wt | 163 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.346× (z -9.1) ⚠ toxic; transcription drop |
| [[Hs 766T (line)]] | wt | 120 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.01× (z +8.6) | — |
| [[J82 (line)]] | alt | 135 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.397× (z -10.1) ⚠ toxic; transcription drop |
| [[NCI-H1573 (line)]] | alt | 135 | 0 | 1 | — | [[Belumosudil (drug)]] 5 µM 0.420× (z -8.9) |
| [[PANC-1 (line)]] | alt | 132 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 5.08× (z +9.4) | — |
| [[RKO (line)]] | wt | 123 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 7.36× (z +9.6) | — |
| [[SW 1088 (line)]] | alt | 174 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0521× (z -11.9) ⚠ toxic; transcription drop |
| [[BT-474 (line)]] | alt | 107 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 137 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 140 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 157 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 160 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 117 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 168 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5775), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*92 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SPICE1]] | +0.78 | +0.77 / +0.74 | both halves | 7e-06 |  |
| [[WDR45B]] | +0.77 | +0.77 / +0.72 | both halves | 7e-06 |  |
| [[INSIG2]] | +0.75 | +0.79 / +0.67 | both halves | 7e-06 |  |
| [[PEX3]] | +0.72 | +0.73 / +0.64 | both halves | 7e-06 |  |
| [[CABIN1]] | +0.72 | +0.74 / +0.68 | both halves | 7e-06 |  |
| [[PDK3]] | +0.69 | +0.72 / +0.65 | both halves | 7e-06 |  |
| [[RBPJ]] | +0.69 | +0.75 / +0.64 | both halves | 7e-06 |  |
| [[VKORC1]] | +0.69 | +0.67 / +0.63 | both halves | 7e-06 |  |
| [[PFKFB4]] | +0.68 | +0.70 / +0.66 | both halves | 7e-06 |  |
| [[CNOT8]] | +0.68 | +0.71 / +0.59 | both halves | 7e-06 |  |
| [[USP28]] | +0.67 | +0.60 / +0.61 | both halves | 7e-06 | same gene group; pathway: Deubiquitination; STRING 667 |
| [[SAP30-DT]] | +0.67 | +0.67 / +0.67 | both halves | 7e-06 |  |

## Genes that move opposite

*8 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[FKRP]] | -0.59 | -0.56 / -0.57 | both halves | 1e-05 |  |
| [[UBE2E3]] | -0.57 | -0.45 / -0.58 | both halves | 3e-05 |  |
| [[TACC2]] | -0.57 | -0.59 / -0.46 | both halves | 2e-05 |  |
| [[DNAH14]] | -0.56 | -0.59 / -0.51 | both halves | 1e-05 |  |
| [[KCNMB3]] | -0.56 | -0.53 / -0.55 | both halves | 1e-05 |  |
| [[SLC25A13]] | -0.55 | -0.55 / -0.46 | both halves | 3e-05 |  |
| [[CUEDC1]] | -0.55 | -0.47 / -0.47 | both halves | 2e-05 |  |
| [[DLG5]] | -0.55 | -0.47 / -0.46 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 1, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers USP37's level | compounds that target TOP2A: 3 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin) | 60% of the class's compounds vs 2.2% of all compounds | 0.059 | ⚠ off-target possible; 3 compounds; artifact flags |
| [[PFKFB4]] | C | PFKFB4's natural level strengthens USP37's drug response | PFKFB4's natural level across 49 lines (lineage-adjusted; a glimpse) | r +0.62, reverse +0.31; direction not clear | 0.084 | ⚠ tissue can mimic it; precision caveat; rises at some drug-doses, falls at others; direction unclear |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 164]]; 26 genes; every member is in the + arm (projection on the module's main direction 0.836). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.37; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (10.8, -17.3); signed map (-36.9, 23.4). **Vector** length 147, 54.1% of its response variance represented; |z| ≥ 3 in 1,136 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +7.9 | +8.2 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~43% of this change | +6.3 | +3.3 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~42% of this change | +6.1 | +5.2 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~41% of this change | +5.7 | +3.8 |
|  | [[TAK-901 (drug)]] 5 µM |  | +5.3 | +13.0 |
|  | [[PF-06260933 (drug)]] 5 µM |  | +3.9 | +4.4 |
|  | [[PH-797804 (drug)]] 5 µM |  | +3.2 | +6.5 |
|  | [[Terfenadine (drug)]] 5 µM |  | +3.0 | +2.7 |
|  | [[Verteporfin (drug)]] 5 µM |  | +2.9 | +2.7 |
|  | [[Silodosin (drug)]] 5 µM |  | +2.7 | +2.3 |
| fall | [[Selinexor (drug)]] 5 µM |  | -8.6 | -6.7 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -7.5 | -3.4 |
|  | [[Harringtonine (drug)]] 5 µM |  | -7.2 | -4.2 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | -7.1 | -6.7 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift | -6.4 | -2.4 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -4.9 | -3.4 |
|  | [[Belumosudil (drug)]] 5 µM |  | -4.4 | -5.9 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -4.1 | -1.3 |
|  | [[Rapamycin (drug)]] 5 µM |  | -4.0 | -3.0 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -4.0 | -2.3 |

## What is on record

|  |  |
|---|---|
| Name | ubiquitin specific peptidase 37 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 2q35 — chr2:218,450,251-218,568,351 (-) |
| Ensembl biotype | protein_coding |
| Also known as | KIAA1594 |
| Gene groups (HGNC) | Ubiquitin specific peptidases |
| Reactome | 2 pathways, smallest: Ub-specific processing proteases; Deubiquitination |
| Matched by | ensembl_id |

**Function**, from UniProt [Q86T82](https://www.uniprot.org/uniprotkb/Q86T82) (Ubiquitin carboxyl-terminal hydrolase 37):

> Deubiquitinase that plays a role in different processes including cell cycle regulation, DNA replication or DNA damage response. Antagonizes the anaphase-promoting complex (APC/C) during G1/S transition by mediating deubiquitination of cyclin-A (CCNA1 and CCNA2), thereby promoting S phase entry. Specifically mediates deubiquitination of 'Lys-11'-linked polyubiquitin chains, a specific ubiquitin-linkage type mediated by the APC/C complex. Phosphorylation at Ser-628 during G1/S phase maximizes …

**Summary**, from NCBI Gene [57695](https://www.ncbi.nlm.nih.gov/gene/57695):

> Enables cysteine-type deubiquitinase activity; cysteine-type endopeptidase activity; and protein kinase binding activity. Involved in G1/S transition of mitotic cell cycle; protein deubiquitination; and regulation of DNA replication. Located in nucleus. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:20063](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:20063) · Entrez [57695](https://www.ncbi.nlm.nih.gov/gene/57695) · UniProt [Q86T82](https://www.uniprot.org/uniprotkb/Q86T82) · Ensembl [ENSG00000135913](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000135913)

## Data

Gene col 5775: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5775); `tables/drug_effects.parquet` (39 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5775, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5775]; `tensor/DDL_lfc|DDL_z.npy` [5775]; `embed/gene_vectors.npy` [5775]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5775 or target_col == 5775). Every well: [[USP37 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/USP37.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
