---
symbol: "IGF2BP3"
type: "gene"
col: 5836
ensembl_id: "ENSG00000136231"
name: "insulin like growth factor 2 mRNA binding protein 3"
location: "7p15.3"
module: 30
arm: "-"
pooled_cpm: 320.86
n_lines_expressing: 46
n_dd_up: 6
n_dd_down: 10
n_dd_up_clean: 5
n_dd_down_clean: 4
in_vector_space: true
direction_upstream: 3
direction_downstream: 1
tags: ["gene", "module/030"]
generated_by: "tahoemap"
---

# IGF2BP3

*insulin like growth factor 2 mRNA binding protein 3* — 7p15.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 6 drug-doses (1 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 0.5 µM: 1.49× (z +9.7, q 2e-19, up in 31 of 44 measured lines).
> Pooled over the cell lines (median), lowered significantly by 10 drug-doses (6 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 0.5 µM: 0.278× (z -31.1, q 0e+00, down in 43 of 44 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SATB2]] (+0.73, fdr 7e-06), [[ASXL2]] (+0.56, fdr 3e-05), [[CLOCK]] (+0.55, fdr 1e-04); moves opposite to [[STRA6LP]] (-0.58, fdr 2e-05), [[MRPS31P4]] (-0.58, fdr 3e-05), [[MKRN2]] (-0.58, fdr 3e-05).
> It sits in the **-** arm of [[Module 030]].
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[PKIG]] → it (grade B ⚠); 1 goes from it, the strongest it → cells under [[Tomivosertib (drug)]] 5 µM (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, 2 with an alert ⚠. 6 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5836.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.49×** | +9.7 | 2e-19 | 31/44 (SW480, Panc 03.27, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.31×** | +9.4 | 2e-18 | 25/45 (AsPC-1, LoVo, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.42×** | +8.4 | 6e-15 | 28/44 (LoVo, Panc 03.27, …) | two highest doses | cell-cycle shift (explains ~0% here); composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.39×** | +7.9 | 3e-13 | 30/44 (SW480, LoVo, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.05 µM |  | **1.27×** | +5.7 | 1e-06 | 28/43 (SW480, PANC-1, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.22×** | +4.9 | 1e-04 | 22/44 (LoVo, SW480, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.16× | +3.5 | 0.035 | 18/44 (SW480, HOP62, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 16 in all, 8 with an alert ⚠; shown: the 15 strongest. 10 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 5836.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 0.5 µM |  | **0.278×** | -31.1 | 0e+00 | 43/44 (SW480, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.280×** | -30.9 | 0e+00 | 43/44 (SW480, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.477×** | -18.0 | 0e+00 | 42/44 (SW480, SHP-77, …) | top dose only | cell-cycle shift (explains ~12% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.589×** | -12.4 | 6e-33 | 35/43 (MIA PaCa-2, RKO, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | **0.709×** | -8.0 | 1e-13 | 26/40 (C-33 A, NCI-H460, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change | **0.747×** | -7.1 | 1e-10 | 27/45 (A-427, H4, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~24% of this change | **0.714×** | -6.9 | 3e-10 | 29/41 (NCI-H460, A-172, …) | all doses, stronger at high dose | composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **0.772×** | -6.3 | 2e-08 | 30/44 (SW 1271, PANC-1, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~7% here) |
| [[TAK-901 (drug)]] 5 µM |  | **0.657×** | -4.9 | 7e-05 | 27/45 (NCI-H1573, LOX-IMVI, …) | rises with dose | plate-row cell shift; cell-cycle shift (explains ~7% here); composition shift; noisy plate (z scaled) |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **0.833×** | -4.4 | 5e-04 | 20/44 (MIA PaCa-2, NCI-H2030, …) | all doses, stronger at high dose |  |
| [[Ponatinib (drug)]] 5 µM |  | 0.856× | -3.8 | 0.008 | 18/44 (NCI-H23, C32, …) | rises with dose |  |
| [[Amsacrine (drug)]] 5 µM |  | 0.898× | -3.7 | 0.010 | 9/44 (A549, NCI-H2030, …) | top dose only |  |
| [[Radotinib (drug)]] 5 µM |  | 0.899× | -3.6 | 0.012 | 12/44 (RKO, NCI-H23, …) | top dose only |  |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.904× | -3.4 | 0.023 | 13/44 (RKO, SK-MEL-2, …) | top dose only | low cells (technical?) |
| [[Mebendazole (drug)]] 5 µM |  | 0.864× | -3.4 | 0.025 | 12/44 (SW48, NCI-H1573, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.17 per unit of S-phase module lfc, +0.02 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5836. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 311 | 8 (3 ⚠) | 6 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 2.04× (z +14.6) | [[Panobinostat (drug)]] 5 µM 0.179× (z -35.2) |
| [[PANC-1 (line)]] | alt | 607 | 4 (2 ⚠) | 8 (5 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.67× (z +13.6) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 0.5 µM 1.85× (z +11.5) | [[Panobinostat (drug)]] 5 µM 0.274× (z -24.3) |
| [[Panc 03.27 (line)]] | alt | 289 | 7 (3 ⚠) | 4 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.88× (z +14.9) | [[Panobinostat (drug)]] 0.5 µM 0.261× (z -22.5) |
| [[A-427 (line)]] | wt | 563 | 4 (1 ⚠) | 6 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 1.95× (z +11.2) | [[Panobinostat (drug)]] 0.5 µM 0.268× (z -22.1) |
| [[NCI-H23 (line)]] | alt | 569 | 1 (1 ⚠) | 9 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.55× (z +10.4) ⚠ cell-cycle shift, explains ~0% of this change | [[Panobinostat (drug)]] 5 µM 0.229× (z -24.8) |
| [[HOP62 (line)]] | alt | 265 | 5 (1 ⚠) | 4 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.83× (z +13.7) | [[Panobinostat (drug)]] 5 µM 0.209× (z -25.0) |
| [[RKO (line)]] | wt | 346 | 0 | 9 (5 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.233× (z -20.4) |
| [[MIA PaCa-2 (line)]] | alt | 844 | 0 | 8 (5 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.184× (z -23.9) ⚠ toxic · without an alert: [[Panobinostat (drug)]] 5 µM 0.265× (z -19.5) |
| [[A549 (line)]] | wt | 314 | 0 | 7 (4 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.218× (z -21.9) |
| [[C32 (line)]] | wt | 510 | 0 | 7 (2 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.176× (z -18.1) |
| [[H4 (line)]] | wt | 938 | 0 | 7 (4 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.220× (z -20.0) |
| [[HT-29 (line)]] | alt | 409 | 3 | 4 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 1.88× (z +10.2) | [[Panobinostat (drug)]] 0.5 µM 0.213× (z -24.8) |
| [[NCI-H460 (line)]] | wt | 452 | 0 | 7 (4 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.216× (z -25.8) |
| [[A-172 (line)]] | wt | 362 | 0 | 6 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.367× (z -13.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~24% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.442× (z -12.6) |
| [[C-33 A (line)]] | alt | 486 | 0 | 6 (3 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.218× (z -22.2) |
| [[HepG2_C3A (line)]] | wt | 283 | 0 | 6 (3 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.179× (z -23.9) |
| [[LoVo (line)]] | wt | 270 | 5 (1 ⚠) | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.18× (z +18.8) | [[Panobinostat (drug)]] 0.5 µM 0.581× (z -9.2) |
| [[AsPC-1 (line)]] | alt | 245 | 3 (1 ⚠) | 2 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.89× (z +24.9) | [[Panobinostat (drug)]] 5 µM 0.345× (z -13.8) |
| [[HEC-1-A (line)]] | alt | 246 | 1 | 4 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 1.87× (z +10.2) | [[Panobinostat (drug)]] 5 µM 0.247× (z -23.0) |
| [[Hs 766T (line)]] | wt | 311 | 1 | 4 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.88× (z +12.5) | [[Panobinostat (drug)]] 0.5 µM 0.272× (z -18.2) |
| [[CFPAC-1 (line)]] | alt | 207 | 2 | 2 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.68× (z +10.2) | [[Panobinostat (drug)]] 5 µM 0.374× (z -13.6) |
| [[LOX-IMVI (line)]] | wt | 323 | 0 | 4 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.137× (z -30.5) |
| [[LS 180 (line)]] | wt | 183 | 2 (1 ⚠) | 2 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.74× (z +11.3) | [[Panobinostat (drug)]] 5 µM 0.373× (z -14.2) |
| [[NCI-H1573 (line)]] | alt | 214 | 0 | 4 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.428× (z -14.6) |
| [[NCI-H2030 (line)]] | alt | 409 | 0 | 4 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.319× (z -18.0) |
| [[RPMI-7951 (line)]] | alt | 301 | 1 | 3 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.39× (z +17.7) | [[Panobinostat (drug)]] 0.5 µM 0.371× (z -14.3) |
| [[SHP-77 (line)]] | alt | 414 | 0 | 4 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.160× (z -26.3) |
| [[SK-MEL-2 (line)]] | alt | 209 | 0 | 4 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.219× (z -17.8) |
| [[SW 900 (line)]] | alt | 157 | 1 | 3 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.70× (z +9.1) | [[Panobinostat (drug)]] 5 µM 0.303× (z -14.5) |
| [[A498 (line)]] | wt | 299 | 0 | 3 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.476× (z -11.5) |
| [[CHP-212 (line)]] | wt | 308 | 0 | 3 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.215× (z -15.2) |
| [[COLO 205 (line)]] | alt | 122 | 1 | 2 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.73× (z +15.7) | [[Panobinostat (drug)]] 0.5 µM 0.356× (z -11.4) |
| [[hTERT-HPNE (line)]] | wt | 206 | 0 | 3 | — | [[Panobinostat (drug)]] 5 µM 0.254× (z -14.4) |
| [[NCI-H1792 (line)]] | alt | 208 | 1 (1 ⚠) | 2 | [[Homoharringtonine (drug)]] 5 µM 1.72× (z +11.5) ⚠ cell-cycle shift, explains ~0% of this change | [[Panobinostat (drug)]] 5 µM 0.374× (z -14.9) |
| [[SNU-423 (line)]] | alt | 424 | 0 | 3 | — | [[Panobinostat (drug)]] 5 µM 0.191× (z -24.3) |
| [[SW 1271 (line)]] | alt | 482 | 0 | 3 (1 ⚠) | — | [[Docetaxel (drug)]] 0.05 µM 0.198× (z -12.9) ⚠ transcription drop · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.241× (z -11.3) |
| [[SW1417 (line)]] | alt | 304 | 0 | 3 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.436× (z -12.0) |
| [[HCT15 (line)]] | alt | 289 | 0 | 2 | — | [[Panobinostat (drug)]] 5 µM 0.388× (z -12.4) |
| [[J82 (line)]] | alt | 127 | 0 | 2 | — | [[Panobinostat (drug)]] 0.5 µM 0.397× (z -12.8) |
| [[NCI-H661 (line)]] | alt | 510 | 0 | 1 | — | [[Panobinostat (drug)]] 0.5 µM 0.317× (z -8.8) |
| [[AN3 CA (line)]] | alt | 146 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 21.0 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 56.1 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 108 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 255 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 20.6 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 301 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 27.3 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 325 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 82.8 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5836), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*31 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SATB2]] | +0.73 | +0.64 / +0.61 | both halves | 7e-06 |  |
| [[ASXL2]] | +0.56 | +0.52 / +0.44 | both halves | 3e-05 |  |
| [[CLOCK]] | +0.55 | +0.36 / +0.51 | both halves | 1e-04 |  |
| [[DPY19L1P1]] | +0.55 | +0.53 / +0.42 | both halves | 4e-05 |  |
| [[PKP4]] | +0.55 | +0.58 / +0.43 | both halves | 3e-05 |  |
| [[KDSR]] | +0.55 | +0.38 / +0.48 | both halves | 6e-05 |  |
| [[PTPRG]] | +0.54 | +0.51 / +0.43 | both halves | 3e-05 |  |
| [[ATXN2]] | +0.53 | +0.53 / +0.44 | both halves | 3e-05 |  |
| [[DGKH]] | +0.53 | +0.39 / +0.43 | both halves | 5e-05 |  |
| [[TSC22D1]] | +0.52 | +0.29 / +0.47 | both halves | 2e-04 |  |
| [[GNG12-AS1]] | +0.52 | +0.30 / +0.49 | both halves | 2e-04 |  |
| [[RFX3]] | +0.51 | +0.38 / +0.45 | both halves | 6e-05 |  |

## Genes that move opposite

*69 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[STRA6LP]] | -0.58 | -0.47 / -0.46 | both halves | 2e-05 |  |
| [[MRPS31P4]] | -0.58 | -0.52 / -0.44 | both halves | 3e-05 |  |
| [[MKRN2]] | -0.58 | -0.45 / -0.55 | both halves | 3e-05 | STRING 515 |
| [[HARS2]] | -0.58 | -0.50 / -0.44 | both halves | 3e-05 |  |
| [[BCAS2]] | -0.57 | -0.61 / -0.49 | both halves | 1e-05 |  |
| [[SLC35A3]] | -0.57 | -0.49 / -0.35 | both halves | 1e-04 |  |
| [[SUGT1P4-STRA6LP]] | -0.57 | -0.48 / -0.44 | both halves | 3e-05 |  |
| [[BBS5]] | -0.56 | -0.47 / -0.41 | both halves | 4e-05 |  |
| [[STAM]] | -0.56 | -0.40 / -0.50 | both halves | 4e-05 |  |
| [[OSBPL7]] | -0.56 | -0.40 / -0.47 | both halves | 4e-05 |  |
| [[TFIP11]] | -0.56 | -0.66 / -0.44 | both halves | 3e-05 |  |
| [[STX18]] | -0.55 | -0.44 / -0.44 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PKIG]] | B | PKIG activity raises IGF2BP3's level | lines that do not express PKIG (6) vs lines expressing it (44) | 2.38× lower at baseline in the lines without PKIG | 0.054 | ⚠ within organs, on part of the lines; also absent: GPR155, TTC7B, CIBAR1 |
| [[HDAC6]] | B | HDAC6 activity raises IGF2BP3's level | compounds that target HDAC6: 2 of 2 lower it (Belinostat, Panobinostat) | 100% of the class's compounds vs 1.7% of all compounds | 0.084 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[IRF6]] | B | IRF6 activity lowers IGF2BP3's level | lines that do not express IRF6 (31) vs lines expressing it (19) | 1.72× higher at baseline in the lines without IRF6 | 0.093 | ⚠ within organs, on part of the lines; co-absent genes; also absent: ST14, TMPRSS4, TMEM125 |

### Downstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| cells under [[Tomivosertib (drug)]] 5 µM | C | IGF2BP3 activity raises the cells' numbers under Tomivosertib 5 µM (protects the cells) | lines that do not express IGF2BP3 (4) vs lines expressing it (44) | the lines without IGF2BP3: 0.74× the cells of the other lines | 0.030 | ⚠ few lines (4 vs 46); tissue-confounded; across organs; also absent: CDK6, RGL1, UACA |

## Where it sits

- **Module**: [[Module 030]]; 146 genes; this gene is in the **-** arm (projection on the module's main direction -0.522). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.37).
- **Nodal map** (x, y) = (-3.8, -4.4); signed map (15.5, -6.7). **Vector** length 122, 37.7% of its response variance represented; |z| ≥ 3 in 1,348 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +10.8 | +9.4 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | +7.9 | +3.5 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | +7.3 | +2.9 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | +7.2 | +9.7 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | +7.0 | +8.4 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +6.1 | +1.0 |
|  | [[Afatinib (drug)]] 0.5 µM |  | +2.0 | +2.7 |
|  | [[Gefitinib (drug)]] 5 µM |  | +2.0 | +2.3 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | +2.0 | +2.8 |
|  | [[Diphenhydramine (drug)]] 0.5 µM |  | +1.8 | +1.5 |
| fall | [[Panobinostat (drug)]] 5 µM |  | -7.6 | -30.9 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | -7.4 | -31.1 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | -5.7 | -12.4 |
|  | [[Belinostat (drug)]] 5 µM |  | -4.9 | -18.0 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~24% of this change | -4.5 | -6.9 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -4.2 | -2.9 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | -3.9 | -2.3 |
|  | [[Ponatinib (drug)]] 5 µM |  | -3.4 | -3.8 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -3.1 | -2.7 |
|  | [[Trametinib (drug)]] 0.05 µM |  | -3.0 | -1.4 |

## What is on record

|  |  |
|---|---|
| Name | insulin like growth factor 2 mRNA binding protein 3 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 7p15.3 — chr7:23,310,209-23,470,491 (-) |
| Ensembl biotype | protein_coding |
| Also known as | IMP-3, CT98, IMP3 |
| Gene groups (HGNC) | RNA binding motif containing |
| Reactome | 2 pathways, smallest: Insulin-like Growth Factor-2 mRNA Binding Proteins (IGF2BPs/IMPs/VICKZs) bind RNA; Metabolism of RNA |
| Matched by | ensembl_id |

**Function**, from UniProt [O00425](https://www.uniprot.org/uniprotkb/O00425) (Insulin-like growth factor 2 mRNA-binding protein 3):

> RNA-binding factor that may recruit target transcripts to cytoplasmic protein-RNA complexes (mRNPs). This transcript 'caging' into mRNPs allows mRNA transport and transient storage. It also modulates the rate and location at which target transcripts encounter the translational apparatus and shields them from endonuclease attacks or microRNA-mediated degradation. Preferentially binds to N6-methyladenosine (m6A)-containing mRNAs and increases their stability. Binds to the 3'-UTR of CD44 mRNA and …

**Summary**, from NCBI Gene [10643](https://www.ncbi.nlm.nih.gov/gene/10643):

> The protein encoded by this gene is primarily found in the nucleolus, where it can bind to the 5' UTR of the insulin-like growth factor II leader 3 mRNA and may repress translation of insulin-like growth factor II during late development. The encoded protein contains several KH domains, which are important in RNA binding and are known to be involved in RNA synthesis and metabolism. A pseudogene exists on chromosome 7, and there are putative pseudogenes on other chromosomes. [provided by RefSeq, …

**Accessions** — [HGNC:28868](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:28868) · Entrez [10643](https://www.ncbi.nlm.nih.gov/gene/10643) · UniProt [O00425](https://www.uniprot.org/uniprotkb/O00425) · Ensembl [ENSG00000136231](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000136231)

## Data

Gene col 5836: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5836); `tables/drug_effects.parquet` (23 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5836, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5836]; `tensor/DDL_lfc|DDL_z.npy` [5836]; `embed/gene_vectors.npy` [5836]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5836 or target_col == 5836). Every well: [[IGF2BP3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/IGF2BP3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
