---
symbol: "LDLR"
type: "gene"
col: 5027
ensembl_id: "ENSG00000130164"
name: "low density lipoprotein receptor"
location: "19p13.2"
module: 86
arm: "+"
pooled_cpm: 131.12
n_lines_expressing: 48
n_dd_up: 27
n_dd_down: 51
n_dd_up_clean: 23
n_dd_down_clean: 44
in_vector_space: true
direction_upstream: 3
direction_downstream: 0
tags: ["gene", "module/086"]
generated_by: "tahoemap"
---

# LDLR

*low density lipoprotein receptor* — 19p13.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 27 drug-doses (4 with an alert ⚠); the strongest is [[Cepharanthine (drug)]] 5 µM: 2.02× (z +13.5, q 2e-38, up in 46 of 46 measured lines).
> Pooled over the cell lines (median), lowered significantly by 51 drug-doses (7 with an alert ⚠); the strongest is [[Topotecan (hydrochloride) (drug)]] 5 µM: 0.441× (z -10.9, q 8e-25, down in 41 of 45 measured lines) ⚠ toxic. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.598× (z -9.7, q 6e-20, down in 38 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[IDI1]] (+0.71, fdr 7e-06), [[LIPG]] (+0.71, fdr 7e-06), [[HMGCS1]] (+0.68, fdr 7e-06); moves opposite to [[CEPT1]] (-0.50, fdr 3e-05), [[PHC3]] (-0.48, fdr 4e-05), [[FHIP2A]] (-0.47, fdr 1e-04).
> It is in [[Module 086]], a single-armed module (cholesterol synthesis).
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 29 in all, 4 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 27 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5027.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Cepharanthine (drug)]] 5 µM |  | **2.02×** | +13.5 | 2e-38 | 46/46 (NCI-H23, HOP62, …) | top dose only |  |
| [[Berbamine (drug)]] 5 µM |  | **1.72×** | +10.3 | 1e-22 | 43/47 (NCI-H23, HOP62, …) | rises with dose |  |
| [[TAK-901 (drug)]] 5 µM |  | **3.90×** | +9.9 | 1e-20 | 41/47 (AsPC-1, NCI-H1573, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Posaconazole (drug)]] 5 µM |  | **1.63×** | +6.5 | 1e-08 | 37/46 (HEC-1-A, HOP62, …) | top dose only | plate-row cell shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.58×** | +6.4 | 2e-08 | 35/46 (A-172, SNU-1, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[(S)-Crizotinib (drug)]] 5 µM |  | **1.58×** | +6.1 | 9e-08 | 38/46 (HOP62, H4, …) | top dose only |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.55×** | +5.7 | 9e-07 | 27/46 (NCI-H2347, HCT15, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | **1.49×** | +5.6 | 2e-06 | 28/45 (SW48, SK-MEL-2, …) | two highest doses | low cells (technical?); position effect removed |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **2.12×** | +5.5 | 3e-06 | 31/43 (NCI-H2347, Panc 03.27, …) | all doses, flat | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Berbamine (dihydrochloride) (drug)]] 5 µM |  | **1.50×** | +5.4 | 3e-06 | 36/46 (HEC-1-A, SNU-423, …) | top dose only | plate-row cell shift |
| [[Entrectinib (drug)]] 5 µM |  | **1.42×** | +4.9 | 5e-05 | 29/46 (H4, HOP62, …) | top dose only |  |
| [[GSK1059615 (drug)]] 5 µM |  | **1.91×** | +4.7 | 1e-04 | 28/47 (MIA PaCa-2, SHP-77, …) | top dose only | plate-row cell shift; noisy plate (z scaled); position effect removed |
| [[Almonertinib (mesylate) (drug)]] 5 µM |  | **1.42×** | +4.7 | 1e-04 | 27/47 (HOP62, H4, …) | top dose only | plate-row cell shift |
| [[Adagrasib (drug)]] 5 µM |  | **1.41×** | +4.5 | 2e-04 | 24/46 (H4, HOP62, …) | top dose only |  |
| [[Ritonavir (drug)]] 5 µM |  | **1.26×** | +4.4 | 4e-04 | 25/46 (PANC-1, HEC-1-A, …) | top dose only | position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.34×** | +4.1 | 0.002 | 25/46 (SNU-1, A-172, …) | rises with dose | cell-cycle shift (explains ~0% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 54 in all, 7 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 51 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 5027.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.441×** | -10.9 | 8e-25 | 41/45 (H4, KATO III, …) | rises with dose | cell-cycle shift (explains ~10% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.598×** | -9.7 | 6e-20 | 38/47 (HT-29, PANC-1, …) | rises with dose | cell-cycle shift (explains ~10% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.517×** | -8.8 | 3e-16 | 38/46 (HT-29, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~12% here) |
| [[Belumosudil (drug)]] 5 µM |  | **0.579×** | -7.3 | 5e-11 | 33/46 (NCI-H23, HCT15, …) | top dose only |  |
| [[Panobinostat (drug)]] 5 µM |  | **0.604×** | -7.0 | 4e-10 | 32/46 (SK-MEL-2, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here) |
| [[Selinexor (drug)]] 5 µM |  | **0.696×** | -6.9 | 5e-10 | 33/46 (SK-MEL-2, A549, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~5% here) |
| [[Trametinib (drug)]] 5 µM |  | **0.602×** | -6.9 | 5e-10 | 37/48 (SK-MEL-2, SW48, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.609×** | -6.8 | 5e-10 | 30/46 (SNU-423, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Harringtonine (drug)]] 5 µM |  | **0.607×** | -6.6 | 2e-09 | 31/46 (SW480, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.620×** | -6.6 | 2e-09 | 31/46 (SK-MEL-2, BT-474, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.624×** | -6.3 | 2e-08 | 31/48 (HT-29, LS 180, …) | top dose only | cell-cycle shift (explains ~14% here) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **0.633×** | -6.1 | 6e-08 | 35/46 (SW480, SK-MEL-2, …) | all doses, stronger at high dose |  |
| [[Trametinib (drug)]] 0.5 µM |  | **0.697×** | -5.9 | 2e-07 | 31/46 (SW480, LoVo, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.742×** | -5.7 | 6e-07 | 26/46 (KATO III, LS 180, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.665×** | -5.6 | 6e-07 | 28/46 (PANC-1, RKO, …) | all doses, flat |  |
| [[Belinostat (drug)]] 5 µM |  | **0.674×** | -5.5 | 2e-06 | 29/46 (SK-MEL-2, HT-29, …) | rises with dose | cell-cycle shift (explains ~22% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.21 per unit of S-phase module lfc, +0.14 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5027. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LoVo (line)]] | wt | 183 | 2 | 16 (4 ⚠) | [[Cepharanthine (drug)]] 5 µM 2.57× (z +12.3) | [[Dinaciclib (drug)]] 5 µM 0.256× (z -12.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change · without an alert: [[Trametinib (drug)]] 5 µM 0.304× (z -12.1) |
| [[SW480 (line)]] | alt | 135 | 0 | 17 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.358× (z -12.7) |
| [[SK-MEL-2 (line)]] | alt | 106 | 2 | 14 | [[Cepharanthine (drug)]] 5 µM 2.41× (z +9.8) | [[Trametinib (drug)]] 5 µM 0.192× (z -14.0) |
| [[HT-29 (line)]] | alt | 201 | 0 | 12 (4 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.245× (z -17.2) |
| [[KATO III (line)]] | alt | 237 | 0 | 11 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.153× (z -22.2) |
| [[LS 180 (line)]] | wt | 249 | 1 | 9 (3 ⚠) | [[Cepharanthine (drug)]] 5 µM 2.34× (z +9.3) | [[Dinaciclib (drug)]] 5 µM 0.129× (z -15.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.295× (z -13.4) |
| [[SW48 (line)]] | wt | 163 | 1 | 6 (2 ⚠) | [[Pitavastatin (Calcium) (drug)]] 0.5 µM 2.94× (z +8.6) | [[Trametinib (drug)]] 5 µM 0.184× (z -12.7) |
| [[AsPC-1 (line)]] | alt | 206 | 3 | 3 (2 ⚠) | [[TAK-901 (drug)]] 5 µM 9.48× (z +12.1) | [[Dinaciclib (drug)]] 5 µM 0.305× (z -11.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.370× (z -10.2) |
| [[MIA PaCa-2 (line)]] | alt | 165 | 1 | 5 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 9.95× (z +11.2) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.387× (z -12.0) |
| [[NCI-H23 (line)]] | alt | 83.3 | 2 | 4 | [[Cepharanthine (drug)]] 5 µM 3.54× (z +14.5) | [[Panobinostat (drug)]] 5 µM 0.237× (z -11.9) |
| [[SNU-1 (line)]] | wt | 88.6 | 6 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 4.39× (z +10.2) | — |
| [[COLO 205 (line)]] | alt | 260 | 0 | 5 (1 ⚠) | — | [[Belinostat (drug)]] 5 µM 0.217× (z -9.8) |
| [[HEC-1-A (line)]] | alt | 101 | 3 | 2 | [[Berbamine (drug)]] 5 µM 2.34× (z +9.9) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.435× (z -9.8) |
| [[SNU-423 (line)]] | alt | 119 | 2 | 3 (1 ⚠) | [[Cepharanthine (drug)]] 5 µM 4.18× (z +12.4) | [[Selinexor (drug)]] 5 µM 0.300× (z -10.4) |
| [[A-172 (line)]] | wt | 92.5 | 4 (2 ⚠) | 0 | [[Niclosamide (olamine) (drug)]] 5 µM 3.68× (z +10.0) ⚠ toxic · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 3.45× (z +9.9) | — |
| [[A549 (line)]] | wt | 110 | 3 | 1 | [[Cepharanthine (drug)]] 5 µM 2.64× (z +10.9) | [[Selinexor (drug)]] 5 µM 0.344× (z -11.9) |
| [[BT-474 (line)]] | alt | 448 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.321× (z -13.1) |
| [[HCT15 (line)]] | alt | 295 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.223× (z -13.1) |
| [[Hs 766T (line)]] | wt | 425 | 0 | 4 (4 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.171× (z -13.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change |
| [[NCI-H2347 (line)]] | alt | 72.6 | 4 (1 ⚠) | 0 | [[TAK-901 (drug)]] 5 µM 8.50× (z +10.5) | — |
| [[Panc 03.27 (line)]] | alt | 125 | 3 | 1 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 10.1× (z +11.1) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.274× (z -11.3) ⚠ toxic |
| [[PANC-1 (line)]] | alt | 142 | 0 | 4 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.321× (z -14.4) |
| [[H4 (line)]] | wt | 82.0 | 2 | 1 (1 ⚠) | [[Cepharanthine (drug)]] 5 µM 3.69× (z +11.5) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.120× (z -13.0) ⚠ toxic |
| [[NCI-H1573 (line)]] | alt | 86.3 | 1 | 2 | [[TAK-901 (drug)]] 5 µM 17.4× (z +11.9) | [[Panobinostat (drug)]] 5 µM 0.329× (z -8.9) |
| [[NCI-H2030 (line)]] | alt | 120 | 1 | 2 (1 ⚠) | [[Cepharanthine (drug)]] 5 µM 2.58× (z +11.0) | [[Homoharringtonine (drug)]] 5 µM 0.389× (z -10.8) |
| [[RPMI-7951 (line)]] | alt | 94.5 | 0 | 3 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.218× (z -10.6) |
| [[SW 900 (line)]] | alt | 115 | 2 | 1 (1 ⚠) | [[Cepharanthine (drug)]] 5 µM 2.39× (z +10.7) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.271× (z -11.0) ⚠ toxic |
| [[A498 (line)]] | wt | 159 | 0 | 2 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.431× (z -12.3) |
| [[C-33 A (line)]] | alt | 35.0 | 2 | 0 | [[Cepharanthine (drug)]] 5 µM 3.67× (z +9.9) | — |
| [[HepG2_C3A (line)]] | wt | 195 | 0 | 2 | — | [[Panobinostat (drug)]] 0.5 µM 0.306× (z -10.7) |
| [[HOP62 (line)]] | alt | 67.8 | 2 | 0 | [[Cepharanthine (drug)]] 5 µM 3.99× (z +14.3) | — |
| [[HS-578T (line)]] | alt | 40.4 | 2 | 0 | [[Cepharanthine (drug)]] 5 µM 3.35× (z +10.7) | — |
| [[AN3 CA (line)]] | alt | 57.8 | 0 | 1 | — | [[Harringtonine (drug)]] 5 µM 0.0970× (z -9.9) |
| [[hTERT-HPNE (line)]] | wt | 74.4 | 1 | 0 | [[Cepharanthine (drug)]] 5 µM 3.15× (z +9.3) | — |
| [[NCI-H460 (line)]] | wt | 65.9 | 1 | 0 | [[Chlorhexidine (diacetate) (drug)]] 5 µM 2.61× (z +9.6) | — |
| [[RKO (line)]] | wt | 126 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.405× (z -8.7) |
| [[SHP-77 (line)]] | alt | 112 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.310× (z -9.5) ⚠ toxic |
| [[A-427 (line)]] | wt | 12.4 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 16.3 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 133 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 53.6 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 37.8 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 55.7 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 134 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 121 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 109 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 40.1 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 57.9 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 171 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 109 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5027), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*84 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[IDI1]] | +0.71 | +0.68 / +0.68 | both halves | 7e-06 | pathway: HALLMARK_CHOLESTEROL_HOMEOSTASIS |
| [[LIPG]] | +0.71 | +0.71 / +0.67 | both halves | 7e-06 | pathway: Plasma lipoprotein assembly, remodeling, and clearance |
| [[HMGCS1]] | +0.68 | +0.66 / +0.68 | both halves | 7e-06 | pathway: HALLMARK_CHOLESTEROL_HOMEOSTASIS; STRING 699 |
| [[HMGCR]] | +0.66 | +0.67 / +0.62 | both halves | 7e-06 | pathway: HALLMARK_CHOLESTEROL_HOMEOSTASIS |
| [[DHCR7]] | +0.66 | +0.70 / +0.58 | both halves | 7e-06 | pathway: HALLMARK_CHOLESTEROL_HOMEOSTASIS |
| [[LPIN1]] | +0.63 | +0.62 / +0.57 | both halves | 1e-05 | same gene group |
| [[ADIPOR2]] | +0.63 | +0.68 / +0.56 | both halves | 1e-05 | pathway: HALLMARK_MTORC1_SIGNALING |
| [[NPC1]] | +0.62 | +0.61 / +0.60 | both halves | 7e-06 | pathway: LDL clearance |
| [[EBP]] | +0.61 | +0.67 / +0.47 | both halves | 2e-05 | pathway: HALLMARK_CHOLESTEROL_HOMEOSTASIS |
| [[PCSK9]] | +0.61 | +0.65 / +0.53 | both halves | 1e-05 | pathway: LDL clearance; STRING 999 |
| [[MSMO1]] | +0.60 | +0.63 / +0.57 | both halves | 1e-05 |  |
| [[FDPS]] | +0.60 | +0.67 / +0.53 | both halves | 1e-05 | pathway: HALLMARK_CHOLESTEROL_HOMEOSTASIS; STRING 402 |

## Genes that move opposite

*16 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CEPT1]] | -0.50 | -0.53 / -0.43 | both halves | 3e-05 |  |
| [[PHC3]] | -0.48 | -0.50 / -0.42 | both halves | 4e-05 |  |
| [[FHIP2A]] | -0.47 | -0.33 / -0.43 | both halves | 1e-04 |  |
| [[FBXW4]] | -0.47 | -0.43 / -0.49 | both halves | 4e-05 |  |
| [[RWDD3]] | -0.47 | -0.41 / -0.46 | both halves | 4e-05 |  |
| [[NFYB]] | -0.46 | -0.51 / -0.39 | both halves | 6e-05 |  |
| [[TSR2]] | -0.46 | -0.45 / -0.40 | both halves | 5e-05 |  |
| [[DCP1B]] | -0.45 | -0.47 / -0.40 | both halves | 5e-05 |  |
| [[WHAMMP3]] | -0.45 | -0.41 / -0.34 | both halves | 1e-04 |  |
| [[ZDHHC17]] | -0.44 | -0.40 / -0.39 | both halves | 5e-05 |  |
| [[ACTR10]] | -0.42 | -0.36 / -0.49 | both halves | 9e-05 |  |
| [[ZFR]] | -0.42 | -0.46 / -0.34 | both halves | 1e-04 | same gene group |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity raises LDLR's level | compounds that target TOP2A: 5 of 5 lower it (Amsacrine, Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 100% of the class's compounds vs 8.4% of all compounds | 0.015 | ⚠ off-target possible; 5 compounds; artifact flags |
| [[TRIB1]] | B | TRIB1 activity raises LDLR's level | lines that do not express TRIB1 (6) vs lines expressing it (44) | 2.29× lower at baseline in the lines without TRIB1 | 0.025 | ⚠ within organs, on part of the lines; also absent: TGFBR2, VDR, PLSCR2; maybe low, not absent |
| [[SHB]] | B | SHB activity raises LDLR's level | lines that do not express SHB (5) vs lines expressing it (45) | 3.83× lower at baseline in the lines without SHB | 0.060 | ⚠ within organs, on part of the lines; also absent: SLC2A1, NIBAN2, IER3; maybe low, not absent; its own permutation p |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 086]] — cholesterol synthesis; 51 genes; every member is in the + arm (projection on the module's main direction 0.691). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (20.9, -48.8); signed map (-51.8, 33.1). **Vector** length 144, 52.0% of its response variance represented; |z| ≥ 3 in 1,928 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *Cholesterol biosynthesis* (reactome, mean cos +0.53 to 20); *Metabolism of steroids* (reactome, mean cos +0.54 to 25); *Regulation of cholesterol biosynthesis by SREBP (SREBF)* (reactome, mean cos +0.54 to 17).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Cepharanthine (drug)]] 5 µM |  | +10.0 | +13.5 |
|  | [[Berbamine (drug)]] 5 µM |  | +8.5 | +10.3 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +6.1 | +1.1 |
|  | [[Entrectinib (drug)]] 5 µM |  | +5.9 | +4.9 |
|  | [[Berbamine (dihydrochloride) (drug)]] 5 µM |  | +5.8 | +5.4 |
| fall | [[Homoharringtonine (drug)]] 0.05 µM |  | -6.7 | -5.6 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -6.7 | -6.8 |
|  | [[Trametinib (drug)]] 5 µM |  | -5.7 | -6.9 |
|  | [[Radotinib (drug)]] 5 µM |  | -5.1 | -4.5 |
|  | [[Belumosudil (drug)]] 5 µM |  | -4.6 | -7.3 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -4.4 | -5.9 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -4.2 | -4.5 |

## What is on record

|  |  |
|---|---|
| Name | low density lipoprotein receptor |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 19p13.2 — chr19:11,089,418-11,133,820 (+) |
| Ensembl biotype | protein_coding |
| Also known as | LDLCQ2 |
| Gene groups (HGNC) | Low density lipoprotein receptors; MicroRNA protein coding host genes |
| Hallmark sets | CHOLESTEROL_HOMEOSTASIS, INFLAMMATORY_RESPONSE, UV_RESPONSE_DN, TNFA_SIGNALING_VIA_NFKB, MTORC1_SIGNALING |
| Reactome | 14 pathways, smallest: Chylomicron clearance; LDL clearance; Retinoid metabolism and transport |
| Matched by | ensembl_id |

**Function**, from UniProt [P01130](https://www.uniprot.org/uniprotkb/P01130) (Low-density lipoprotein receptor):

> Binds low density lipoprotein /LDL, the major cholesterol-carrying lipoprotein of plasma, and transports it into cells by endocytosis. In order to be internalized, the receptor-ligand complexes must first cluster into clathrin-coated pits. Forms a ternary complex with PGRMC1 and TMEM97 receptors which increases LDLR-mediated LDL internalization.; (Microbial infection) Acts as a receptor for hepatitis C virus in hepatocytes, but not through a direct interaction with viral proteins.; (Microbial …

**Summary**, from NCBI Gene [3949](https://www.ncbi.nlm.nih.gov/gene/3949):

> The low density lipoprotein receptor (LDLR) gene family consists of cell surface proteins involved in receptor-mediated endocytosis of specific ligands. The encoded protein is normally bound at the cell membrane, where it binds low density lipoprotein/cholesterol and is taken into the cell. Lysosomes release the cholesterol, which is made available for repression of microsomal enzyme 3-hydroxy-3-methylglutaryl coenzyme A (HMG CoA) reductase, the rate-limiting step in cholesterol synthesis. At …

**Accessions** — [HGNC:6547](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:6547) · Entrez [3949](https://www.ncbi.nlm.nih.gov/gene/3949) · UniProt [P01130](https://www.uniprot.org/uniprotkb/P01130) · Ensembl [ENSG00000130164](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000130164)

## Data

Gene col 5027: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5027); `tables/drug_effects.parquet` (83 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5027, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5027]; `tensor/DDL_lfc|DDL_z.npy` [5027]; `embed/gene_vectors.npy` [5027]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5027 or target_col == 5027). Every well: [[LDLR — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/LDLR.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
