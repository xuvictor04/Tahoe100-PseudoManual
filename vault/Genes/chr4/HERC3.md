---
symbol: "HERC3"
type: "gene"
col: 6201
ensembl_id: "ENSG00000138641"
name: "HECT and RLD domain containing E3 ubiquitin protein ligase 3"
location: "4q22.1"
module: 164
arm: "+"
pooled_cpm: 75.21
n_lines_expressing: 48
n_dd_up: 17
n_dd_down: 17
n_dd_up_clean: 16
n_dd_down_clean: 10
in_vector_space: true
direction_upstream: 4
direction_downstream: 0
tags: ["gene", "module/164"]
generated_by: "tahoemap"
---

# HERC3

*HECT and RLD domain containing E3 ubiquitin protein ligase 3* — 4q22.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 17 drug-doses (1 with an alert ⚠); the strongest is [[Tucidinostat (drug)]] 5 µM: 1.74× (z +9.1, q 4e-17, up in 43 of 46 measured lines).
> Pooled over the cell lines (median), lowered significantly by 17 drug-doses (7 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.233× (z -24.1, q 0e+00, down in 45 of 46 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[HDAC3]] (+0.78, fdr 7e-06), [[PDK1]] (+0.78, fdr 7e-06), [[PDK3]] (+0.78, fdr 7e-06); moves opposite to [[ZNF140]] (-0.64, fdr 1e-05), [[FKRP]] (-0.64, fdr 3e-05), [[ST7L]] (-0.64, fdr 1e-05).
> It is in [[Module 164]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 4 arrows point to it, the strongest [[RAB20]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 17 in all, 1 with an alert ⚠; shown: the 15 strongest. 17 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6201.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 5 µM |  | **1.74×** | +9.1 | 4e-17 | 43/46 (KATO III, MIA PaCa-2, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.70×** | +6.2 | 1e-07 | 31/46 (BT-474, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here) |
| [[Belinostat (drug)]] 5 µM |  | **1.65×** | +5.8 | 1e-06 | 28/46 (NCI-H23, SK-MEL-2, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.60×** | +5.5 | 6e-06 | 35/47 (C32, SK-MEL-2, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 5 µM |  | **1.57×** | +5.3 | 1e-05 | 27/46 (SK-MEL-2, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here) |
| [[TAK-901 (drug)]] 5 µM |  | **2.11×** | +4.6 | 5e-04 | 27/47 (NCI-H23, NCI-H1792, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.41×** | +4.0 | 0.005 | 25/46 (NCI-H23, MIA PaCa-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Brivudine (drug)]] 5 µM |  | **1.81×** | +3.6 | 0.019 | 26/47 (A-427, SK-MEL-2, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Ponatinib (drug)]] 5 µM |  | **1.34×** | +3.4 | 0.036 | 23/46 (SW48, LoVo, …) | inconsistent across doses |  |
| [[PF-06260933 (drug)]] 5 µM |  | **1.74×** | +3.4 | 0.037 | 22/46 (SW480, SHP-77, …) | top dose only | noisy plate (z scaled) |
| [[palbociclib (drug)]] 0.5 µM |  | **1.52×** | +3.4 | 0.037 | 26/46 (H4, HOP62, …) | inconsistent across doses | cell-cycle shift (explains ~8% here); noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **1.67×** | +3.2 | 0.069 | 24/46 (HOP62, A-172, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Dimethyl fumarate (drug)]] 5 µM |  | **1.32×** | +3.1 | 0.069 | 20/47 (HT-29, HEC-1-A, …) | top dose only | plate-row cell shift |
| [[Flumatinib (mesylate) (drug)]] 5 µM |  | **1.32×** | +3.1 | 0.069 | 18/46 (LOX-IMVI, KATO III, …) | top dose only |  |
| [[Tomivosertib (drug)]] 5 µM |  | **1.66×** | +3.1 | 0.069 | 23/46 (HT-29, SHP-77, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 17 in all, 7 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 17 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 6201.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.233×** | -24.1 | 0e+00 | 45/46 (NCI-H1792, C32, …) | rises with dose | cell-cycle shift (explains ~9% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.260×** | -15.8 | 0e+00 | 44/46 (C32, LOX-IMVI, …) | rises with dose | cell-cycle shift (explains ~6% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.335×** | -12.3 | 2e-32 | 41/46 (LOX-IMVI, C32, …) | rises with dose | cell-cycle shift (explains ~10% here); composition shift |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.395×** | -10.4 | 2e-23 | 40/45 (C32, C-33 A, …) | top dose only | cell-cycle shift (explains ~4% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.451×** | -9.3 | 2e-18 | 41/47 (CFPAC-1, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.462×** | -8.7 | 4e-16 | 34/39 (SK-MEL-2, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here); composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.482×** | -8.2 | 2e-14 | 42/45 (CFPAC-1, HCT15, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **0.657×** | -4.9 | 6e-05 | 28/46 (CFPAC-1, HOP62, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 5 µM |  | **0.749×** | -4.8 | 1e-04 | 30/46 (SK-MEL-2, SNU-423, …) | top dose only | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Lucanthone (drug)]] 5 µM |  | **0.688×** | -4.2 | 0.002 | 33/47 (NCI-H2347, LOX-IMVI, …) | top dose only |  |
| [[Auranofin (drug)]] 5 µM |  | **0.712×** | -4.0 | 0.004 | 25/46 (HOP62, J82, …) | top dose only |  |
| [[Megestrol (drug)]] 5 µM |  | **0.795×** | -3.8 | 0.007 | 24/47 (SK-MEL-2, A-427, …) | inconsistent across doses |  |
| [[5-Azacytidine (drug)]] 5 µM |  | **0.737×** | -3.6 | 0.016 | 24/46 (NCI-H460, NCI-H1573, …) | top dose only |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~31% of this change | **0.748×** | -3.4 | 0.028 | 25/46 (SW1417, HCT15, …) | inconsistent across doses | low cells (technical?) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.738×** | -3.3 | 0.039 | 22/42 (NCI-H2347, RKO, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 0.05 µM |  | **0.772×** | -3.0 | 0.086 | 20/46 (NCI-H2347, SK-MEL-2, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.10 per unit of S-phase module lfc, -0.23 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6201. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[C32 (line)]] | wt | 150 | 1 | 7 (4 ⚠) | [[Tucidinostat (drug)]] 5 µM 2.39× (z +10.4) | [[Homoharringtonine (drug)]] 5 µM 0.110× (z -26.3) |
| [[CFPAC-1 (line)]] | alt | 218 | 0 | 8 (6 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.193× (z -20.8) |
| [[SK-MEL-2 (line)]] | alt | 101 | 3 | 5 (2 ⚠) | [[Panobinostat (drug)]] 5 µM 3.81× (z +9.5) | [[Homoharringtonine (drug)]] 5 µM 0.0864× (z -24.6) |
| [[HOP62 (line)]] | alt | 157 | 2 (1 ⚠) | 5 (3 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 4.20× (z +9.7) ⚠ cell-cycle shift, explains ~49% of this change · without an alert: [[PH-797804 (drug)]] 5 µM 13.9× (z +9.3) | [[Homoharringtonine (drug)]] 5 µM 0.122× (z -20.2) |
| [[A-172 (line)]] | wt | 63.9 | 1 | 5 (2 ⚠) | [[Tucidinostat (drug)]] 5 µM 2.22× (z +8.6) | [[Homoharringtonine (drug)]] 5 µM 0.117× (z -22.8) |
| [[HCT15 (line)]] | alt | 178 | 0 | 6 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0860× (z -22.2) |
| [[HEC-1-A (line)]] | alt | 112 | 0 | 6 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.274× (z -11.8) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.348× (z -10.0) |
| [[NCI-H23 (line)]] | alt | 34.5 | 4 (1 ⚠) | 2 (1 ⚠) | [[Panobinostat (drug)]] 0.5 µM 4.19× (z +10.2) | [[Homoharringtonine (drug)]] 5 µM 0.178× (z -17.3) |
| [[NCI-H2347 (line)]] | alt | 138 | 0 | 6 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.203× (z -20.4) |
| [[Hs 766T (line)]] | wt | 208 | 0 | 5 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.136× (z -21.2) |
| [[SW48 (line)]] | wt | 129 | 0 | 5 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.205× (z -13.4) |
| [[H4 (line)]] | wt | 182 | 0 | 4 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.119× (z -16.4) |
| [[LoVo (line)]] | wt | 58.3 | 1 (1 ⚠) | 3 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.89× (z +12.4) ⚠ cell-cycle shift, explains ~59% of this change | [[Homoharringtonine (drug)]] 5 µM 0.304× (z -14.1) |
| [[MIA PaCa-2 (line)]] | alt | 19.4 | 3 | 1 | [[Tucidinostat (drug)]] 5 µM 4.03× (z +11.6) | [[Homoharringtonine (drug)]] 0.5 µM 0.154× (z -11.0) |
| [[NCI-H1573 (line)]] | alt | 81.8 | 0 | 4 (1 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.104× (z -15.4) |
| [[SW480 (line)]] | alt | 55.6 | 1 (1 ⚠) | 3 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.50× (z +9.2) ⚠ cell-cycle shift, explains ~49% of this change | [[Homoharringtonine (drug)]] 5 µM 0.360× (z -14.7) |
| [[AN3 CA (line)]] | alt | 125 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.126× (z -11.2) |
| [[HS-578T (line)]] | alt | 73.2 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.176× (z -16.2) |
| [[HT-29 (line)]] | alt | 52.4 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.280× (z -12.6) |
| [[J82 (line)]] | alt | 58.7 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.154× (z -20.5) |
| [[KATO III (line)]] | alt | 62.3 | 1 | 2 | [[Tucidinostat (drug)]] 5 µM 2.97× (z +12.5) | [[Homoharringtonine (drug)]] 0.5 µM 0.305× (z -9.7) |
| [[LOX-IMVI (line)]] | wt | 60.2 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.0990× (z -23.9) |
| [[NCI-H1792 (line)]] | alt | 129 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0586× (z -28.4) |
| [[NCI-H2030 (line)]] | alt | 39.0 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.168× (z -19.4) |
| [[NCI-H460 (line)]] | wt | 46.9 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.223× (z -16.9) |
| [[RKO (line)]] | wt | 47.2 | 1 (1 ⚠) | 2 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.02× (z +11.1) ⚠ cell-cycle shift, explains ~59% of this change | [[Dinaciclib (drug)]] 0.05 µM 0.180× (z -11.2) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.296× (z -8.6) |
| [[RPMI-7951 (line)]] | alt | 96.0 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.0956× (z -24.0) |
| [[SNU-1 (line)]] | wt | 116 | 0 | 3 (2 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.227× (z -9.8) ⚠ cell-cycle shift, explains ~30% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.253× (z -9.1) |
| [[SNU-423 (line)]] | alt | 43.4 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.152× (z -18.3) |
| [[SW 900 (line)]] | alt | 58.5 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.198× (z -14.7) |
| [[A549 (line)]] | wt | 29.5 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.270× (z -13.0) |
| [[AsPC-1 (line)]] | alt | 37.8 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.230× (z -14.2) |
| [[BT-474 (line)]] | alt | 46.2 | 2 | 0 | [[Panobinostat (drug)]] 0.5 µM 5.55× (z +11.0) | — |
| [[CHP-212 (line)]] | wt | 98.6 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.125× (z -14.5) |
| [[hTERT-HPNE (line)]] | wt | 83.7 | 0 | 2 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.147× (z -12.6) |
| [[Panc 03.27 (line)]] | alt | 70.4 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.163× (z -19.9) |
| [[A498 (line)]] | wt | 28.7 | 1 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.20× (z +14.8) ⚠ cell-cycle shift, explains ~59% of this change | — |
| [[C-33 A (line)]] | alt | 42.6 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.0952× (z -12.4) ⚠ toxic |
| [[COLO 205 (line)]] | alt | 62.3 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.310× (z -10.5) |
| [[HepG2_C3A (line)]] | wt | 49.5 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.155× (z -12.4) |
| [[LS 180 (line)]] | wt | 115 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.255× (z -8.9) ⚠ toxic; transcription drop |
| [[SW 1088 (line)]] | alt | 94.2 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0440× (z -10.0) |
| [[SW1417 (line)]] | alt | 43.2 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.324× (z -9.3) ⚠ toxic |
| [[A-427 (line)]] | wt | 32.0 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 98.8 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 88.2 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 15.9 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 18.3 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 50.8 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 72.7 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6201), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*88 of its nearest partners move with it, 2 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 2 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[HDAC3]] | +0.78 | +0.77 / +0.74 | both halves | 7e-06 |  |
| [[PDK1]] | +0.78 | +0.86 / +0.64 | both halves | 7e-06 |  |
| [[PDK3]] | +0.78 | +0.84 / +0.66 | both halves | 7e-06 |  |
| [[INSIG2]] | +0.77 | +0.83 / +0.63 | both halves | 7e-06 |  |
| [[FAM13A]] | +0.76 | +0.80 / +0.66 | both halves | 7e-06 | STRING 578; ⚠ same locus (17.4 kb: neighbours can correlate without regulation) |
| [[SMAP2]] | +0.74 | +0.70 / +0.69 | both halves | 7e-06 |  |
| [[FAM13A-AS1]] | +0.74 | +0.72 / +0.71 | both halves | 7e-06 | ⚠ same locus (0.8 kb, same strand: neighbours can correlate without regulation) |
| [[YEATS2]] | +0.73 | +0.80 / +0.59 | both halves | 7e-06 |  |
| [[SAP30-DT]] | +0.73 | +0.75 / +0.69 | both halves | 7e-06 |  |
| [[MXI1]] | +0.72 | +0.78 / +0.59 | both halves | 7e-06 |  |
| [[P4HA1]] | +0.70 | +0.75 / +0.59 | both halves | 7e-06 |  |
| [[PEX3]] | +0.70 | +0.75 / +0.54 | both halves | 1e-05 |  |
| [[KDM3A]] | +0.69 | +0.75 / +0.60 | both halves | 7e-06 |  |
| [[WDR45B]] | +0.69 | +0.75 / +0.53 | both halves | 1e-05 |  |

## Genes that move opposite

*12 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZNF140]] | -0.64 | -0.56 / -0.62 | both halves | 1e-05 |  |
| [[FKRP]] | -0.64 | -0.69 / -0.44 | both halves | 3e-05 |  |
| [[ST7L]] | -0.64 | -0.66 / -0.51 | both halves | 1e-05 |  |
| [[NME6]] | -0.61 | -0.64 / -0.53 | both halves | 1e-05 |  |
| [[AFG3L1P]] | -0.60 | -0.63 / -0.45 | both halves | 3e-05 |  |
| [[INO80]] | -0.60 | -0.52 / -0.55 | both halves | 1e-05 |  |
| [[FIZ1]] | -0.60 | -0.62 / -0.46 | both halves | 3e-05 |  |
| [[SRCAP]] | -0.60 | -0.52 / -0.55 | both halves | 1e-05 |  |
| [[TTC27]] | -0.59 | -0.54 / -0.53 | both halves | 1e-05 |  |
| [[PPP3CB-AS1]] | -0.58 | -0.59 / -0.45 | both halves | 3e-05 |  |
| [[RAB30-DT]] | -0.58 | -0.61 / -0.42 | both halves | 4e-05 |  |
| [[ZNF764]] | -0.57 | -0.56 / -0.45 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 4, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[RAB20]] | B | RAB20 activity raises HERC3's level | lines that do not express RAB20 (8) vs lines expressing it (42) | 2.27× lower at baseline in the lines without RAB20 | 0.014 | ⚠ within organs, on part of the lines; also absent: RPS6KA2, PRDX2, YPEL3; maybe low, not absent |
| [[GLRX]] | B | GLRX activity raises HERC3's level | lines that do not express GLRX (10) vs lines expressing it (40) | 1.76× lower at baseline in the lines without GLRX | 0.058 | ⚠ within organs, on part of the lines; also absent: DUSP10, FES, DGKG; maybe low, not absent |
| [[CASZ1]] | B | CASZ1 activity lowers HERC3's level | lines that do not express CASZ1 (10) vs lines expressing it (40) | 1.63× higher at baseline in the lines without CASZ1 | 0.076 | ⚠ within organs, on part of the lines; also absent: SBK1, CPLX1, LLGL2; maybe low, not absent |
| [[NDRG1]] | B | NDRG1 activity raises HERC3's level | lines that do not express NDRG1 (6) vs lines expressing it (44) | 2.15× lower at baseline in the lines without NDRG1 | 0.092 | ⚠ within organs, on part of the lines; also absent: SMOX, DELEC1, SLC2A1 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 164]]; 26 genes; every member is in the + arm (projection on the module's main direction 0.827). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.37; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (11.1, -17.1); signed map (-36.3, 23.6). **Vector** length 141, 47.9% of its response variance represented; |z| ≥ 3 in 1,335 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +9.5 | +9.1 |
|  | [[Belinostat (drug)]] 5 µM |  | +7.9 | +5.8 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | +7.6 | +4.0 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +7.5 | +5.5 |
|  | [[Panobinostat (drug)]] 5 µM |  | +6.7 | +5.3 |
|  | [[Brivudine (drug)]] 5 µM |  | +5.5 | +3.6 |
|  | [[Radotinib (drug)]] 5 µM |  | +5.4 | +2.8 |
|  | [[Ponatinib (drug)]] 5 µM |  | +4.2 | +3.4 |
|  | [[PF-06260933 (drug)]] 5 µM |  | +3.9 | +3.4 |
| fall | [[Homoharringtonine (drug)]] 5 µM |  | -10.7 | -24.1 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -8.3 | -15.8 |
|  | [[Harringtonine (drug)]] 5 µM |  | -7.5 | -12.3 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -5.2 | -3.6 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | -5.1 | -4.9 |
|  | [[GSK1059615 (drug)]] 5 µM |  | -3.8 | -2.0 |
|  | [[Temsirolimus (drug)]] 0.05 µM |  | -3.8 | -2.8 |
|  | [[Rapamycin (drug)]] 5 µM |  | -3.4 | -2.3 |
|  | [[Retinoic acid (drug)]] 0.05 µM |  | -2.9 | -2.7 |

## What is on record

|  |  |
|---|---|
| Name | HECT and RLD domain containing E3 ubiquitin protein ligase 3 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 4q22.1 — chr4:88,592,434-88,708,541 (+) |
| Ensembl biotype | protein_coding |
| Also known as | KIAA0032 |
| Gene groups (HGNC) | HECT and RLD domain containing E3 ubiquitin protein ligases |
| Hallmark sets | ANDROGEN_RESPONSE |
| Reactome | 3 pathways, smallest: Antigen processing: Ubiquitination & Proteasome degradation; Class I MHC mediated antigen processing & presentation; Adaptive Immune System |
| Matched by | ensembl_id |

**Function**, from UniProt [Q15034](https://www.uniprot.org/uniprotkb/Q15034) (Probable E3 ubiquitin-protein ligase HERC3):

> E3 ubiquitin-protein ligase which accepts ubiquitin from an E2 ubiquitin-conjugating enzyme in the form of a thioester and then directly transfers the ubiquitin to targeted substrates.

**Summary**, from NCBI Gene [8916](https://www.ncbi.nlm.nih.gov/gene/8916):

> This gene encodes a member the HERC ubiquitin ligase family. The encoded protein is located in the cytosol and binds ubiquitin via a HECT domain. Mutations in this gene have been associated with colorectal and gastric carcinomas. Alternatively spliced transcript variants encoding multiple isoforms have been observed for this gene. [provided by RefSeq, Oct 2012]

**Accessions** — [HGNC:4876](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:4876) · Entrez [8916](https://www.ncbi.nlm.nih.gov/gene/8916) · UniProt [Q15034](https://www.uniprot.org/uniprotkb/Q15034) · Ensembl [ENSG00000138641](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000138641)

## Data

Gene col 6201: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6201); `tables/drug_effects.parquet` (34 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6201, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6201]; `tensor/DDL_lfc|DDL_z.npy` [6201]; `embed/gene_vectors.npy` [6201]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6201 or target_col == 6201). Every well: [[HERC3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/HERC3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
