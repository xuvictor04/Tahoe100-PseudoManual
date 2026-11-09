---
symbol: "MAPK14"
type: "gene"
col: 3316
ensembl_id: "ENSG00000112062"
name: "mitogen-activated protein kinase 14"
location: "6p21.31"
module: 169
arm: "+"
pooled_cpm: 117.63
n_lines_expressing: 50
n_dd_up: 9
n_dd_down: 10
n_dd_up_clean: 9
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 1
direction_downstream: 5
tags: ["gene", "module/169"]
generated_by: "tahoemap"
---

# MAPK14

*mitogen-activated protein kinase 14* — 6p21.31

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 9 drug-doses (none with an alert); the strongest is [[TAK-901 (drug)]] 5 µM: 2.21× (z +7.2, q 4e-10, up in 35 of 49 measured lines).
> Pooled over the cell lines (median), lowered significantly by 10 drug-doses (8 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 0.532× (z -12.7, q 2e-34, down in 45 of 49 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Harringtonine (drug)]] 0.5 µM: 0.750× (z -5.8, q 5e-07, down in 34 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 7 here, 5 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 9 lines (NCI-H1573 0.133×, Panc 03.27 0.191×, LoVo 0.256×, HCT15 0.165×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.5 µM in 3 lines (SW480 0.319×, LS 180 0.295×, Panc 03.27 0.348×; ⚠ toxic; transcription drop); [[Auranofin (drug)]] 5 µM in 3 lines (SK-MEL-2 0.328×, MIA PaCa-2 0.419×, C32 0.429×); [[Harringtonine (drug)]] 0.5 µM in 2 lines (HOP62 0.473×, NCI-H1573 0.451×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CLASP1]] (+0.57, fdr 2e-05), [[PIK3R1]] (+0.56, fdr 5e-05), [[EPB41L4B]] (+0.52, fdr 3e-05); moves opposite to [[INHBA]] (-0.52, fdr 3e-05), [[TRAF1]] (-0.51, fdr 1e-05), [[DDX5]] (-0.51, fdr 3e-05).
> It is in [[Module 169]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[HDAC6]] → it (grade B ⚠); 5 go from it, the strongest it → [[ESRRA]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 17 in all, 2 with an alert ⚠. 9 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3316.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[TAK-901 (drug)]] 5 µM |  | **2.21×** | +7.2 | 4e-10 | 35/49 (PANC-1, KATO III, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Panobinostat (drug)]] 5 µM |  | **1.40×** | +6.8 | 4e-09 | 36/48 (PANC-1, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM |  | **1.32×** | +5.7 | 2e-06 | 34/48 (PANC-1, J82, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.31×** | +5.4 | 8e-06 | 32/48 (PANC-1, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ponatinib (drug)]] 5 µM |  | **1.29×** | +5.1 | 3e-05 | 32/48 (NCI-H23, LOX-IMVI, …) | rises with dose | position effect removed |
| [[Tucidinostat (drug)]] 5 µM |  | 1.17× | +4.6 | 4e-04 | 20/48 (J82, A498, …) | top dose only |  |
| [[PH-797804 (drug)]] 5 µM |  | **1.65×** | +4.5 | 5e-04 | 25/48 (LS 180, PANC-1, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Brivudine (drug)]] 5 µM |  | **1.60×** | +4.2 | 0.002 | 28/49 (PANC-1, J82, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.20×** | +3.8 | 0.011 | 22/48 (PANC-1, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Clobetasol propionate (drug)]] 0.5 µM |  | 1.20× | +3.7 | 0.013 | 19/48 (HOP62, H4, …) | all doses, flat |  |
| [[Radotinib (drug)]] 5 µM |  | 1.14× | +3.6 | 0.014 | 13/48 (NCI-H23, A498, …) | top dose only |  |
| [[Ralimetinib dimesylate (drug)]] 0.05 µM | ⚠ unreliable plate only | 1.18× | +3.3 | 0.042 | 12/48 (NCI-H1573, NCI-H1792, …) | inconsistent across doses |  |
| [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.17× | +3.2 | 0.055 | 17/48 (NCI-H23, NCI-H460, …) | rises with dose |  |
| [[Ipatasertib (drug)]] 5 µM |  | **1.42×** | +3.2 | 0.055 | 13/48 (PANC-1, LOX-IMVI, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Dexamethasone (drug)]] 0.5 µM |  | 1.16× | +3.1 | 0.076 | 19/48 (SW 900, HOP62, …) | inconsistent across doses |  |
| [[Bentamapimod (drug)]] 0.05 µM |  | 1.17× | +3.1 | 0.076 | 10/47 (NCI-H460, PANC-1, …) | inconsistent across doses |  |
| [[Clobetasol propionate (drug)]] 5 µM |  | 1.16× | +3.0 | 0.095 | 18/48 (HOP62, H4, …) | all doses, flat |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 10 with an alert ⚠. 10 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 3316.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 7 here, 5 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 9 lines (NCI-H1573 0.133×, Panc 03.27 0.191×, LoVo 0.256×, HCT15 0.165×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.5 µM in 3 lines (SW480 0.319×, LS 180 0.295×, Panc 03.27 0.348×; ⚠ toxic; transcription drop); [[Auranofin (drug)]] 5 µM in 3 lines (SK-MEL-2 0.328×, MIA PaCa-2 0.419×, C32 0.429×); [[Harringtonine (drug)]] 0.5 µM in 2 lines (HOP62 0.473×, NCI-H1573 0.451×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.532×** | -12.7 | 2e-34 | 45/49 (SW480, LS 180, …) | all doses, flat | cell-cycle shift (explains ~10% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.530×** | -11.8 | 6e-30 | 38/45 (HepG2/C3A, SNU-423, …) | all doses, flat | cell-cycle shift (explains ~5% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.544×** | -11.8 | 6e-30 | 36/44 (NCI-H1573, Panc 03.27, …) | all doses, flat | cell-cycle shift (explains ~8% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~24% of this change | **0.713×** | -6.8 | 1e-09 | 31/48 (HepG2/C3A, AsPC-1, …) | rises with dose | composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.723×** | -6.5 | 7e-09 | 32/48 (HepG2/C3A, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~21% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.739×** | -5.9 | 4e-07 | 34/47 (HepG2/C3A, CFPAC-1, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.750×** | -5.8 | 5e-07 | 34/48 (HOP62, NCI-H1573, …) | inconsistent across doses | cell-cycle shift (explains ~14% here) |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **0.780×** | -5.0 | 4e-05 | 31/48 (AsPC-1, HS-578T, …) | inconsistent across doses |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~42% of this change | **0.815×** | -4.1 | 0.002 | 26/48 (Panc 03.27, NCI-H2347, …) | inconsistent across doses | low cells (technical?) |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.945× | -3.9 | 0.005 | 1/50 (NCI-H2122) | inconsistent across doses |  |
| [[Belumosudil (drug)]] 5 µM |  | **0.829×** | -3.6 | 0.014 | 21/48 (A-172, LS 180, …) | top dose only |  |
| [[Isocorydine (drug)]] 0.5 µM |  | 0.838× | -3.6 | 0.018 | 21/48 (NCI-H661, Hs 766T, …) | inconsistent across doses |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | 0.843× | -3.4 | 0.025 | 20/48 (A-172, C32, …) | inconsistent across doses |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~31% of this change | 0.844× | -3.4 | 0.027 | 22/48 (HepG2/C3A, HOP62, …) | rises with dose |  |
| [[Vilanterol (drug)]] 5 µM |  | 0.899× | -3.0 | 0.093 | 4/49 (A-427, J82, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.04 per unit of S-phase module lfc, -0.20 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3316. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HepG2_C3A (line)]] | wt | 250 | 0 | 11 (11 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.209× (z -18.2) ⚠ toxic |
| [[AsPC-1 (line)]] | alt | 106 | 0 | 7 (7 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.237× (z -14.9) ⚠ toxic; transcription drop |
| [[PANC-1 (line)]] | alt | 94.8 | 2 | 3 (3 ⚠) | [[TAK-901 (drug)]] 5 µM 3.98× (z +9.4) | [[Dinaciclib (drug)]] 0.5 µM 0.530× (z -9.7) ⚠ toxic; transcription drop |
| [[KATO III (line)]] | alt | 145 | 1 | 3 (3 ⚠) | [[TAK-901 (drug)]] 5 µM 4.23× (z +8.6) | [[Dinaciclib (drug)]] 5 µM 0.317× (z -14.8) ⚠ toxic; transcription drop |
| [[NCI-H1573 (line)]] | alt | 56.7 | 0 | 4 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.133× (z -21.1) ⚠ toxic; transcription drop · without an alert: [[Harringtonine (drug)]] 0.5 µM 0.451× (z -8.6) |
| [[NCI-H460 (line)]] | wt | 79.6 | 0 | 4 (4 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.247× (z -17.7) ⚠ toxic; transcription drop |
| [[SNU-423 (line)]] | alt | 182 | 0 | 4 (4 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.294× (z -14.6) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 93.0 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.288× (z -14.5) ⚠ toxic; transcription drop |
| [[HEC-1-A (line)]] | alt | 178 | 1 (1 ⚠) | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.52× (z +9.1) ⚠ cell-cycle shift, would explain all of this change | [[Dinaciclib (drug)]] 0.5 µM 0.496× (z -10.9) ⚠ toxic; transcription drop |
| [[HOP62 (line)]] | alt | 124 | 0 | 3 (2 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.439× (z -10.0) ⚠ cell-cycle shift, explains ~24% of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 0.473× (z -9.1) |
| [[HS-578T (line)]] | alt | 103 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.324× (z -11.0) ⚠ toxic; transcription drop |
| [[HT-29 (line)]] | alt | 138 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.395× (z -11.6) ⚠ toxic; transcription drop |
| [[LS 180 (line)]] | wt | 231 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.295× (z -15.1) ⚠ toxic; transcription drop |
| [[Panc 03.27 (line)]] | alt | 196 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.191× (z -21.0) ⚠ toxic; transcription drop |
| [[SW480 (line)]] | alt | 184 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.319× (z -15.3) ⚠ toxic; transcription drop |
| [[A-427 (line)]] | wt | 93.8 | 1 | 1 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 5.04× (z +8.5) | [[Dinaciclib (drug)]] 0.05 µM 0.295× (z -13.2) ⚠ toxic; transcription drop |
| [[CFPAC-1 (line)]] | alt | 129 | 0 | 2 (2 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.422× (z -10.2) ⚠ toxic |
| [[NCI-H23 (line)]] | alt | 106 | 1 (1 ⚠) | 1 (1 ⚠) | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 2.14× (z +8.9) ⚠ cell-cycle shift, explains ~15% of this change | [[Dinaciclib (drug)]] 5 µM 0.360× (z -11.8) ⚠ toxic; transcription drop |
| [[SK-MEL-2 (line)]] | alt | 80.8 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.292× (z -11.5) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.328× (z -11.3) |
| [[SNU-1 (line)]] | wt | 130 | 0 | 2 (2 ⚠) | — | [[LY-2584702 (tosylate salt) (drug)]] 5 µM 0.0765× (z -11.8) ⚠ toxic |
| [[SW48 (line)]] | wt | 140 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.289× (z -11.9) ⚠ toxic; transcription drop |
| [[A549 (line)]] | wt | 70.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.380× (z -10.7) ⚠ toxic; transcription drop |
| [[C32 (line)]] | wt | 82.4 | 0 | 1 | — | [[Auranofin (drug)]] 5 µM 0.429× (z -8.7) |
| [[COLO 205 (line)]] | alt | 110 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.304× (z -11.2) ⚠ toxic; transcription drop |
| [[H4 (line)]] | wt | 95.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.233× (z -11.3) ⚠ toxic; transcription drop |
| [[HCT15 (line)]] | alt | 131 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.165× (z -18.0) ⚠ toxic; transcription drop |
| [[J82 (line)]] | alt | 93.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.381× (z -11.3) ⚠ toxic; transcription drop |
| [[LoVo (line)]] | wt | 138 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.256× (z -19.0) ⚠ toxic; transcription drop |
| [[LOX-IMVI (line)]] | wt | 103 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.387× (z -9.9) ⚠ toxic; transcription drop |
| [[MIA PaCa-2 (line)]] | alt | 122 | 0 | 1 | — | [[Auranofin (drug)]] 5 µM 0.419× (z -9.3) |
| [[NCI-H2347 (line)]] | alt | 122 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.451× (z -9.1) ⚠ toxic |
| [[RKO (line)]] | wt | 142 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.80× (z +9.2) ⚠ cell-cycle shift, would explain all of this change | — |
| [[RPMI-7951 (line)]] | alt | 94.4 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.416× (z -8.5) ⚠ cell-cycle shift, explains ~27% of this change |
| [[A498 (line)]] | wt | 65.3 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 150 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 99.6 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 120 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 93.0 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 85.3 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 76.4 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 99.8 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 96.4 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 116 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 115 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 113 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 98.8 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 83.0 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 135 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 86.5 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 127 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3316), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*74 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CLASP1]] | +0.57 | +0.58 / +0.48 | both halves | 2e-05 | pathway: Cell Cycle Checkpoints |
| [[PIK3R1]] | +0.56 | +0.39 / +0.64 | both halves | 5e-05 | pathway: Platelet activation, signaling and aggregation |
| [[EPB41L4B]] | +0.52 | +0.46 / +0.48 | both halves | 3e-05 |  |
| [[GRB2]] | +0.51 | +0.49 / +0.50 | both halves | 1e-05 | pathway: Leishmania infection; STRING 631 |
| [[CCDC6]] | +0.51 | +0.56 / +0.47 | both halves | 2e-05 |  |
| [[SPATC1L]] | +0.51 | +0.48 / +0.47 | both halves | 2e-05 |  |
| [[PPP3R1]] | +0.51 | +0.53 / +0.50 | both halves | 1e-05 | STRING 431 |
| [[PSMA6]] | +0.51 | +0.54 / +0.38 | both halves | 6e-05 | pathway: Cell Cycle Checkpoints |
| [[LRRC1]] | +0.51 | +0.49 / +0.48 | both halves | 2e-05 |  |
| [[SHROOM2]] | +0.50 | +0.43 / +0.52 | both halves | 3e-05 | pathway: HALLMARK_APICAL_JUNCTION |
| [[PARGP1]] | +0.50 | +0.49 / +0.47 | both halves | 2e-05 |  |
| [[GRAMD2B]] | +0.49 | +0.49 / +0.42 | both halves | 4e-05 |  |

## Genes that move opposite

*26 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[INHBA]] | -0.52 | -0.45 / -0.61 | both halves | 3e-05 |  |
| [[TRAF1]] | -0.51 | -0.49 / -0.51 | both halves | 1e-05 | pathway: HALLMARK_APICAL_JUNCTION |
| [[DDX5]] | -0.51 | -0.46 / -0.49 | both halves | 3e-05 |  |
| [[LIF]] | -0.50 | -0.44 / -0.54 | both halves | 3e-05 |  |
| [[DPH1-AS1]] | -0.50 | -0.53 / -0.37 | both halves | 8e-05 |  |
| [[ALG13]] | -0.49 | -0.45 / -0.45 | both halves | 3e-05 |  |
| [[PLA2G4C]] | -0.48 | -0.48 / -0.39 | both halves | 5e-05 |  |
| [[LINC00944]] | -0.48 | -0.45 / -0.49 | both halves | 3e-05 |  |
| [[LINC01060]] | -0.48 | -0.53 / -0.42 | both halves | 4e-05 |  |
| [[KDM6B]] | -0.47 | -0.47 / -0.42 | both halves | 4e-05 | pathway: Cellular Senescence |
| [[HDAC9]] | -0.46 | -0.40 / -0.46 | both halves | 5e-05 |  |
| [[LINC01010]] | -0.46 | -0.41 / -0.45 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HDAC6]] | B | HDAC6 activity lowers MAPK14's level | compounds that target HDAC6: 2 of 2 raise it (Belinostat, Panobinostat) | 100% of the class's compounds vs 2.0% of all compounds | 0.095 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

*5 arrows, 5 of them with an alert ⚠; grade A 0, B 5, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ESRRA]] | B | MAPK14 activity raises ESRRA's level | compounds that target MAPK14: 2 of 2 lower it (PH-797804, Ralimetinib dimesylate) | 100% of the class's compounds vs 0.8% of all compounds | 0.044 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[DLGAP1]] | B | MAPK14 activity raises DLGAP1's level | compounds that target MAPK14: 2 of 2 lower it (PH-797804, Ralimetinib dimesylate) | 100% of the class's compounds vs 1.4% of all compounds | 0.071 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[TSFM]] | B | MAPK14 activity lowers TSFM's level | compounds that target MAPK14: 2 of 2 raise it (PH-797804, Ralimetinib dimesylate) | 100% of the class's compounds vs 1.4% of all compounds | 0.071 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[NFATC2IP]] | B | MAPK14 activity raises NFATC2IP's level | compounds that target MAPK14: 2 of 2 lower it (PH-797804, Ralimetinib dimesylate) | 100% of the class's compounds vs 1.7% of all compounds | 0.084 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[TSEN34]] | B | MAPK14 activity raises TSEN34's level | compounds that target MAPK14: 2 of 2 lower it (PH-797804, Ralimetinib dimesylate) | 100% of the class's compounds vs 1.7% of all compounds | 0.084 | ⚠ off-target possible; 2 compounds; artifact flags |

## Where it sits

- **Module**: [[Module 169]]; 25 genes; every member is in the + arm (projection on the module's main direction 0.526). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.25; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (23.8, 15.0); signed map (-20.0, 17.9). **Vector** length 103, 30.7% of its response variance represented; |z| ≥ 3 in 1,159 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[TAK-901 (drug)]] 5 µM |  | +7.2 | +7.2 |
|  | [[PH-797804 (drug)]] 5 µM |  | +4.8 | +4.5 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift | +4.2 | +2.6 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | +3.8 | +3.1 |
|  | [[Radotinib (drug)]] 5 µM |  | +3.7 | +3.6 |
|  | [[Dexamethasone (drug)]] 5 µM |  | +3.4 | +1.4 |
|  | [[Ponatinib (drug)]] 5 µM |  | +3.2 | +5.1 |
| fall | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~27% of this change | -5.4 | -5.0 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -4.1 | -3.4 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | -3.6 | -11.8 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~24% of this change | -3.3 | -6.8 |
|  | [[Belumosudil (drug)]] 5 µM |  | -3.1 | -3.6 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -3.0 | -1.6 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -2.8 | -1.9 |
|  | [[Temsirolimus (drug)]] 0.05 µM |  | -2.3 | -1.4 |

## What is on record

|  |  |
|---|---|
| Name | mitogen-activated protein kinase 14 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 6p21.31 — chr6:36,027,782-36,111,236 (+) |
| Ensembl biotype | protein_coding |
| Also known as | p38alpha, PRKM14, p38, Mxi2, PRKM15; previously CSPB1, CSBP1, CSBP2 |
| Gene groups (HGNC) | Mitogen-activated protein kinase 11-14 (p38) family |
| Hallmark sets | UV_RESPONSE_DN, APICAL_JUNCTION, G2M_CHECKPOINT |
| Reactome | 74 pathways, smallest: CD163 mediating an anti-inflammatory response; Activation of PPARGC1A (PGC-1alpha) by phosphorylation; Activation of the AP-1 family of transcription factors |
| Matched by | ensembl_id |

**Function**, from UniProt [Q16539](https://www.uniprot.org/uniprotkb/Q16539) (Mitogen-activated protein kinase 14):

> Serine/threonine kinase which acts as an essential component of the MAP kinase signal transduction pathway. MAPK14 is one of the four p38 MAPKs which play an important role in the cascades of cellular responses evoked by extracellular stimuli such as pro-inflammatory cytokines or physical stress leading to direct activation of transcription factors. Accordingly, p38 MAPKs phosphorylate a broad range of proteins and it has been estimated that they may have approximately 200 to 300 substrates …

**Summary**, from NCBI Gene [1432](https://www.ncbi.nlm.nih.gov/gene/1432):

> The protein encoded by this gene is a member of the MAP kinase family. MAP kinases act as an integration point for multiple biochemical signals, and are involved in a wide variety of cellular processes such as proliferation, differentiation, transcription regulation and development. This kinase is activated by various environmental stresses and proinflammatory cytokines. The activation requires its phosphorylation by MAP kinase kinases (MKKs), or its autophosphorylation triggered by the …

**Accessions** — [HGNC:6876](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:6876) · Entrez [1432](https://www.ncbi.nlm.nih.gov/gene/1432) · UniProt [Q16539](https://www.uniprot.org/uniprotkb/Q16539) · Ensembl [ENSG00000112062](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000112062)

## Data

Gene col 3316: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3316); `tables/drug_effects.parquet` (32 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3316, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3316]; `tensor/DDL_lfc|DDL_z.npy` [3316]; `embed/gene_vectors.npy` [3316]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3316 or target_col == 3316). Every well: [[MAPK14 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MAPK14.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
