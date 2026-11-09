---
symbol: "OS9"
type: "gene"
col: 5717
ensembl_id: "ENSG00000135506"
name: "OS9 endoplasmic reticulum lectin"
location: "12q13.3-q14.1"
module: 42
arm: "+"
pooled_cpm: 132.66
n_lines_expressing: 50
n_dd_up: 9
n_dd_down: 9
n_dd_up_clean: 6
n_dd_down_clean: 6
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/042"]
generated_by: "tahoemap"
---

# OS9

*OS9 endoplasmic reticulum lectin* — 12q13.3-q14.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 9 drug-doses (3 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 2.17× (z +17.5, q 0e+00, up in 47 of 49 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Panobinostat (drug)]] 5 µM: 1.62× (z +10.9, q 2e-25, up in 45 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 9 drug-doses (3 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.727× (z -9.0, q 2e-16, down in 38 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[FKBP8]] (+0.80, fdr 7e-06), [[NUCB1]] (+0.73, fdr 7e-06), [[CALR]] (+0.72, fdr 7e-06); moves opposite to [[BRIX1]] (-0.57, fdr 1e-05), [[NOP56]] (-0.57, fdr 1e-05), [[NIP7]] (-0.56, fdr 1e-05).
> It is in [[Module 042]], a single-armed module (UPR ER).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[HDAC6]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 7 with an alert ⚠. 9 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5717.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.17×** | +17.5 | 0e+00 | 47/49 (PANC-1, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.99×** | +14.9 | 0e+00 | 43/44 (HOP62, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.69×** | +11.0 | 1e-25 | 36/45 (NCI-H2030, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Panobinostat (drug)]] 5 µM |  | **1.62×** | +10.9 | 2e-25 | 45/48 (PANC-1, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.61×** | +10.7 | 1e-24 | 42/48 (PANC-1, LoVo, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM |  | **1.42×** | +7.9 | 3e-13 | 35/48 (LoVo, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.27×** | +6.7 | 1e-09 | 31/49 (HEC-1-A, NCI-H2347, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[TAK-901 (drug)]] 5 µM |  | **1.44×** | +4.3 | 0.001 | 28/49 (C32, SW480, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.21×** | +4.1 | 0.002 | 27/50 (HEC-1-A, Panc 03.27, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.05× | +4.1 | 0.003 | 1/50 (NCI-H23) | inconsistent across doses |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.18× | +3.5 | 0.021 | 21/48 (SNU-423, HEC-1-A, …) | top dose only |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~0% of this change | 1.17× | +3.5 | 0.021 | 19/48 (SW48, BT-474, …) | inconsistent across doses | low cells (technical?) |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~8% of this change | 1.16× | +3.4 | 0.029 | 18/48 (AsPC-1, SW480, …) | all doses, flat |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 1.14× | +3.2 | 0.050 | 17/48 (HOP62, A-172, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 5 with an alert ⚠. 9 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 5717.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.727×** | -9.0 | 2e-16 | 38/48 (AsPC-1, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here); composition shift |
| [[Verteporfin (drug)]] 5 µM |  | **0.672×** | -8.7 | 1e-15 | 44/49 (HepG2/C3A, J82, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.694×** | -8.3 | 2e-14 | 37/48 (AN3 CA, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.727×** | -6.9 | 6e-10 | 36/48 (KATO III, CFPAC-1, …) | rises with dose | cell-cycle shift (explains ~4% here); composition shift; position effect removed |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.775×** | -5.8 | 9e-07 | 34/48 (AN3 CA, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~2% here); position effect removed |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.793×** | -5.2 | 1e-05 | 28/48 (NCI-H460, MIA PaCa-2, …) | all doses, flat |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.796×** | -5.0 | 5e-05 | 26/47 (SNU-1, SW480, …) | top dose only | cell-cycle shift (explains ~3% here) |
| [[Carbidopa (monohydrate) (drug)]] 0.05 µM | ⚠ unreliable plate only; position not correctable | **0.821×** | -4.5 | 5e-04 | 31/49 (NCI-H2347, NCI-H2122, …) | inconsistent across doses |  |
| [[TAK-901 (drug)]] 0.05 µM |  | **0.826×** | -4.1 | 0.003 | 22/47 (C32, Panc 03.27, …) | inconsistent across doses |  |
| [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~5% of this change | 0.854× | -3.6 | 0.020 | 17/47 (A549, Hs 766T, …) | inconsistent across doses |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.873× | -3.1 | 0.10 | 14/48 (COLO 205, HOP62, …) | inconsistent across doses |  |
| [[Palmatine (chloride) (drug)]] 5 µM |  | 0.907× | -3.0 | 0.11 | 3/48 (H4, SNU-1, …) | inconsistent across doses |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | 0.876× | -3.0 | 0.11 | 20/48 (MIA PaCa-2, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Peretinoin (drug)]] 5 µM |  | 0.872× | -3.0 | 0.11 | 8/47 (A-427, NCI-H23, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.01 per unit of S-phase module lfc, -0.04 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5717. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A549 (line)]] | wt | 114 | 4 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 2.38× (z +11.7) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 5 µM 2.20× (z +10.7) | [[Verteporfin (drug)]] 5 µM 0.496× (z -9.2) |
| [[HS-578T (line)]] | alt | 170 | 3 (3 ⚠) | 2 | [[Dinaciclib (drug)]] 0.5 µM 2.49× (z +12.6) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.563× (z -10.1) |
| [[LoVo (line)]] | wt | 110 | 5 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.83× (z +12.5) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 5 µM 2.51× (z +11.5) | — |
| [[NCI-H1792 (line)]] | alt | 578 | 2 (2 ⚠) | 3 | [[Dinaciclib (drug)]] 0.5 µM 1.91× (z +11.0) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 0.5 µM 0.447× (z -13.8) |
| [[NCI-H460 (line)]] | wt | 150 | 4 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 2.51× (z +14.1) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 5 µM 1.77× (z +8.7) | [[Verteporfin (drug)]] 5 µM 0.523× (z -9.8) |
| [[PANC-1 (line)]] | alt | 128 | 5 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.65× (z +16.5) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 5 µM 2.00× (z +11.6) | — |
| [[SW480 (line)]] | alt | 102 | 5 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.20× (z +11.9) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 5 µM 2.15× (z +11.6) | — |
| [[HepG2_C3A (line)]] | wt | 155 | 2 (2 ⚠) | 2 | [[Dinaciclib (drug)]] 0.5 µM 2.23× (z +9.1) ⚠ toxic; transcription drop | [[Verteporfin (drug)]] 5 µM 0.392× (z -10.1) |
| [[J82 (line)]] | alt | 143 | 3 (3 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 2.34× (z +11.7) ⚠ toxic; transcription drop | [[Verteporfin (drug)]] 5 µM 0.496× (z -9.8) |
| [[MIA PaCa-2 (line)]] | alt | 72.2 | 4 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.63× (z +10.4) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 0.5 µM 2.29× (z +8.9) | — |
| [[SNU-423 (line)]] | alt | 141 | 3 (3 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 2.37× (z +11.2) ⚠ toxic; transcription drop | [[Verteporfin (drug)]] 5 µM 0.501× (z -8.6) |
| [[C32 (line)]] | wt | 149 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.52× (z +11.2) ⚠ toxic; transcription drop | — |
| [[CFPAC-1 (line)]] | alt | 133 | 1 (1 ⚠) | 2 | [[Dinaciclib (drug)]] 0.5 µM 1.85× (z +9.1) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.501× (z -12.8) |
| [[HEC-1-A (line)]] | alt | 81.2 | 3 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.68× (z +12.0) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.73× (z +8.5) | — |
| [[HOP62 (line)]] | alt | 123 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.06× (z +15.2) ⚠ toxic; transcription drop | — |
| [[NCI-H2030 (line)]] | alt | 125 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.44× (z +12.0) ⚠ toxic; transcription drop | — |
| [[Panc 03.27 (line)]] | alt | 155 | 2 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 2.16× (z +12.0) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 0.5 µM 0.573× (z -8.7) |
| [[RKO (line)]] | wt | 120 | 3 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.34× (z +10.0) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 0.5 µM 2.34× (z +10.0) | — |
| [[SHP-77 (line)]] | alt | 165 | 2 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 2.94× (z +14.7) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.545× (z -10.2) |
| [[A-427 (line)]] | wt | 128 | 2 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.68× (z +13.7) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 5 µM 2.12× (z +10.5) | — |
| [[A498 (line)]] | wt | 113 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.59× (z +14.1) ⚠ toxic; transcription drop | — |
| [[AsPC-1 (line)]] | alt | 99.0 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 2.06× (z +9.3) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.453× (z -13.0) |
| [[H4 (line)]] | wt | 117 | 0 | 2 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.277× (z -12.9) |
| [[KATO III (line)]] | alt | 127 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 2.34× (z +11.0) ⚠ toxic; transcription drop | [[Harringtonine (drug)]] 5 µM 0.471× (z -9.4) |
| [[LOX-IMVI (line)]] | wt | 123 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.25× (z +10.0) ⚠ toxic; transcription drop | — |
| [[NCI-H23 (line)]] | alt | 141 | 2 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.12× (z +9.7) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 5 µM 2.03× (z +9.1) | — |
| [[NCI-H2347 (line)]] | alt | 124 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.636× (z -9.0) |
| [[RPMI-7951 (line)]] | alt | 164 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.487× (z -12.6) |
| [[SK-MEL-2 (line)]] | alt | 106 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.96× (z +12.7) ⚠ toxic; transcription drop | — |
| [[SW1417 (line)]] | alt | 106 | 2 | 0 | [[Panobinostat (drug)]] 5 µM 2.06× (z +9.1) | — |
| [[A-172 (line)]] | wt | 107 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.04× (z +9.4) ⚠ toxic; transcription drop | — |
| [[AN3 CA (line)]] | alt | 132 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0876× (z -18.0) |
| [[hTERT-HPNE (line)]] | wt | 183 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.492× (z -8.5) |
| [[LS 180 (line)]] | wt | 132 | 1 | 0 | [[Panobinostat (drug)]] 0.5 µM 2.24× (z +9.1) | — |
| [[NCI-H1573 (line)]] | alt | 131 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.49× (z +11.8) ⚠ toxic; transcription drop | — |
| [[SNU-1 (line)]] | wt | 101 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.316× (z -9.5) ⚠ toxic |
| [[SW 1088 (line)]] | alt | 198 | 0 | 1 | — | [[Simotinib (drug)]] 0.05 µM 0.0923× (z -11.3) |
| [[SW 900 (line)]] | alt | 151 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.01× (z +9.0) ⚠ toxic; transcription drop | — |
| [[BT-474 (line)]] | alt | 93.0 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 57.6 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 106 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 162 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 122 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 93.8 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 117 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 139 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 128 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 151 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 126 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 93.8 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5717), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*87 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[FKBP8]] | +0.80 | +0.76 / +0.74 | both halves | 7e-06 |  |
| [[NUCB1]] | +0.73 | +0.71 / +0.70 | both halves | 7e-06 | STRING 683 |
| [[CALR]] | +0.72 | +0.77 / +0.59 | both halves | 7e-06 | pathway: Asparagine N-linked glycosylation; STRING 737 |
| [[LMAN2]] | +0.70 | +0.73 / +0.68 | both halves | 7e-06 | pathway: Asparagine N-linked glycosylation; STRING 526 |
| [[DDOST]] | +0.69 | +0.67 / +0.71 | both halves | 7e-06 | pathway: Asparagine N-linked glycosylation |
| [[CANX]] | +0.68 | +0.69 / +0.72 | both halves | 7e-06 | pathway: Asparagine N-linked glycosylation; STRING 958 |
| [[ALDH6A1]] | +0.67 | +0.65 / +0.62 | both halves | 7e-06 |  |
| [[GRN]] | +0.66 | +0.63 / +0.65 | both halves | 7e-06 |  |
| [[PSAP]] | +0.65 | +0.68 / +0.59 | both halves | 7e-06 |  |
| [[PRKCSH]] | +0.64 | +0.59 / +0.59 | both halves | 7e-06 | same gene group; pathway: Asparagine N-linked glycosylation; STRING 564 |
| [[HDAC6]] | +0.63 | +0.57 / +0.63 | both halves | 9e-06 |  |
| [[ATP6AP2]] | +0.63 | +0.54 / +0.64 | both halves | 1e-05 |  |

## Genes that move opposite

*13 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[BRIX1]] | -0.57 | -0.49 / -0.62 | both halves | 1e-05 |  |
| [[NOP56]] | -0.57 | -0.51 / -0.62 | both halves | 1e-05 |  |
| [[NIP7]] | -0.56 | -0.51 / -0.61 | both halves | 1e-05 |  |
| [[MRPS16]] | -0.55 | -0.58 / -0.48 | both halves | 2e-05 |  |
| [[TRIM47]] | -0.55 | -0.48 / -0.50 | both halves | 2e-05 |  |
| [[TP53RK]] | -0.55 | -0.42 / -0.57 | both halves | 4e-05 |  |
| [[TMEM70]] | -0.54 | -0.45 / -0.56 | both halves | 3e-05 |  |
| [[FJX1]] | -0.54 | -0.46 / -0.50 | both halves | 3e-05 |  |
| [[NDUFAF4]] | -0.53 | -0.56 / -0.50 | both halves | 1e-05 |  |
| [[CCDC137]] | -0.53 | -0.42 / -0.60 | both halves | 4e-05 |  |
| [[RPP25]] | -0.53 | -0.45 / -0.53 | both halves | 3e-05 |  |
| [[ERCC4]] | -0.53 | -0.45 / -0.56 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HDAC6]] | B | HDAC6 activity lowers OS9's level | compounds that target HDAC6: 2 of 2 raise it (Belinostat, Panobinostat) | 100% of the class's compounds vs 1.7% of all compounds | 0.084 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 042]] — UPR ER; 103 genes; every member is in the + arm (projection on the module's main direction 0.647). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.26; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-18.1, -20.2); signed map (-56.7, 5.6). **Vector** length 134, 42.0% of its response variance represented; |z| ≥ 3 in 949 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *UPR ER* (control, mean cos +0.56 to 11); *Maturation of DENV proteins* (reactome, mean cos +0.57 to 11); *Dengue Virus Genome Translation and Replication* (reactome, mean cos +0.57 to 12).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[TAK-901 (drug)]] 5 µM |  | +7.1 | +4.3 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | +5.6 | +10.7 |
|  | [[PH-797804 (drug)]] 5 µM |  | +4.8 | +2.8 |
|  | [[Panobinostat (drug)]] 5 µM |  | +4.7 | +10.9 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +4.0 | +14.9 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +2.7 | +2.2 |
|  | [[Bimiralisib (drug)]] 5 µM |  | +2.6 | +1.6 |
|  | [[Binimetinib (drug)]] 0.5 µM |  | +2.5 | +2.7 |
|  | [[Malotilate (drug)]] 0.05 µM |  | +2.3 | +0.8 |
| fall | [[Homoharringtonine (drug)]] 0.5 µM |  | -9.3 | -8.3 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | -8.0 | -9.0 |
|  | [[Harringtonine (drug)]] 5 µM |  | -7.3 | -6.9 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -7.1 | -5.8 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | -5.9 | -5.0 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -5.2 | -3.0 |
|  | [[Auranofin (drug)]] 5 µM |  | -3.8 | -0.6 |
|  | [[Peretinoin (drug)]] 5 µM |  | -3.7 | -3.0 |
|  | [[Verteporfin (drug)]] 5 µM |  | -3.5 | -8.7 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | -3.3 | -2.3 |

## What is on record

|  |  |
|---|---|
| Name | OS9 endoplasmic reticulum lectin |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 12q13.3-q14.1 — chr12:57,693,841-57,728,342 (+) |
| Ensembl biotype | protein_coding |
| Also known as | OS-9, ERLEC2 |
| Gene groups (HGNC) | MRH domain containing |
| Reactome | 20 pathways, smallest: ER Quality Control Compartment (ERQC); Calnexin/calreticulin cycle; N-glycan trimming in the ER and Calnexin/Calreticulin cycle |
| Matched by | ensembl_id |

**Function**, from UniProt [Q13438](https://www.uniprot.org/uniprotkb/Q13438) (Protein OS-9):

> Lectin component of the HRD1 complex, which functions in endoplasmic reticulum (ER) quality control and ER-associated degradation (ERAD). Specifically recognizes and binds improperly folded glycoproteins as well as hyperglycosylated proteins, retain them in the ER, and transfers them to the ubiquitination machinery and promote their degradation. Possible targets include TRPV4 as well as hyperglycosylated HSP90B1.

**Summary**, from NCBI Gene [10956](https://www.ncbi.nlm.nih.gov/gene/10956):

> This gene encodes a protein that is highly expressed in osteosarcomas. This protein binds to the hypoxia-inducible factor 1 (HIF-1), a key regulator of the hypoxic response and angiogenesis, and promotes the degradation of one of its subunits. Alternate transcriptional splice variants, encoding different isoforms, have been characterized. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:16994](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:16994) · Entrez [10956](https://www.ncbi.nlm.nih.gov/gene/10956) · UniProt [Q13438](https://www.uniprot.org/uniprotkb/Q13438) · Ensembl [ENSG00000135506](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000135506)

## Data

Gene col 5717: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5717); `tables/drug_effects.parquet` (28 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5717, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5717]; `tensor/DDL_lfc|DDL_z.npy` [5717]; `embed/gene_vectors.npy` [5717]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5717 or target_col == 5717). Every well: [[OS9 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/OS9.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
