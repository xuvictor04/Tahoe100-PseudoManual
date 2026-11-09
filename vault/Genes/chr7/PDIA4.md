---
symbol: "PDIA4"
type: "gene"
col: 7910
ensembl_id: "ENSG00000155660"
name: "protein disulfide isomerase family A member 4"
location: "7q36.1"
module: 42
arm: "+"
pooled_cpm: 168.43
n_lines_expressing: 50
n_dd_up: 12
n_dd_down: 12
n_dd_up_clean: 5
n_dd_down_clean: 11
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/042"]
generated_by: "tahoemap"
---

# PDIA4

*protein disulfide isomerase family A member 4* — 7q36.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 12 drug-doses (7 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 2.88× (z +12.8, q 1e-34, up in 47 of 49 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change. The strongest without an alert is [[Panobinostat (drug)]] 0.5 µM: 2.70× (z +12.0, q 1e-30, up in 45 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 12 drug-doses (1 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.336× (z -18.3, q 0e+00, down in 48 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[HSP90B1]] (+0.92, fdr 7e-06), [[CALR]] (+0.88, fdr 7e-06), [[PDIA6]] (+0.88, fdr 7e-06); moves opposite to [[TRIM47]] (-0.65, fdr 1e-05), [[ITPA]] (-0.61, fdr 1e-05), [[RPL7L1]] (-0.60, fdr 1e-05).
> It is in [[Module 042]], a single-armed module (UPR ER).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[AGR2]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 7 with an alert ⚠. 12 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7910.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change | **2.88×** | +12.8 | 1e-34 | 47/49 (PANC-1, A-427, …) | all doses, stronger at high dose | composition shift |
| [[Panobinostat (drug)]] 0.5 µM |  | **2.70×** | +12.0 | 1e-30 | 45/48 (A-172, HOP62, …) | two highest doses | cell-cycle shift (explains ~19% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | **2.46×** | +10.4 | 3e-23 | 42/44 (PANC-1, A549, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change | **2.05×** | +8.0 | 2e-13 | 38/45 (NCI-H2030, PANC-1, …) | all doses, stronger at high dose | composition shift |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~35% of this change | **1.84×** | +7.3 | 3e-11 | 42/48 (HOP62, NCI-H1792, …) | two highest doses |  |
| [[Tucidinostat (drug)]] 5 µM |  | **1.36×** | +5.2 | 1e-05 | 35/48 (NCI-H23, SHP-77, …) | rises with dose | position effect removed |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~47% of this change | **1.51×** | +5.0 | 5e-05 | 32/48 (HOP62, A-172, …) | top dose only |  |
| [[Lipoic acid (drug)]] 5 µM |  | **1.30×** | +4.4 | 7e-04 | 33/48 (SW480, PANC-1, …) | top dose only | position effect removed |
| [[HI-TOPK-032 (drug)]] 5 µM |  | **1.90×** | +4.1 | 0.003 | 36/48 (A-427, SW480, …) | rises with dose | noisy plate (z scaled) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~31% of this change | **1.37×** | +3.8 | 0.009 | 30/48 (Hs 766T, SW1417, …) | inconsistent across doses | low cells (technical?); position effect removed |
| [[Auranofin (drug)]] 5 µM |  | **1.34×** | +3.5 | 0.022 | 27/48 (LOX-IMVI, HT-29, …) | top dose only | position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~36% of this change | **1.22×** | +3.4 | 0.032 | 28/49 (NCI-H2347, LOX-IMVI, …) | top dose only |  |
| [[S-Adenosyl-L-methionine (disulfate tosylate) (drug)]] 5 µM |  | 1.20× | +3.0 | 0.11 | 21/49 (NCI-H2347, CFPAC-1, …) | inconsistent across doses | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 1 with an alert ⚠. 12 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 7910.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.336×** | -18.3 | 0e+00 | 48/48 (KATO III, H4, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.292×** | -14.8 | 0e+00 | 44/48 (A-427, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.363×** | -11.8 | 1e-29 | 47/48 (KATO III, AN3 CA, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.428×** | -10.2 | 2e-22 | 45/48 (HS-578T, A-172, …) | all doses, stronger at high dose |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.517×** | -7.9 | 2e-13 | 42/48 (KATO III, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 0.05 µM |  | **0.622×** | -5.3 | 1e-05 | 41/47 (HS-578T, A-172, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **0.654×** | -5.1 | 3e-05 | 40/48 (C32, KATO III, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Rapamycin (drug)]] 5 µM |  | **0.751×** | -4.8 | 1e-04 | 38/48 (C32, RPMI-7951, …) | rises with dose | position effect removed |
| [[5-Azacytidine (drug)]] 5 µM |  | **0.692×** | -4.4 | 6e-04 | 36/48 (J82, HS-578T, …) | top dose only |  |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~38% of this change | **0.768×** | -4.4 | 6e-04 | 32/48 (RPMI-7951, NCI-H2030, …) | top dose only | low cells (technical?) |
| [[GSK1059615 (drug)]] 5 µM |  | **0.509×** | -4.3 | 0.001 | 35/49 (J82, A-427, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Temsirolimus (drug)]] 0.05 µM |  | **0.757×** | -3.3 | 0.039 | 28/49 (CFPAC-1, C32, …) | inconsistent across doses | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.32 per unit of S-phase module lfc, +0.09 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7910. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HOP62 (line)]] | alt | 227 | 5 (4 ⚠) | 5 | [[Panobinostat (drug)]] 0.5 µM 5.89× (z +14.8) | [[Homoharringtonine (drug)]] 5 µM 0.226× (z -17.3) |
| [[A-172 (line)]] | wt | 148 | 4 (3 ⚠) | 5 | [[Panobinostat (drug)]] 0.5 µM 5.22× (z +15.2) | [[Homoharringtonine (drug)]] 5 µM 0.185× (z -21.7) |
| [[HS-578T (line)]] | alt | 200 | 3 (2 ⚠) | 5 | [[Panobinostat (drug)]] 0.5 µM 4.13× (z +12.9) | [[Homoharringtonine (drug)]] 5 µM 0.292× (z -15.8) |
| [[A-427 (line)]] | wt | 120 | 4 (4 ⚠) | 3 | [[Dinaciclib (drug)]] 0.5 µM 6.00× (z +15.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change | [[Homoharringtonine (drug)]] 0.5 µM 0.0319× (z -29.6) |
| [[NCI-H2030 (line)]] | alt | 120 | 4 (3 ⚠) | 3 | [[Dinaciclib (drug)]] 0.5 µM 4.18× (z +14.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 2.50× (z +9.3) | [[Homoharringtonine (drug)]] 5 µM 0.423× (z -12.2) |
| [[A498 (line)]] | wt | 242 | 3 (2 ⚠) | 3 | [[Dinaciclib (drug)]] 0.5 µM 3.45× (z +12.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 3.01× (z +10.9) | [[Homoharringtonine (drug)]] 5 µM 0.253× (z -19.0) |
| [[A549 (line)]] | wt | 79.5 | 4 (3 ⚠) | 2 | [[Dinaciclib (drug)]] 0.5 µM 5.71× (z +14.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 3.51× (z +10.7) | [[Homoharringtonine (drug)]] 0.05 µM 0.352× (z -8.9) |
| [[H4 (line)]] | wt | 302 | 2 (1 ⚠) | 4 | [[Panobinostat (drug)]] 0.5 µM 3.98× (z +11.9) | [[Homoharringtonine (drug)]] 5 µM 0.112× (z -26.4) |
| [[hTERT-HPNE (line)]] | wt | 146 | 2 (1 ⚠) | 4 | [[Dinaciclib (drug)]] 0.5 µM 3.74× (z +9.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 3.44× (z +8.5) | [[Homoharringtonine (drug)]] 0.05 µM 0.206× (z -10.7) |
| [[J82 (line)]] | alt | 154 | 3 (2 ⚠) | 3 | [[Dinaciclib (drug)]] 5 µM 3.74× (z +12.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 2.64× (z +9.7) | [[Homoharringtonine (drug)]] 5 µM 0.188× (z -23.6) |
| [[KATO III (line)]] | alt | 505 | 0 | 6 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.125× (z -28.1) |
| [[NCI-H1792 (line)]] | alt | 188 | 2 (1 ⚠) | 4 | [[Panobinostat (drug)]] 0.5 µM 5.96× (z +14.0) | [[Homoharringtonine (drug)]] 0.5 µM 0.171× (z -13.8) |
| [[NCI-H460 (line)]] | wt | 198 | 1 (1 ⚠) | 5 | [[Dinaciclib (drug)]] 0.5 µM 3.40× (z +9.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change | [[Homoharringtonine (drug)]] 5 µM 0.233× (z -15.2) |
| [[PANC-1 (line)]] | alt | 146 | 4 (3 ⚠) | 2 | [[Dinaciclib (drug)]] 0.5 µM 4.08× (z +16.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 2.98× (z +12.6) | [[Homoharringtonine (drug)]] 0.05 µM 0.446× (z -9.4) |
| [[RPMI-7951 (line)]] | alt | 114 | 2 (1 ⚠) | 4 | [[Panobinostat (drug)]] 0.5 µM 3.34× (z +9.7) | [[Homoharringtonine (drug)]] 5 µM 0.156× (z -21.0) |
| [[C-33 A (line)]] | alt | 113 | 3 (3 ⚠) | 2 | [[Dinaciclib (drug)]] 0.5 µM 3.98× (z +12.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change | [[Homoharringtonine (drug)]] 5 µM 0.262× (z -17.4) |
| [[C32 (line)]] | wt | 495 | 0 | 5 | — | [[Homoharringtonine (drug)]] 5 µM 0.139× (z -15.9) |
| [[CFPAC-1 (line)]] | alt | 220 | 2 (1 ⚠) | 3 | [[Panobinostat (drug)]] 0.5 µM 3.03× (z +9.6) | [[Homoharringtonine (drug)]] 5 µM 0.315× (z -13.9) |
| [[NCI-H23 (line)]] | alt | 177 | 3 (2 ⚠) | 2 | [[Panobinostat (drug)]] 0.5 µM 4.86× (z +11.0) | [[Homoharringtonine (drug)]] 5 µM 0.307× (z -11.6) |
| [[NCI-H2347 (line)]] | alt | 204 | 0 | 5 | — | [[Homoharringtonine (drug)]] 5 µM 0.211× (z -21.3) |
| [[LOX-IMVI (line)]] | wt | 63.0 | 4 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 8.14× (z +14.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 4.59× (z +10.8) | — |
| [[NCI-H1573 (line)]] | alt | 113 | 2 (1 ⚠) | 2 | [[Panobinostat (drug)]] 0.5 µM 5.08× (z +11.5) | [[Homoharringtonine (drug)]] 5 µM 0.232× (z -14.5) |
| [[SW 1088 (line)]] | alt | 418 | 1 | 3 | [[Panobinostat (drug)]] 0.5 µM 7.37× (z +9.5) | [[Homoharringtonine (drug)]] 5 µM 0.156× (z -12.4) |
| [[Panc 03.27 (line)]] | alt | 117 | 2 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 3.11× (z +9.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | [[Homoharringtonine (drug)]] 5 µM 0.415× (z -10.2) |
| [[SNU-1 (line)]] | wt | 74.9 | 1 (1 ⚠) | 2 | [[Dinaciclib (drug)]] 0.5 µM 4.81× (z +9.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change | [[Homoharringtonine (drug)]] 5 µM 0.193× (z -14.3) |
| [[SW1417 (line)]] | alt | 158 | 2 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 2.73× (z +10.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change | [[Homoharringtonine (drug)]] 5 µM 0.528× (z -9.4) |
| [[SW480 (line)]] | alt | 99.4 | 2 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 3.52× (z +13.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change | [[Homoharringtonine (drug)]] 5 µM 0.483× (z -10.5) |
| [[AN3 CA (line)]] | alt | 161 | 0 | 2 | — | [[Harringtonine (drug)]] 5 µM 0.123× (z -14.7) |
| [[AsPC-1 (line)]] | alt | 72.7 | 2 (1 ⚠) | 0 | [[Panobinostat (drug)]] 0.5 µM 3.65× (z +10.2) | — |
| [[BT-474 (line)]] | alt | 115 | 0 | 2 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.215× (z -12.4) |
| [[CHP-212 (line)]] | wt | 88.6 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.195× (z -11.1) |
| [[HCT15 (line)]] | alt | 224 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.153× (z -17.4) |
| [[HEC-1-A (line)]] | alt | 113 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.361× (z -9.7) |
| [[HepG2_C3A (line)]] | wt | 102 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 3.03× (z +8.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change | [[Homoharringtonine (drug)]] 5 µM 0.313× (z -12.4) |
| [[Hs 766T (line)]] | wt | 105 | 2 (1 ⚠) | 0 | [[Panobinostat (drug)]] 0.5 µM 3.84× (z +10.8) | — |
| [[HT-29 (line)]] | alt | 317 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.205× (z -15.3) |
| [[LS 180 (line)]] | wt | 260 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.262× (z -13.3) |
| [[MIA PaCa-2 (line)]] | alt | 179 | 1 | 1 | [[Panobinostat (drug)]] 0.5 µM 3.05× (z +8.6) | [[Homoharringtonine (drug)]] 5 µM 0.240× (z -15.4) |
| [[RKO (line)]] | wt | 128 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.426× (z -11.2) |
| [[SHP-77 (line)]] | alt | 82.8 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 2.80× (z +9.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change | [[Homoharringtonine (drug)]] 5 µM 0.351× (z -12.9) |
| [[SK-MEL-2 (line)]] | alt | 67.4 | 2 (1 ⚠) | 0 | [[Panobinostat (drug)]] 0.5 µM 4.81× (z +10.8) | — |
| [[SNU-423 (line)]] | alt | 64.4 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.66× (z +11.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change | — |
| [[SW 900 (line)]] | alt | 171 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.252× (z -13.1) |
| [[SW48 (line)]] | wt | 160 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.59× (z +10.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change | — |
| [[LoVo (line)]] | wt | 159 | 0 | 1 | — | [[Harringtonine (drug)]] 5 µM 0.298× (z -8.8) |
| [[NCI-H661 (line)]] | alt | 197 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.205× (z -9.7) |
| [[COLO 205 (line)]] | alt | 170 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 145 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 150 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 123 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7910), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*87 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[HSP90B1]] | +0.92 | +0.92 / +0.90 | both halves | 7e-06 | STRING 998 |
| [[CALR]] | +0.88 | +0.87 / +0.85 | both halves | 7e-06 | STRING 973 |
| [[PDIA6]] | +0.88 | +0.90 / +0.86 | both halves | 7e-06 | same gene group; STRING 893 |
| [[P4HB]] | +0.87 | +0.87 / +0.81 | both halves | 7e-06 | same gene group; STRING 799 |
| [[HSPA5]] | +0.84 | +0.84 / +0.82 | both halves | 7e-06 | STRING 990 |
| [[HYOU1]] | +0.81 | +0.79 / +0.85 | both halves | 7e-06 | STRING 997 |
| [[TMED9]] | +0.80 | +0.80 / +0.72 | both halves | 7e-06 |  |
| [[CALU]] | +0.79 | +0.77 / +0.73 | both halves | 7e-06 | STRING 660 |
| [[LMAN1]] | +0.79 | +0.80 / +0.71 | both halves | 7e-06 | STRING 556 |
| [[MANF]] | +0.78 | +0.75 / +0.80 | both halves | 7e-06 | STRING 821 |
| [[PDIA3]] | +0.78 | +0.85 / +0.82 | both halves | 7e-06 | same gene group; STRING 784 |
| [[SEC61A1]] | +0.77 | +0.83 / +0.71 | both halves | 7e-06 | STRING 681 |

## Genes that move opposite

*13 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TRIM47]] | -0.65 | -0.59 / -0.55 | both halves | 1e-05 |  |
| [[ITPA]] | -0.61 | -0.55 / -0.55 | both halves | 1e-05 |  |
| [[RPL7L1]] | -0.60 | -0.58 / -0.55 | both halves | 1e-05 |  |
| [[C1orf131]] | -0.60 | -0.56 / -0.51 | both halves | 1e-05 |  |
| [[ZFY]] | -0.60 | -0.46 / -0.55 | both halves | 3e-05 |  |
| [[ZNF480]] | -0.60 | -0.64 / -0.53 | both halves | 1e-05 |  |
| [[RPP38]] | -0.60 | -0.53 / -0.53 | both halves | 1e-05 |  |
| [[PBDC1]] | -0.60 | -0.54 / -0.49 | both halves | 1e-05 |  |
| [[METTL18]] | -0.59 | -0.51 / -0.53 | both halves | 1e-05 |  |
| [[CCDC137]] | -0.59 | -0.60 / -0.55 | both halves | 1e-05 |  |
| [[MIER3]] | -0.59 | -0.52 / -0.50 | both halves | 1e-05 |  |
| [[NNT-AS1]] | -0.59 | -0.55 / -0.45 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[AGR2]] | B | AGR2 activity weakens PDIA4's drug response | lines that do not express AGR2 (32) vs lines expressing it (17) | the lines without AGR2 respond 1.22× as strongly (z diff -1.14); strongest at Dinaciclib 5 µM: 2.77x vs 1.90x (z diff -2.8) | 0.059 | ⚠ within organs, on part of the lines; also absent: FXYD3, SERPINB5, PRKCH-AS1; target measured in part of the lines; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 042]] — UPR ER; 103 genes; every member is in the + arm (projection on the module's main direction 0.899). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.26; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (14.3, -30.7); signed map (-54.2, 7.2). **Vector** length 149, 53.5% of its response variance represented; |z| ≥ 3 in 1,342 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *Asparagine N-linked glycosylation* (reactome, mean cos +0.55 to 23); *Maturation of DENV proteins* (reactome, mean cos +0.74 to 11); *Dengue Virus Genome Translation and Replication* (reactome, mean cos +0.73 to 12).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Panobinostat (drug)]] 0.5 µM |  | +8.7 | +12.0 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~35% of this change | +8.4 | +7.3 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~47% of this change | +7.0 | +5.0 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +6.3 | +5.2 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +4.6 | +2.1 |
|  | [[PH-797804 (drug)]] 5 µM |  | +3.3 | +1.1 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | +3.1 | +4.1 |
|  | [[Brivudine (drug)]] 5 µM |  | +2.8 | +0.8 |
|  | [[Lipoic acid (drug)]] 5 µM |  | +2.4 | +4.4 |
| fall | [[Harringtonine (drug)]] 5 µM |  | -11.0 | -11.8 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -10.6 | -7.9 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -10.1 | -10.2 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -9.5 | -14.8 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | -7.7 | -18.3 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -6.1 | -5.3 |
|  | [[Temsirolimus (drug)]] 0.05 µM |  | -4.0 | -3.3 |
|  | [[Rapamycin (drug)]] 5 µM |  | -3.9 | -4.8 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -3.8 | -4.4 |

## What is on record

|  |  |
|---|---|
| Name | protein disulfide isomerase family A member 4 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 7q36.1 — chr7:149,003,062-149,028,662 (-) |
| Ensembl biotype | protein_coding |
| Also known as | ERP70, ERP72 |
| Gene groups (HGNC) | Protein disulfide isomerases |
| Matched by | ensembl_id |

UniProt [P13667](https://www.uniprot.org/uniprotkb/P13667) carries no function annotation.

**Summary**, from NCBI Gene [9601](https://www.ncbi.nlm.nih.gov/gene/9601):

> This gene encodes a member of the disulfide isomerase (PDI) family of endoplasmic reticulum (ER) proteins that catalyze protein folding and thiol-disulfide interchange reactions. The encoded protein has an N-terminal ER-signal sequence, three catalytically active thioredoxin (TRX) domains, two TRX-like domains and a C-terminal ER-retention sequence. This protein, when bound to cyclophilin B, enhances the rate of immunoglobulin G intermolecular disulfide bonding and antibody assembly. [provided …

**Accessions** — [HGNC:30167](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:30167) · Entrez [9601](https://www.ncbi.nlm.nih.gov/gene/9601) · UniProt [P13667](https://www.uniprot.org/uniprotkb/P13667) · Ensembl [ENSG00000155660](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000155660)

## Data

Gene col 7910: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7910); `tables/drug_effects.parquet` (25 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7910, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7910]; `tensor/DDL_lfc|DDL_z.npy` [7910]; `embed/gene_vectors.npy` [7910]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7910 or target_col == 7910). Every well: [[PDIA4 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PDIA4.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
