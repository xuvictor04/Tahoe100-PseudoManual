---
symbol: "DHRS3"
type: "gene"
col: 8523
ensembl_id: "ENSG00000162496"
name: "dehydrogenase/reductase 3"
location: "1p36.21"
module: 69
arm: "+"
pooled_cpm: 109.26
n_lines_expressing: 37
n_dd_up: 14
n_dd_down: 55
n_dd_up_clean: 12
n_dd_down_clean: 33
in_vector_space: true
direction_upstream: 4
direction_downstream: 16
tags: ["gene", "module/069"]
generated_by: "tahoemap"
---

# DHRS3

*dehydrogenase/reductase 3* — 1p36.21

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 14 drug-doses (2 with an alert ⚠); the strongest is [[Retinoic acid (drug)]] 5 µM: 1.46× (z +8.8, q 4e-16, up in 32 of 36 measured lines).
> Pooled over the cell lines (median), lowered significantly by 55 drug-doses (22 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 0.183× (z -27.9, q 0e+00, down in 35 of 35 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[HOXA5]] (+0.66, fdr 1e-05), [[FBXO32]] (+0.59, fdr 1e-05), [[GPRC5C]] (+0.58, fdr 6e-05); moves opposite to [[SACS]] (-0.57, fdr 7e-06), [[WDR77]] (-0.51, fdr 2e-05), [[C3orf52]] (-0.51, fdr 3e-05).
> It is in [[Module 069]], a single-armed module (FOXO-mediated transcription).
> Probable direction (from the cell lines, not proof of direct regulation): 4 arrows point to it, the strongest [[ADAM28]] → it (grade B ⚠); 16 go from it, the strongest it → [[GPRC5C]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 19 in all, 4 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 14 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8523.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Retinoic acid (drug)]] 5 µM |  | **1.46×** | +8.8 | 4e-16 | 32/36 (SHP-77, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Retinoic acid (drug)]] 0.5 µM |  | **1.71×** | +8.8 | 4e-16 | 35/35 (SHP-77, PANC-1, …) | all doses, stronger at high dose |  |
| [[Retinoic acid (drug)]] 0.05 µM |  | **1.50×** | +6.7 | 5e-09 | 29/35 (SHP-77, LOX-IMVI, …) | all doses, stronger at high dose |  |
| [[Tirabrutinib (hydrochloride) (drug)]] 5 µM | ⚠ position correction uncertain | **1.43×** | +5.9 | 5e-07 | 30/35 (PANC-1, SHP-77, …) | all doses, stronger at high dose |  |
| [[Tirabrutinib (hydrochloride) (drug)]] 0.5 µM | ⚠ position correction uncertain | **1.38×** | +5.3 | 1e-05 | 28/35 (PANC-1, HT-29, …) | all doses, stronger at high dose |  |
| [[Clotrimazole (drug)]] 5 µM |  | **1.24×** | +5.1 | 3e-05 | 19/36 (SHP-77, CFPAC-1, …) | rises with dose |  |
| [[Tazarotene (drug)]] 5 µM |  | **1.32×** | +4.5 | 4e-04 | 21/35 (SHP-77, CFPAC-1, …) | all doses, stronger at high dose |  |
| [[Posaconazole (drug)]] 5 µM |  | **1.30×** | +4.1 | 0.003 | 23/35 (CFPAC-1, RPMI-7951, …) | top dose only | plate-row cell shift |
| [[Cobimetinib (drug)]] 5 µM |  | **1.27×** | +3.8 | 0.010 | 18/35 (AsPC-1, J82, …) | rises with dose |  |
| [[Tazarotene (drug)]] 0.5 µM |  | **1.25×** | +3.8 | 0.010 | 18/36 (SHP-77, PANC-1, …) | all doses, stronger at high dose |  |
| [[Bexarotene (drug)]] 0.5 µM |  | **1.23×** | +3.5 | 0.026 | 18/35 (NCI-H460, SHP-77, …) | inconsistent across doses |  |
| [[Apalutamide (drug)]] 5 µM |  | **1.23×** | +3.3 | 0.044 | 15/35 (LOX-IMVI, SHP-77, …) | rises with dose |  |
| [[Tirabrutinib (drug)]] 5 µM |  | **1.22×** | +3.2 | 0.053 | 10/35 (SHP-77, PANC-1, …) | rises with dose |  |
| [[Bexarotene (drug)]] 0.05 µM |  | **1.21×** | +3.1 | 0.066 | 16/35 (SHP-77, PANC-1, …) | inconsistent across doses |  |
| [[Gemfibrozil (drug)]] 5 µM |  | 1.14× | +3.1 | 0.072 | 9/37 (SHP-77, PANC-1, …) | top dose only |  |
| [[Tirabrutinib (drug)]] 0.5 µM |  | 1.20× | +3.0 | 0.082 | 13/35 (RPMI-7951, HEC-1-A, …) | rises with dose |  |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | 1.20× | +3.0 | 0.082 | 14/36 (PANC-1, RPMI-7951, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 60 in all, 25 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 55 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 22 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 8523.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **0.183×** | -27.9 | 0e+00 | 35/35 (COLO 205, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.188×** | -27.5 | 0e+00 | 35/35 (COLO 205, SW 900, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.287×** | -20.5 | 0e+00 | 35/35 (COLO 205, SW 900, …) | rises with dose | cell-cycle shift (explains ~25% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.461×** | -17.9 | 0e+00 | 28/35 (NCI-H1792, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change | **0.326×** | -17.7 | 0e+00 | 30/33 (SW 900, A549, …) | all doses, stronger at high dose | composition shift; position effect removed |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.373×** | -16.2 | 0e+00 | 32/35 (NCI-H1573, RPMI-7951, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.385×** | -15.7 | 0e+00 | 33/35 (SW1417, SW 900, …) | inconsistent across doses |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~42% of this change | **0.393×** | -15.3 | 0e+00 | 29/36 (COLO 205, BT-474, …) | all doses, stronger at high dose | composition shift; position effect removed |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.441×** | -12.9 | 3e-36 | 33/35 (COLO 205, A549, …) | rises with dose | cell-cycle shift (explains ~19% here); position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.475×** | -12.2 | 2e-32 | 33/35 (COLO 205, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here); composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.472×** | -11.8 | 1e-30 | 28/35 (SW 900, Panc 03.27, …) | rises with dose | cell-cycle shift (explains ~23% here) |
| [[Auranofin (drug)]] 5 µM |  | **0.489×** | -11.7 | 5e-30 | 35/35 (RPMI-7951, Hs 766T, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.514×** | -10.9 | 4e-26 | 33/35 (RPMI-7951, SW 900, …) | rises with dose | cell-cycle shift (explains ~12% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change | **0.487×** | -10.9 | 5e-26 | 31/34 (SNU-423, A549, …) | all doses, stronger at high dose | composition shift; position effect removed |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.565×** | -9.3 | 4e-19 | 30/35 (SW 900, RPMI-7951, …) | rises with dose |  |
| [[EX229 (drug)]] 5 µM |  | **0.331×** | -9.3 | 4e-19 | 29/35 (RPMI-7951, Panc 03.27, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Abemaciclib (drug)]] 5 µM |  | **0.365×** | -8.5 | 6e-16 | 30/35 (A498, SW 900, …) | rises with dose | noisy plate (z scaled) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.595×** | -8.5 | 6e-16 | 27/35 (NCI-H1573, NCI-H460, …) | two highest doses | cell-cycle shift (explains ~9% here) |
| [[Peretinoin (drug)]] 5 µM |  | **0.615×** | -7.6 | 6e-13 | 28/35 (Panc 03.27, NCI-H1573, …) | all doses, stronger at high dose |  |
| [[Peretinoin (drug)]] 0.5 µM |  | **0.639×** | -7.3 | 6e-12 | 26/35 (Panc 03.27, MIA PaCa-2, …) | all doses, stronger at high dose |  |
| [[TAK-733 (drug)]] 5 µM |  | **0.420×** | -7.3 | 6e-12 | 26/35 (LoVo, SW1417, …) | top dose only | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.57 per unit of S-phase module lfc, +0.05 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8523. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW 900 (line)]] | alt | 281 | 0 | 27 (12 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0575× (z -27.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.0719× (z -25.9) |
| [[Panc 03.27 (line)]] | alt | 155 | 0 | 23 (10 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.151× (z -19.8) |
| [[BT-474 (line)]] | alt | 161 | 0 | 20 (13 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.0432× (z -22.4) |
| [[NCI-H1573 (line)]] | alt | 106 | 0 | 20 (6 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0722× (z -33.1) |
| [[SHP-77 (line)]] | alt | 114 | 3 | 17 (9 ⚠) | [[Retinoic acid (drug)]] 5 µM 3.46× (z +12.3) | [[Homoharringtonine (drug)]] 5 µM 0.0912× (z -23.5) |
| [[RPMI-7951 (line)]] | alt | 210 | 0 | 18 (8 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.140× (z -28.0) |
| [[SNU-423 (line)]] | alt | 182 | 0 | 18 (9 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.212× (z -26.0) |
| [[A549 (line)]] | wt | 221 | 0 | 16 (7 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.0993× (z -26.4) |
| [[CFPAC-1 (line)]] | alt | 179 | 0 | 16 (6 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.183× (z -16.8) |
| [[NCI-H460 (line)]] | wt | 41.3 | 4 (1 ⚠) | 12 (6 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.60× (z +11.2) ⚠ cell-cycle shift, explains ~33% of this change · without an alert: [[Retinoic acid (drug)]] 5 µM 2.53× (z +10.9) | [[Homoharringtonine (drug)]] 5 µM 0.265× (z -15.4) |
| [[PANC-1 (line)]] | alt | 132 | 2 | 13 (8 ⚠) | [[Retinoic acid (drug)]] 5 µM 1.84× (z +10.8) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.427× (z -14.9) ⚠ cell-cycle shift, explains ~33% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.305× (z -14.7) |
| [[COLO 205 (line)]] | alt | 356 | 0 | 13 (5 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0177× (z -42.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~42% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.114× (z -32.6) |
| [[HEC-1-A (line)]] | alt | 176 | 0 | 13 (3 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.113× (z -22.2) |
| [[A498 (line)]] | wt | 221 | 0 | 12 (3 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.188× (z -18.7) |
| [[MIA PaCa-2 (line)]] | alt | 75.8 | 0 | 12 (2 ⚠) | — | [[Homoharringtonine (drug)]] 0.05 µM 0.112× (z -17.0) |
| [[SW1417 (line)]] | alt | 76.8 | 0 | 11 (5 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.170× (z -18.7) ⚠ unreliable plate only · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.182× (z -18.0) |
| [[AN3 CA (line)]] | alt | 233 | 0 | 10 (3 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.108× (z -15.6) |
| [[C32 (line)]] | wt | 149 | 0 | 10 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.125× (z -27.1) |
| [[Hs 766T (line)]] | wt | 344 | 0 | 10 (3 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.195× (z -14.2) |
| [[NCI-H1792 (line)]] | alt | 264 | 0 | 10 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0943× (z -35.7) |
| [[AsPC-1 (line)]] | alt | 110 | 0 | 9 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.211× (z -20.3) |
| [[HS-578T (line)]] | alt | 145 | 0 | 8 (3 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.0889× (z -23.3) |
| [[LoVo (line)]] | wt | 80.7 | 1 (1 ⚠) | 7 (3 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.41× (z +13.1) ⚠ cell-cycle shift, explains ~33% of this change | [[Panobinostat (drug)]] 0.5 µM 0.202× (z -16.9) |
| [[HT-29 (line)]] | alt | 79.2 | 0 | 7 (3 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.158× (z -18.1) |
| [[NCI-H2347 (line)]] | alt | 77.7 | 0 | 7 (4 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.146× (z -17.8) |
| [[J82 (line)]] | alt | 91.1 | 0 | 5 (3 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.242× (z -12.5) ⚠ toxic · without an alert: [[Panobinostat (drug)]] 5 µM 0.361× (z -9.3) |
| [[KATO III (line)]] | alt | 98.9 | 0 | 5 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0989× (z -18.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.141× (z -16.2) |
| [[LS 180 (line)]] | wt | 61.0 | 1 (1 ⚠) | 4 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.61× (z +11.2) ⚠ cell-cycle shift, explains ~33% of this change | [[Panobinostat (drug)]] 0.5 µM 0.126× (z -17.0) |
| [[HepG2_C3A (line)]] | wt | 359 | 0 | 4 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.206× (z -14.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.360× (z -9.9) |
| [[SK-MEL-2 (line)]] | alt | 39.3 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.193× (z -14.9) |
| [[SW480 (line)]] | alt | 45.0 | 0 | 4 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.272× (z -11.8) ⚠ unreliable plate only · without an alert: [[Panobinostat (drug)]] 5 µM 0.310× (z -10.7) |
| [[CHP-212 (line)]] | wt | 82.0 | 0 | 3 (2 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.106× (z -9.4) ⚠ toxic · without an alert: [[Panobinostat (drug)]] 5 µM 0.120× (z -9.3) |
| [[LOX-IMVI (line)]] | wt | 27.6 | 1 | 1 | [[Retinoic acid (drug)]] 5 µM 3.97× (z +9.9) | [[Homoharringtonine (drug)]] 5 µM 0.178× (z -12.2) |
| [[HOP62 (line)]] | alt | 45.0 | 0 | 1 | — | [[Panobinostat (drug)]] 0.5 µM 0.298× (z -9.0) |
| [[A-172 (line)]] | wt | 8.95 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 10.4 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 9.30 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 40.9 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 19.3 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 11.2 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 7.10 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 96.3 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 12.3 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 89.2 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 11.6 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 11.6 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 9.31 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 23.5 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 8.95 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 22.5 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8523), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*72 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[HOXA5]] | +0.66 | +0.50 / +0.67 | both halves | 1e-05 |  |
| [[FBXO32]] | +0.59 | +0.51 / +0.56 | both halves | 1e-05 |  |
| [[GPRC5C]] | +0.58 | +0.38 / +0.63 | both halves | 6e-05 |  |
| [[ATOSA]] | +0.57 | +0.49 / +0.59 | both halves | 1e-05 |  |
| [[ARID4A]] | +0.56 | +0.41 / +0.61 | both halves | 4e-05 |  |
| [[PEX13]] | +0.55 | +0.55 / +0.52 | both halves | 1e-05 | pathway: HALLMARK_PEROXISOME |
| [[ETFB]] | +0.54 | +0.51 / +0.59 | both halves | 1e-05 |  |
| [[TERF2IP]] | +0.53 | +0.35 / +0.59 | both halves | 1e-04 |  |
| [[ELF2]] | +0.52 | +0.40 / +0.55 | both halves | 5e-05 |  |
| [[CNNM2]] | +0.51 | +0.44 / +0.53 | both halves | 3e-05 |  |
| [[TRIM7-AS2]] | +0.51 | +0.43 / +0.54 | both halves | 3e-05 |  |
| [[EAPP]] | +0.51 | +0.32 / +0.57 | both halves | 1e-04 |  |

## Genes that move opposite

*28 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SACS]] | -0.57 | -0.58 / -0.58 | both halves | 7e-06 |  |
| [[WDR77]] | -0.51 | -0.49 / -0.48 | both halves | 2e-05 |  |
| [[C3orf52]] | -0.51 | -0.43 / -0.49 | both halves | 3e-05 | same gene group |
| [[HOMER2]] | -0.50 | -0.33 / -0.55 | both halves | 1e-04 |  |
| [[GNPNAT1]] | -0.50 | -0.51 / -0.51 | both halves | 1e-05 |  |
| [[TBILA]] | -0.50 | -0.43 / -0.52 | both halves | 3e-05 |  |
| [[TTL]] | -0.50 | -0.44 / -0.51 | both halves | 3e-05 |  |
| [[CCT3]] | -0.49 | -0.48 / -0.51 | both halves | 2e-05 |  |
| [[CCT5]] | -0.49 | -0.48 / -0.47 | both halves | 2e-05 |  |
| [[ADCY7]] | -0.48 | -0.54 / -0.38 | both halves | 7e-05 | same gene group |
| [[SUPT3H]] | -0.48 | -0.47 / -0.45 | both halves | 3e-05 | same gene group |
| [[UGGT2]] | -0.47 | -0.43 / -0.49 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 3, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ADAM28]] | B | ADAM28 activity raises DHRS3's level | lines that do not express ADAM28 (31) vs lines expressing it (19) | 2.51× lower at baseline in the lines without ADAM28 | 0.008 | ⚠ within organs, on part of the lines; also absent: DHRS9, BATF, IGFBP5 |
| [[GPRC5C]] | B | GPRC5C activity raises DHRS3's level | lines that do not express GPRC5C (13) vs lines expressing it (37) | 3.02× lower at baseline in the lines without GPRC5C | 0.013 | ⚠ within organs, on part of the lines; also absent: TMEM184A, VAMP8, ASS1 |
| [[PLD1]] | B | PLD1 activity raises DHRS3's level | lines that do not express PLD1 (7) vs lines expressing it (43) | 4.46× lower at baseline in the lines without PLD1 | 0.067 | ⚠ within organs, on part of the lines; also absent: DUSP1, ATP1B1, DUSP10; maybe low, not absent |
| [[FBXO32]] | C | FBXO32 activity raises DHRS3's level | lines that do not express FBXO32 (14) vs lines expressing it (36) | 3.24× lower at baseline in the lines without FBXO32 | 0.012 | ⚠ within organs, on part of the lines; also absent: ETS2, BACE2, MLPH; maybe low, not absent; co-absent with the target |

### Downstream of this gene

*16 arrows, 16 of them with an alert ⚠; grade A 0, B 14, C 2. Shown: the 12 strongest; 4 more arrows (4 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[GPRC5C]] | B | DHRS3 activity raises GPRC5C's level | lines that do not express DHRS3 (13) vs lines expressing it (37) | 2.99× lower at baseline in the lines without DHRS3 | 0.001 | ⚠ within organs, on part of the lines; also absent: CCDC9B, ENSG00000290729, STON2 |
| [[SACS]] | B | DHRS3 activity lowers SACS's level | lines that do not express DHRS3 (13) vs lines expressing it (37) | 1.67× higher at baseline in the lines without DHRS3 | 0.026 | ⚠ within organs, on part of the lines; also absent: CCDC9B, ENSG00000290729, STON2 |
| [[TTL]] | B | DHRS3 activity lowers TTL's level | lines that do not express DHRS3 (13) vs lines expressing it (37) | 1.65× higher at baseline in the lines without DHRS3 | 0.039 | ⚠ within organs, on part of the lines; also absent: CCDC9B, ENSG00000290729, STON2 |
| [[TPCN1]] | B | DHRS3 activity raises TPCN1's level | lines that do not express DHRS3 (13) vs lines expressing it (37) | 1.56× lower at baseline in the lines without DHRS3 | 0.050 | ⚠ within organs, on part of the lines; also absent: CCDC9B, ENSG00000290729, STON2 |
| [[DYNC2I1]] | B | DHRS3 activity raises DYNC2I1's level | lines that do not express DHRS3 (13) vs lines expressing it (37) | 1.33× lower at baseline in the lines without DHRS3 | 0.051 | ⚠ within organs, on part of the lines; also absent: CCDC9B, ENSG00000290729, STON2 |
| [[ADAMTSL5]] | B | DHRS3 activity lowers ADAMTSL5's level | lines that do not express DHRS3 (13) vs lines expressing it (37) | 1.51× higher at baseline in the lines without DHRS3 | 0.055 | ⚠ within organs, on part of the lines; also absent: CCDC9B, ENSG00000290729, STON2 |
| [[GNPNAT1]] | B | DHRS3 activity lowers GNPNAT1's level | lines that do not express DHRS3 (13) vs lines expressing it (37) | 1.50× higher at baseline in the lines without DHRS3 | 0.060 | ⚠ within organs, on part of the lines; also absent: CCDC9B, ENSG00000290729, STON2 |
| [[MVP]] | B | DHRS3 activity strengthens MVP's drug response | lines that do not express DHRS3 (13) vs lines expressing it (34) | the lines without DHRS3 respond 0.47× as strongly (z diff +1.90); strongest at Homoharringtonine 5 µM: 1.08x vs 0.63x (z diff +5.4) | 0.060 | ⚠ within organs, on part of the lines; also absent: CCDC9B, ENSG00000290729, STON2; target measured in part of the lines; artifact flags |
| [[TTL]] | B | DHRS3 activity strengthens TTL's drug response | lines that do not express DHRS3 (13) vs lines expressing it (33) | the lines without DHRS3 respond 0.47× as strongly (z diff +1.79); strongest at Doxorubicin (hydrochloride) 5 µM: 1.30x vs 1.89x (z diff +2.7) | 0.060 | ⚠ within organs, on part of the lines; also absent: CCDC9B, ENSG00000290729, STON2; target measured in part of the lines; artifact flags |
| [[CDKN1B]] | B | DHRS3 activity strengthens CDKN1B's drug response | lines that do not express DHRS3 (13) vs lines expressing it (36) | the lines without DHRS3 respond 0.69× as strongly (z diff +0.95); strongest at Belinostat 5 µM: 0.60x vs 0.41x (z diff +2.6) | 0.063 | ⚠ within organs, on part of the lines; also absent: CCDC9B, ENSG00000290729, STON2; target measured in part of the lines; the reference differs; artifact flags |
| [[CCT5]] | B | DHRS3 activity lowers CCT5's level | lines that do not express DHRS3 (13) vs lines expressing it (37) | 1.34× higher at baseline in the lines without DHRS3 | 0.069 | ⚠ within organs, on part of the lines; also absent: CCDC9B, ENSG00000290729, STON2 |
| [[WDR77]] | B | DHRS3 activity lowers WDR77's level | lines that do not express DHRS3 (13) vs lines expressing it (37) | 1.38× higher at baseline in the lines without DHRS3 | 0.074 | ⚠ within organs, on part of the lines; also absent: CCDC9B, ENSG00000290729, STON2 |

## Where it sits

- **Module**: [[Module 069]] — FOXO-mediated transcription; 71 genes; every member is in the + arm (projection on the module's main direction 0.504). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.33; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-2.1, -43.6); signed map (-12.0, 10.4). **Vector** length 113, 37.9% of its response variance represented; |z| ≥ 3 in 1,791 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | +3.7 | -9.2 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +3.4 | -17.9 |
|  | [[Retinoic acid (drug)]] 5 µM |  | +3.2 | +8.8 |
|  | [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift | +2.9 | -1.3 |
|  | [[Osimertinib (mesylate) (drug)]] 5 µM |  | +2.6 | +1.7 |
|  | [[Retinoic acid (drug)]] 0.5 µM |  | +2.6 | +8.8 |
|  | [[Triamcinolone (drug)]] 5 µM |  | +2.2 | -0.0 |
|  | [[Cabozantinib (S-malate) (drug)]] 5 µM |  | +2.1 | +2.0 |
| fall | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -9.6 | -15.7 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change | -6.6 | -17.7 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~42% of this change | -6.5 | -15.3 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -6.2 | -7.3 |
|  | [[Peretinoin (drug)]] 5 µM |  | -6.1 | -7.6 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | -5.3 | -6.1 |
|  | [[EX229 (drug)]] 5 µM |  | -4.9 | -9.3 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -4.8 | -8.5 |

## What is on record

|  |  |
|---|---|
| Name | dehydrogenase/reductase 3 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1p36.21 — chr1:12,567,909-12,620,133 (-) |
| Ensembl biotype | protein_coding |
| Also known as | retSDR1, Rsdr1, SDR1, RDH17, SDR16C1, CNALPTC1 |
| Gene groups (HGNC) | Short chain dehydrogenase/reductase superfamily; MicroRNA protein coding host genes |
| Hallmark sets | PEROXISOME, IL2_STAT5_SIGNALING, ESTROGEN_RESPONSE_EARLY |
| Reactome | 5 pathways, smallest: RA biosynthesis pathway; Signaling by Retinoic Acid; Visual phototransduction |
| Matched by | ensembl_id |

**Function**, from UniProt [O75911](https://www.uniprot.org/uniprotkb/O75911) (Short-chain dehydrogenase/reductase 3):

> Catalyzes the reduction of all-trans-retinal to all-trans-retinol in the presence of NADPH. It limits excessive synthesis of all-trans retinoic acid (RA) from all-trans-retinal.

**Summary**, from NCBI Gene [9249](https://www.ncbi.nlm.nih.gov/gene/9249):

> Predicted to enable all-trans-retinol dehydrogenase (NAD+) activity. Predicted to be involved in regulation of retinoic acid receptor signaling pathway and retinoid metabolic process. Predicted to act upstream of or within several processes, including heart morphogenesis; negative regulation of retinoic acid receptor signaling pathway; and regulation of ossification. Predicted to be located in endoplasmic reticulum membrane and photoreceptor outer segment membrane. Predicted to be active in …

**Accessions** — [HGNC:17693](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:17693) · Entrez [9249](https://www.ncbi.nlm.nih.gov/gene/9249) · UniProt [O75911](https://www.uniprot.org/uniprotkb/O75911) · Ensembl [ENSG00000162496](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000162496)

## Data

Gene col 8523: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8523); `tables/drug_effects.parquet` (79 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8523, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8523]; `tensor/DDL_lfc|DDL_z.npy` [8523]; `embed/gene_vectors.npy` [8523]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8523 or target_col == 8523). Every well: [[DHRS3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/DHRS3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
