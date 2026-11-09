---
symbol: "GRIP1"
type: "gene"
col: 7936
ensembl_id: "ENSG00000155974"
name: "glutamate receptor interacting protein 1"
location: "12q14.3"
module: 137
arm: "+"
pooled_cpm: 96.49
n_lines_expressing: 37
n_dd_up: 34
n_dd_down: 18
n_dd_up_clean: 26
n_dd_down_clean: 12
in_vector_space: true
direction_upstream: 6
direction_downstream: 4
tags: ["gene", "module/137"]
generated_by: "tahoemap"
---

# GRIP1

*glutamate receptor interacting protein 1* — 12q14.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 34 drug-doses (8 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 1.64× (z +11.1, q 8e-26, up in 18 of 35 measured lines).
> Pooled over the cell lines (median), lowered significantly by 18 drug-doses (6 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 0.5 µM: 0.252× (z -22.0, q 0e+00, down in 35 of 35 measured lines).
> Its strongest partners by |cos| (88 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 12 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SLC25A21]] (+0.79, fdr 7e-06), [[PARD3B]] (+0.70, fdr 7e-06), [[TMEM117]] (+0.68, fdr 1e-05); moves opposite to [[IFT172]] (-0.67, fdr 1e-05), [[POT1]] (-0.65, fdr 4e-05), [[FHIP1B]] (-0.62, fdr 2e-05).
> It sits in the **+** arm of [[Module 137]].
> Probable direction (from the cell lines, not proof of direct regulation): 6 arrows point to it, the strongest [[L3MBTL4]] → it (grade B ⚠); 4 go from it, the strongest it → [[STPG2]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 40 in all, 9 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 34 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7936.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **1.64×** | +11.1 | 8e-26 | 18/35 (J82, BT-474, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~41% of this change | **1.58×** | +10.4 | 1e-22 | 32/35 (SW1417, HEC-1-A, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.58×** | +10.3 | 1e-22 | 23/36 (NCI-H460, H4, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.65×** | +7.7 | 2e-12 | 27/34 (NCI-H460, H4, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | **1.64×** | +7.6 | 4e-12 | 21/35 (H4, J82, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.59×** | +7.4 | 2e-11 | 24/35 (NCI-H1792, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.38×** | +7.2 | 4e-11 | 22/35 (HEC-1-A, A498, …) | top dose only |  |
| [[Cobimetinib (drug)]] 5 µM |  | **1.49×** | +6.1 | 7e-08 | 27/34 (HEC-1-A, A498, …) | rises with dose |  |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~70% of this change | **1.41×** | +5.5 | 2e-06 | 25/35 (HEC-1-A, NCI-H1792, …) | all doses, stronger at high dose |  |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **1.93×** | +5.5 | 2e-06 | 23/32 (HEC-1-A, HT-29, …) | inconsistent across doses | cell-cycle shift (explains ~23% here); noisy plate (z scaled) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.35×** | +4.6 | 3e-04 | 17/37 (NCI-H460, H4, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[5-Azacytidine (drug)]] 5 µM |  | **1.32×** | +4.4 | 5e-04 | 21/34 (HEC-1-A, LOX-IMVI, …) | top dose only |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.37×** | +4.1 | 0.002 | 17/35 (SW1417, SW 900, …) | rises with dose | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Bimiralisib (drug)]] 5 µM |  | **1.61×** | +4.0 | 0.003 | 17/37 (A-427, J82, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.28×** | +3.9 | 0.004 | 15/35 (HEC-1-A, A498, …) | inconsistent across doses |  |
| [[Cobimetinib (drug)]] 0.5 µM |  | **1.35×** | +3.9 | 0.004 | 18/34 (J82, A498, …) | rises with dose | noisy plate (z scaled) |
| [[Neratinib (maleate) (drug)]] 5 µM |  | 1.19× | +3.8 | 0.004 | 14/35 (NCI-H460, CFPAC-1, …) | rises with dose |  |
| [[Rapamycin (drug)]] 5 µM |  | 1.17× | +3.6 | 0.009 | 10/35 (NCI-H1573, SW1417, …) | rises with dose |  |
| [[Benztropine (mesylate) (drug)]] 0.05 µM |  | **1.25×** | +3.6 | 0.009 | 18/35 (HCT15, J82, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 20 in all, 6 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 18 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 7936.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 0.5 µM |  | **0.252×** | -22.0 | 0e+00 | 35/35 (HEC-1-A, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.260×** | -21.4 | 0e+00 | 34/35 (NCI-H1573, SNU-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.275×** | -20.5 | 0e+00 | 34/35 (NCI-H1573, SW48, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.536×** | -9.9 | 5e-21 | 24/35 (SW48, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **0.542×** | -9.8 | 2e-20 | 27/35 (C32, BT-474, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.577×** | -8.4 | 4e-15 | 28/34 (SNU-1, RKO, …) | rises with dose | cell-cycle shift (explains ~8% here) |
| [[TAK-901 (drug)]] 5 µM |  | **0.413×** | -7.4 | 1e-11 | 28/36 (LoVo, C-33 A, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~20% here); composition shift; noisy plate (z scaled) |
| [[Brivudine (drug)]] 5 µM |  | **0.448×** | -6.7 | 2e-09 | 28/36 (A498, NCI-H1573, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~78% of this change | **0.666×** | -6.2 | 3e-08 | 18/30 (SNU-1, AN3 CA, …) | all doses, stronger at high dose | composition shift |
| [[PH-797804 (drug)]] 5 µM |  | **0.510×** | -5.6 | 1e-06 | 19/35 (HEC-1-A, LoVo, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~57% of this change | **0.722×** | -5.2 | 1e-05 | 25/34 (SW 1271, A-427, …) | inconsistent across doses | low cells (technical?) |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **0.608×** | -4.1 | 0.002 | 18/30 (SNU-1, NCI-H2030, …) | top dose only | noisy plate (z scaled) |
| [[Belinostat (drug)]] 0.05 µM |  | **0.771×** | -4.1 | 0.002 | 18/35 (C32, CHP-212, …) | all doses, stronger at high dose |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~85% of this change | **0.760×** | -4.0 | 0.002 | 17/32 (C32, NCI-H1573, …) | all doses, stronger at high dose | composition shift |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **0.787×** | -3.8 | 0.005 | 20/36 (SNU-423, LOX-IMVI, …) | inconsistent across doses |  |
| [[HI-TOPK-032 (drug)]] 5 µM |  | **0.647×** | -3.6 | 0.011 | 19/35 (SHP-77, C-33 A, …) | rises with dose | noisy plate (z scaled) |
| [[Pasireotide (acetate) (drug)]] 5 µM |  | 0.860× | -3.4 | 0.025 | 10/36 (HEC-1-A, A-427, …) | top dose only |  |
| [[Vilanterol (drug)]] 5 µM |  | 0.870× | -3.1 | 0.057 | 12/36 (HEC-1-A, HOP62, …) | top dose only |  |
| [[Mebendazole (drug)]] 5 µM |  | **0.816×** | -3.1 | 0.057 | 10/35 (A549, A498, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.30 per unit of S-phase module lfc, -0.29 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7936. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LoVo (line)]] | wt | 253 | 1 (1 ⚠) | 10 (5 ⚠) | [[Selinexor (drug)]] 5 µM 1.92× (z +9.5) ⚠ cell-cycle shift, explains ~41% of this change | [[Homoharringtonine (drug)]] 5 µM 0.285× (z -18.3) |
| [[C32 (line)]] | wt | 92.3 | 5 (4 ⚠) | 5 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 4.05× (z +13.1) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[TAK-901 (drug)]] 0.05 µM 2.62× (z +8.5) | [[Belinostat (drug)]] 5 µM 0.223× (z -14.0) |
| [[NCI-H1573 (line)]] | alt | 550 | 0 | 10 (5 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.0929× (z -22.9) |
| [[A498 (line)]] | wt | 112 | 3 | 6 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.75× (z +14.3) | [[Panobinostat (drug)]] 0.5 µM 0.133× (z -20.4) |
| [[HEC-1-A (line)]] | alt | 151 | 2 (1 ⚠) | 7 | [[Selinexor (drug)]] 5 µM 2.00× (z +11.3) ⚠ cell-cycle shift, explains ~41% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.89× (z +10.3) | [[Panobinostat (drug)]] 0.5 µM 0.133× (z -23.2) |
| [[LOX-IMVI (line)]] | wt | 113 | 0 | 7 (2 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.116× (z -20.9) |
| [[NCI-H1792 (line)]] | alt | 159 | 2 (1 ⚠) | 5 (1 ⚠) | [[Homoharringtonine (drug)]] 0.5 µM 2.35× (z +9.7) | [[Panobinostat (drug)]] 0.5 µM 0.195× (z -18.7) |
| [[SNU-1 (line)]] | wt | 171 | 1 | 6 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.15× (z +9.2) | [[Panobinostat (drug)]] 5 µM 0.0840× (z -21.1) |
| [[A-427 (line)]] | wt | 180 | 1 (1 ⚠) | 5 (1 ⚠) | [[Selinexor (drug)]] 5 µM 1.79× (z +9.0) ⚠ cell-cycle shift, explains ~41% of this change | [[Panobinostat (drug)]] 5 µM 0.380× (z -10.7) |
| [[C-33 A (line)]] | alt | 250 | 1 (1 ⚠) | 5 (1 ⚠) | [[Selinexor (drug)]] 5 µM 1.81× (z +9.4) ⚠ cell-cycle shift, explains ~41% of this change | [[Panobinostat (drug)]] 5 µM 0.177× (z -19.6) |
| [[H4 (line)]] | wt | 63.8 | 3 | 3 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.22× (z +17.8) | [[Belinostat (drug)]] 5 µM 0.208× (z -10.8) |
| [[NCI-H460 (line)]] | wt | 30.8 | 6 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.22× (z +22.2) | — |
| [[SW1417 (line)]] | alt | 84.5 | 2 (1 ⚠) | 4 (1 ⚠) | [[Selinexor (drug)]] 5 µM 2.72× (z +12.5) ⚠ cell-cycle shift, explains ~41% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 2.57× (z +11.8) | [[Belinostat (drug)]] 5 µM 0.278× (z -11.4) |
| [[HOP62 (line)]] | alt | 42.3 | 3 | 2 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.69× (z +12.7) | [[Panobinostat (drug)]] 5 µM 0.340× (z -9.8) |
| [[HT-29 (line)]] | alt | 32.0 | 2 (1 ⚠) | 3 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.45× (z +8.8) | [[Panobinostat (drug)]] 5 µM 0.256× (z -9.5) |
| [[J82 (line)]] | alt | 196 | 1 | 4 | [[Homoharringtonine (drug)]] 5 µM 2.67× (z +14.8) | [[Panobinostat (drug)]] 5 µM 0.189× (z -17.7) |
| [[NCI-H2030 (line)]] | alt | 205 | 0 | 5 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.252× (z -13.3) |
| [[SNU-423 (line)]] | alt | 168 | 0 | 5 | — | [[Panobinostat (drug)]] 0.5 µM 0.165× (z -16.6) |
| [[SW48 (line)]] | wt | 231 | 0 | 5 | — | [[Belinostat (drug)]] 5 µM 0.0946× (z -20.3) |
| [[A549 (line)]] | wt | 101 | 0 | 4 | — | [[Belinostat (drug)]] 5 µM 0.145× (z -15.7) |
| [[AN3 CA (line)]] | alt | 187 | 0 | 4 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.153× (z -11.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~78% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.168× (z -11.6) |
| [[Panc 03.27 (line)]] | alt | 65.6 | 0 | 4 | — | [[Panobinostat (drug)]] 5 µM 0.173× (z -14.2) |
| [[RKO (line)]] | wt | 76.1 | 0 | 4 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.0922× (z -17.5) ⚠ toxic · without an alert: [[Panobinostat (drug)]] 5 µM 0.231× (z -11.2) |
| [[BT-474 (line)]] | alt | 290 | 1 | 2 | [[Homoharringtonine (drug)]] 5 µM 3.01× (z +13.5) | [[Belinostat (drug)]] 0.5 µM 0.277× (z -11.1) |
| [[COLO 205 (line)]] | alt | 55.1 | 0 | 3 | — | [[Panobinostat (drug)]] 5 µM 0.188× (z -10.3) |
| [[SW 900 (line)]] | alt | 71.2 | 0 | 3 | — | [[Panobinostat (drug)]] 0.5 µM 0.252× (z -10.0) |
| [[NCI-H23 (line)]] | alt | 195 | 0 | 2 | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.329× (z -9.1) |
| [[SHP-77 (line)]] | alt | 119 | 1 | 1 | [[Homoharringtonine (drug)]] 5 µM 2.68× (z +12.3) | [[Panobinostat (drug)]] 0.5 µM 0.328× (z -9.8) |
| [[CFPAC-1 (line)]] | alt | 32.8 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.88× (z +10.7) | — |
| [[SW 1271 (line)]] | alt | 104 | 0 | 1 (1 ⚠) | — | [[Docetaxel (drug)]] 0.05 µM 0.103× (z -8.8) ⚠ transcription drop; cell-cycle shift, explains ~57% of this change |
| [[A-172 (line)]] | wt | 9.67 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 14.5 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 54.9 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 71.3 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 17.8 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 9.15 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 18.5 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 12.7 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 9.39 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 13.1 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 11.8 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 108 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 29.3 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 115 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 16.1 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 16.3 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 18.5 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 37.6 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 36.2 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 20.8 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7936), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*77 of its nearest partners move with it, 10 of them with an alert (⚠; 10 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SLC25A21]] | +0.79 | +0.74 / +0.61 | both halves | 7e-06 |  |
| [[PARD3B]] | +0.70 | +0.74 / +0.58 | both halves | 7e-06 | same gene group |
| [[TMEM117]] | +0.68 | +0.66 / +0.50 | both halves | 1e-05 |  |
| [[MMADHC-DT]] | +0.67 | +0.52 / +0.46 | both halves | 3e-05 |  |
| [[ANKRD18B]] | +0.66 | +0.57 / +0.33 | both halves | 1e-04 |  |
| [[IQCH-AS1]] | +0.65 | +0.62 / +0.33 | both halves | 1e-04 |  |
| [[PHACTR2]] | +0.65 | +0.59 / +0.47 | both halves | 2e-05 |  |
| [[ARRDC3-AS1]] | +0.65 | +0.53 / +0.39 | both halves | 5e-05 |  |
| [[LINC01725]] | +0.64 | +0.55 / +0.32 | both halves | 2e-04 |  |
| [[ZHX2]] | +0.64 | +0.48 / +0.37 | both halves | 8e-05 |  |
| [[CRPPA]] | +0.63 | +0.52 / +0.33 | both halves | 1e-04 |  |
| [[CACNA2D1]] | +0.63 | +0.61 / +0.38 | both halves | 7e-05 | pathway: Neuronal System |

## Genes that move opposite

*23 of its nearest partners move opposite, 2 of them with an alert (⚠; 2 not replicated); shown: the 12 strongest and the 2 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[IFT172]] | -0.67 | -0.50 / -0.50 | both halves | 1e-05 |  |
| [[POT1]] | -0.65 | -0.59 / -0.41 | both halves | 4e-05 |  |
| [[FHIP1B]] | -0.62 | -0.53 / -0.47 | both halves | 2e-05 |  |
| [[EFHC1]] | -0.61 | -0.41 / -0.42 | both halves | 4e-05 |  |
| [[RAB3A]] | -0.60 | -0.49 / -0.19 | ⚠ not reproduced | 8e-04 | pathway: Neuronal System |
| [[ELP1]] | -0.59 | -0.54 / -0.23 | both halves | 5e-04 |  |
| [[LCMT1]] | -0.59 | -0.52 / -0.27 | both halves | 3e-04 |  |
| [[MINK1]] | -0.59 | -0.53 / -0.36 | both halves | 1e-04 |  |
| [[HEATR5B]] | -0.59 | -0.47 / -0.35 | both halves | 1e-04 |  |
| [[POGLUT2]] | -0.58 | -0.51 / -0.34 | both halves | 1e-04 |  |
| [[SNAPC3]] | -0.58 | -0.54 / -0.34 | both halves | 1e-04 |  |
| [[YIF1B]] | -0.58 | -0.49 / -0.09 | ⚠ not reproduced | 0.003 |  |
| [[PRPF3]] | -0.58 | -0.55 / -0.56 | both halves | 1e-05 |  |
| [[PIBF1]] | -0.58 | -0.52 / -0.33 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*6 arrows, 6 of them with an alert ⚠; grade A 0, B 6, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[L3MBTL4]] | B | L3MBTL4 activity raises GRIP1's level | lines that do not express L3MBTL4 (26) vs lines expressing it (24) | 2.30× lower at baseline in the lines without L3MBTL4 | 0.026 | ⚠ within organs, on part of the lines; also absent: FGF14, SNCA, BASP1-AS1 |
| [[BMPR1B]] | B | BMPR1B activity raises GRIP1's level | lines that do not express BMPR1B (28) vs lines expressing it (22) | 2.10× lower at baseline in the lines without BMPR1B | 0.048 | ⚠ within organs, on part of the lines; also absent: ENSG00000286385, SLC6A17, EPHA5-AS1 |
| [[PPM1L]] | B | PPM1L activity raises GRIP1's level | lines that do not express PPM1L (8) vs lines expressing it (42) | 2.75× lower at baseline in the lines without PPM1L | 0.051 | ⚠ within organs, on part of the lines; also absent: SLC25A27, SORBS1, LINC01277; maybe low, not absent |
| [[TOP2A]] | B | TOP2A activity lowers GRIP1's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 7.0% of all compounds | 0.059 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[UST]] | B | UST activity raises GRIP1's level | lines that do not express UST (12) vs lines expressing it (38) | 2.51× lower at baseline in the lines without UST | 0.089 | ⚠ within organs, on part of the lines; also absent: SLC1A1, SH3GL3 |
| [[FAXC]] | B | FAXC activity raises GRIP1's level | lines that do not express FAXC (11) vs lines expressing it (39) | 2.69× lower at baseline in the lines without FAXC | 0.094 | ⚠ within organs, on part of the lines; also absent: NTN1, CYP46A1, CSRP2 |

### Downstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 4, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[STPG2]] | B | GRIP1 activity raises STPG2's level | lines that do not express GRIP1 (13) vs lines expressing it (37) | 2.49× lower at baseline in the lines without GRIP1 | 0.011 | ⚠ within organs, on part of the lines; also absent: PAX9; maybe low, not absent |
| [[CNEP1R1]] | B | GRIP1 activity lowers CNEP1R1's level | lines that do not express GRIP1 (13) vs lines expressing it (37) | 1.15× higher at baseline in the lines without GRIP1 | 0.027 | ⚠ within organs, on part of the lines; also absent: PAX9; maybe low, not absent |
| [[YIF1B]] | B | GRIP1 activity lowers YIF1B's level | lines that do not express GRIP1 (13) vs lines expressing it (37) | 1.35× higher at baseline in the lines without GRIP1 | 0.043 | ⚠ within organs, on part of the lines; also absent: PAX9; maybe low, not absent |
| [[L3MBTL4]] | B | GRIP1 activity raises L3MBTL4's level | lines that do not express GRIP1 (13) vs lines expressing it (37) | 3.66× lower at baseline in the lines without GRIP1 | 0.055 | ⚠ within organs, on part of the lines; also absent: PAX9; maybe low, not absent |

## Where it sits

- **Module**: [[Module 137]]; 34 genes; this gene is in the **+** arm (projection on the module's main direction 0.716). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.43).
- **Nodal map** (x, y) = (-3.9, 8.0); signed map (24.8, -31.4). **Vector** length 127, 36.5% of its response variance represented; |z| ≥ 3 in 1,129 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +10.3 | +10.3 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~41% of this change | +7.9 | +10.4 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +6.3 | +7.2 |
|  | [[Harringtonine (drug)]] 5 µM |  | +6.3 | +7.6 |
|  | [[Auranofin (drug)]] 5 µM |  | +6.2 | +2.7 |
|  | [[Belumosudil (drug)]] 5 µM |  | +4.7 | +3.4 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +4.5 | +3.0 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +3.4 | +6.1 |
| fall | [[Belinostat (drug)]] 5 µM |  | -6.7 | -20.5 |
|  | [[Belinostat (drug)]] 0.5 µM |  | -5.7 | -9.8 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | -5.6 | -22.0 |
|  | [[TAK-901 (drug)]] 5 µM |  | -4.9 | -7.4 |
|  | [[Panobinostat (drug)]] 5 µM |  | -4.7 | -21.4 |
|  | [[PH-797804 (drug)]] 5 µM |  | -3.8 | -5.6 |
|  | [[Brivudine (drug)]] 5 µM |  | -2.9 | -6.7 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | -2.5 | -3.6 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | -2.1 | -3.8 |
|  | [[Goserelin (acetate) (drug)]] 5 µM |  | -2.1 | -1.6 |

## What is on record

|  |  |
|---|---|
| Name | glutamate receptor interacting protein 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 12q14.3 — chr12:66,347,431-67,069,162 (-) |
| Ensembl biotype | protein_coding |
| Gene groups (HGNC) | PDZ domain containing |
| Reactome | 6 pathways, smallest: Trafficking of GluR2-containing AMPA receptors; Glutamate binding, activation of AMPA receptors and synaptic plasticity; Trafficking of AMPA receptors |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9Y3R0](https://www.uniprot.org/uniprotkb/Q9Y3R0) (Glutamate receptor-interacting protein 1):

> May play a role as a localized scaffold for the assembly of a multiprotein signaling complex and as mediator of the trafficking of its binding partners at specific subcellular location in neurons. Through complex formation with NSG1, GRIA2 and STX12 controls the intracellular fate of AMPAR and the endosomal sorting of the GRIA2 subunit toward recycling and membrane targeting (By similarity).

**Summary**, from NCBI Gene [23426](https://www.ncbi.nlm.nih.gov/gene/23426):

> This gene encodes a member of the glutamate receptor interacting protein family. The encoded scaffold protein binds to and mediates the trafficking and membrane organization of a number of transmembrane proteins. Alternatively spliced transcript variants encoding different isoforms have been described. [provided by RefSeq, May 2010]

**Accessions** — [HGNC:18708](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:18708) · Entrez [23426](https://www.ncbi.nlm.nih.gov/gene/23426) · UniProt [Q9Y3R0](https://www.uniprot.org/uniprotkb/Q9Y3R0) · Ensembl [ENSG00000155974](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000155974)

## Data

Gene col 7936: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7936); `tables/drug_effects.parquet` (60 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7936, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7936]; `tensor/DDL_lfc|DDL_z.npy` [7936]; `embed/gene_vectors.npy` [7936]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7936 or target_col == 7936). Every well: [[GRIP1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/GRIP1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
