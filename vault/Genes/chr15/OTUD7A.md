---
symbol: "OTUD7A"
type: "gene"
col: 9874
ensembl_id: "ENSG00000169918"
name: "OTU deubiquitinase 7A"
location: "15q13.3"
module: 115
arm: "+"
pooled_cpm: 20.48
n_lines_expressing: 44
n_dd_up: 20
n_dd_down: 2
n_dd_up_clean: 18
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 5
direction_downstream: 7
tags: ["gene", "module/115"]
generated_by: "tahoemap"
---

# OTUD7A

*OTU deubiquitinase 7A* — 15q13.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 20 drug-doses (2 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 10.6× (z +43.4, q 0e+00, up in 41 of 41 measured lines).
> Pooled over the cell lines (median), lowered significantly by 2 drug-doses (none with an alert); the strongest is [[TAK-901 (drug)]] 5 µM: 0.612× (z -4.7, q 0.001, down in 15 of 40 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 11 here, 6 with an alert ⚠; the 6 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.5 µM in 5 lines (NCI-H2030 0.101×, LoVo 0.251×, AN3 CA 0.0662×, SW1417 0.267×, …; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change); [[Dinaciclib (drug)]] 5 µM in 2 lines (NCI-H2030 0.159×, SK-MEL-2 0.156×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change); [[Topotecan (hydrochloride) (drug)]] 5 µM in 2 lines (SW1417 0.274×, NCI-H2030 0.292×; ⚠ toxic; cell-cycle shift, explains ~0% of this change); [[TAK-901 (drug)]] 5 µM in 2 lines (LoVo 0.165×, SW1417 0.192×); [[Glycyrrhizic acid (drug)]] 0.05 µM in 1 line (AN3 CA 0.0865×); [[Citalopram (hydrobromide) (drug)]] 0.5 µM in 1 line (LS 180 0.0662×).
> Its strongest partners by |cos| (80 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 22 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[APBA1]] (+0.63, fdr 7e-05), [[EML6]] (+0.61, fdr 2e-05), [[STRBP]] (+0.56, fdr 2e-05); moves opposite to [[MAIP1]] (-0.53, fdr 3e-04), [[GANC]] (-0.53, fdr 6e-04), [[MTHFSD]] (-0.53, fdr 3e-04).
> It is in [[Module 115]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 5 arrows point to it, the strongest [[BSN]] → it (grade B ⚠); 7 go from it, the strongest it → [[KRBA2]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 28 in all, 5 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 20 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9874.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **10.6×** | +43.4 | 0e+00 | 41/41 (LoVo, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **9.84×** | +42.0 | 0e+00 | 41/41 (NCI-H460, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here) |
| [[Belinostat (drug)]] 5 µM |  | **7.60×** | +37.2 | 0e+00 | 41/41 (LoVo, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~3% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **3.86×** | +35.1 | 0e+00 | 40/42 (NCI-H460, HT-29, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **4.25×** | +26.6 | 0e+00 | 41/41 (SW480, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **2.82×** | +19.0 | 0e+00 | 38/40 (NCI-H460, C32, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Brivudine (drug)]] 5 µM |  | **5.83×** | +16.9 | 0e+00 | 40/42 (LoVo, NCI-H460, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.56×** | +11.6 | 2e-29 | 23/40 (NCI-H460, A549, …) | rises with dose | cell-cycle shift (explains ~11% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **1.78×** | +10.6 | 3e-24 | 28/38 (LoVo, SW1417, …) | rises with dose | cell-cycle shift (explains ~3% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.36×** | +8.0 | 8e-14 | 19/41 (BT-474, SW480, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **1.46×** | +6.9 | 2e-10 | 24/41 (NCI-H460, SW48, …) | top dose only |  |
| [[HI-TOPK-032 (drug)]] 5 µM |  | **1.79×** | +5.6 | 9e-07 | 14/37 (LoVo, NCI-H460, …) | top dose only | noisy plate (z scaled) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~22% of this change | **1.36×** | +5.4 | 2e-06 | 12/38 (NCI-H460, AN3 CA, …) | rises with dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~24% of this change | **1.33×** | +5.2 | 7e-06 | 13/41 (BT-474, RKO, …) | rises with dose |  |
| [[GSK1059615 (drug)]] 5 µM |  | **1.64×** | +4.8 | 7e-05 | 9/41 (SK-MEL-2, NCI-H2030, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[5-Azacytidine (drug)]] 5 µM |  | **1.26×** | +4.3 | 6e-04 | 9/41 (LoVo, RKO, …) | top dose only |  |
| [[Auranofin (drug)]] 5 µM |  | **1.25×** | +4.1 | 0.001 | 10/41 (MIA PaCa-2, SK-MEL-2, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, 2 with an alert ⚠. 2 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 9874.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 11 here, 6 with an alert ⚠; the 6 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.5 µM in 5 lines (NCI-H2030 0.101×, LoVo 0.251×, AN3 CA 0.0662×, SW1417 0.267×, …; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change); [[Dinaciclib (drug)]] 5 µM in 2 lines (NCI-H2030 0.159×, SK-MEL-2 0.156×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change); [[Topotecan (hydrochloride) (drug)]] 5 µM in 2 lines (SW1417 0.274×, NCI-H2030 0.292×; ⚠ toxic; cell-cycle shift, explains ~0% of this change); [[TAK-901 (drug)]] 5 µM in 2 lines (LoVo 0.165×, SW1417 0.192×); [[Glycyrrhizic acid (drug)]] 0.05 µM in 1 line (AN3 CA 0.0865×); [[Citalopram (hydrobromide) (drug)]] 0.5 µM in 1 line (LS 180 0.0662×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[TAK-901 (drug)]] 5 µM |  | **0.612×** | -4.7 | 0.001 | 15/40 (LoVo, SW1417, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~10% here); composition shift; noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.819×** | -3.7 | 0.062 | 16/41 (NCI-H2030, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Vilanterol (drug)]] 5 µM |  | 0.871× | -3.6 | 0.062 | 4/41 (LOX-IMVI, SW48, …) | top dose only |  |
| [[Sulfatinib (drug)]] 5 µM |  | 0.829× | -3.3 | 0.13 | 8/41 (A-427, NCI-H2030, …) | top dose only |  |
| [[Glycyrrhizic acid (drug)]] 5 µM |  | 0.840× | -3.1 | 0.18 | 10/40 (C32, CFPAC-1, …) | top dose only |  |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.888× | -3.1 | 0.18 | 15/42 (SW1417, BT-474, …) | top dose only | low cells (technical?) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~0% of this change | 0.841× | -3.1 | 0.18 | 12/35 (SW1417, NCI-H2030, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.20 per unit of S-phase module lfc, -0.26 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9874. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LoVo (line)]] | wt | 73.0 | 7 | 3 (2 ⚠) | [[Panobinostat (drug)]] 5 µM 5.73× (z +19.0) | [[Dinaciclib (drug)]] 0.5 µM 0.251× (z -15.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 0.165× (z -10.3) |
| [[NCI-H2030 (line)]] | alt | 52.6 | 4 | 5 (5 ⚠) | [[Panobinostat (drug)]] 5 µM 4.52× (z +13.2) | [[Dinaciclib (drug)]] 0.5 µM 0.101× (z -20.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[NCI-H460 (line)]] | wt | 8.02 | 8 (1 ⚠) | 0 | [[Tucidinostat (drug)]] 5 µM 9.81× (z +19.3) | — |
| [[SW1417 (line)]] | alt | 69.1 | 5 | 3 (2 ⚠) | [[Panobinostat (drug)]] 5 µM 2.93× (z +10.5) | [[Dinaciclib (drug)]] 0.5 µM 0.267× (z -13.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 0.192× (z -8.5) |
| [[A549 (line)]] | wt | 22.5 | 6 | 0 | [[Panobinostat (drug)]] 0.5 µM 10.4× (z +15.7) | — |
| [[SK-MEL-2 (line)]] | alt | 65.0 | 4 | 2 (2 ⚠) | [[Panobinostat (drug)]] 0.5 µM 4.74× (z +9.0) | [[Dinaciclib (drug)]] 5 µM 0.156× (z -10.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change |
| [[SW48 (line)]] | wt | 47.0 | 4 | 2 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 6.81× (z +11.0) | [[DT-061 (drug)]] 5 µM 0.0512× (z -9.0) |
| [[SW480 (line)]] | alt | 18.1 | 6 | 0 | [[Panobinostat (drug)]] 0.5 µM 8.03× (z +15.5) | — |
| [[BT-474 (line)]] | alt | 45.4 | 5 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.36× (z +12.2) | — |
| [[C-33 A (line)]] | alt | 57.3 | 3 | 2 (2 ⚠) | [[Panobinostat (drug)]] 0.5 µM 5.33× (z +11.7) | [[Dinaciclib (drug)]] 0.05 µM 0.168× (z -11.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change |
| [[C32 (line)]] | wt | 12.0 | 5 | 0 | [[Tucidinostat (drug)]] 5 µM 10.2× (z +14.2) | — |
| [[HEC-1-A (line)]] | alt | 10.5 | 5 | 0 | [[Panobinostat (drug)]] 0.5 µM 15.1× (z +15.5) | — |
| [[HOP62 (line)]] | alt | 9.30 | 5 | 0 | [[Panobinostat (drug)]] 5 µM 18.8× (z +15.2) | — |
| [[HT-29 (line)]] | alt | 11.4 | 5 | 0 | [[Panobinostat (drug)]] 5 µM 18.7× (z +15.9) | — |
| [[LS 180 (line)]] | wt | 5.49 | 4 | 1 | [[Tucidinostat (drug)]] 5 µM 9.57× (z +12.1) | [[Citalopram (hydrobromide) (drug)]] 0.5 µM 0.0662× (z -10.2) |
| [[NCI-H1792 (line)]] | alt | 7.62 | 5 | 0 | [[Panobinostat (drug)]] 5 µM 21.2× (z +12.2) | — |
| [[Panc 03.27 (line)]] | alt | 6.63 | 5 | 0 | [[Panobinostat (drug)]] 5 µM 17.2× (z +11.2) | — |
| [[RKO (line)]] | wt | 19.7 | 5 | 0 | [[Tucidinostat (drug)]] 5 µM 4.84× (z +12.9) | — |
| [[A-172 (line)]] | wt | 9.14 | 3 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 8.89× (z +10.8) | [[Docetaxel (drug)]] 0.05 µM 0.0803× (z -12.5) ⚠ transcription drop; cell-cycle shift, would explain all of this change |
| [[A498 (line)]] | wt | 5.70 | 4 | 0 | [[Panobinostat (drug)]] 5 µM 19.0× (z +14.7) | — |
| [[J82 (line)]] | alt | 7.34 | 4 | 0 | [[Panobinostat (drug)]] 5 µM 12.2× (z +11.4) | — |
| [[MIA PaCa-2 (line)]] | alt | 14.7 | 4 | 0 | [[Panobinostat (drug)]] 5 µM 7.19× (z +11.2) | — |
| [[NCI-H1573 (line)]] | alt | 28.9 | 4 | 0 | [[Panobinostat (drug)]] 5 µM 7.18× (z +14.6) | — |
| [[NCI-H23 (line)]] | alt | 26.8 | 4 | 0 | [[Panobinostat (drug)]] 5 µM 6.71× (z +13.3) | — |
| [[PANC-1 (line)]] | alt | 12.0 | 4 | 0 | [[Panobinostat (drug)]] 5 µM 6.88× (z +14.2) | — |
| [[RPMI-7951 (line)]] | alt | 8.65 | 4 | 0 | [[Panobinostat (drug)]] 5 µM 22.0× (z +10.7) | — |
| [[SNU-423 (line)]] | alt | 5.35 | 4 | 0 | [[Panobinostat (drug)]] 5 µM 20.9× (z +10.7) | — |
| [[A-427 (line)]] | wt | 28.6 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 4.05× (z +9.5) | — |
| [[AN3 CA (line)]] | alt | 75.7 | 0 | 3 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0662× (z -14.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change · without an alert: [[Glycyrrhizic acid (drug)]] 0.05 µM 0.0865× (z -11.6) |
| [[CFPAC-1 (line)]] | alt | 7.36 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 15.2× (z +12.7) | — |
| [[COLO 205 (line)]] | alt | 9.72 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 10.9× (z +9.4) | — |
| [[LOX-IMVI (line)]] | wt | 17.2 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 5.95× (z +11.4) | — |
| [[SW 900 (line)]] | alt | 12.1 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 14.5× (z +11.0) | — |
| [[HepG2_C3A (line)]] | wt | 8.01 | 2 | 0 | [[Panobinostat (drug)]] 5 µM 16.4× (z +8.7) | — |
| [[SNU-1 (line)]] | wt | 28.3 | 2 | 0 | [[Panobinostat (drug)]] 5 µM 10.8× (z +11.1) | — |
| [[H4 (line)]] | wt | 6.74 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 24.0× (z +9.5) | — |
| [[SHP-77 (line)]] | alt | 127 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.364× (z -10.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[AsPC-1 (line)]] | alt | 4.25 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 7.37 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 8.70 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 5.08 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 4.76 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 4.67 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 3.13 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 31.3 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 4.68 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 22.8 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 12.1 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 7.70 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 11.8 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9874), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*73 of its nearest partners move with it, 13 of them with an alert (⚠; 11 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[APBA1]] | +0.63 | +0.38 / +0.71 | both halves | 7e-05 |  |
| [[EML6]] | +0.61 | +0.48 / +0.64 | both halves | 2e-05 |  |
| [[STRBP]] | +0.56 | +0.47 / +0.63 | both halves | 2e-05 |  |
| [[SH3GL2]] | +0.56 | +0.47 / +0.67 | both halves | 2e-05 |  |
| [[TSPAN33]] | +0.56 | +0.42 / +0.55 | both halves | 4e-05 |  |
| [[PPP1R14C]] | +0.54 | +0.37 / +0.62 | both halves | 8e-05 |  |
| [[TMOD2]] | +0.54 | +0.37 / +0.58 | both halves | 8e-05 |  |
| [[RGS10]] | +0.54 | +0.29 / +0.46 | both halves | 2e-04 |  |
| [[SYN2]] | +0.53 | +0.37 / +0.65 | both halves | 7e-05 |  |
| [[RTN2]] | +0.53 | +0.31 / +0.43 | both halves | 2e-04 |  |
| [[TSPAN7]] | +0.53 | +0.41 / +0.60 | both halves | 4e-05 |  |
| [[LINC00937]] | +0.53 | +0.36 / +0.62 | both halves | 1e-04 |  |

## Genes that move opposite

*27 of its nearest partners move opposite, 9 of them with an alert (⚠; 9 not replicated); shown: the 12 strongest and the 2 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MAIP1]] | -0.53 | -0.28 / -0.42 | both halves | 3e-04 |  |
| [[GANC]] | -0.53 | -0.21 / -0.57 | both halves | 6e-04 |  |
| [[MTHFSD]] | -0.53 | -0.28 / -0.39 | both halves | 3e-04 |  |
| [[PSMC2]] | -0.51 | -0.35 / -0.39 | both halves | 1e-04 | pathway: Deubiquitination |
| [[PNISR-AS1]] | -0.51 | -0.19 / -0.45 | ⚠ not reproduced | 8e-04 |  |
| [[RBM48]] | -0.51 | -0.20 / -0.46 | ⚠ not reproduced | 8e-04 |  |
| [[MFF-DT]] | -0.51 | -0.25 / -0.40 | both halves | 4e-04 |  |
| [[WDR73]] | -0.51 | -0.24 / -0.40 | both halves | 4e-04 |  |
| [[VPS52]] | -0.50 | -0.31 / -0.41 | both halves | 2e-04 |  |
| [[PPWD1]] | -0.50 | -0.22 / -0.50 | both halves | 6e-04 |  |
| [[INTS2]] | -0.50 | -0.40 / -0.34 | both halves | 1e-04 |  |
| [[LINC01134]] | -0.49 | -0.25 / -0.34 | both halves | 4e-04 |  |
| [[TACO1]] | -0.49 | -0.28 / -0.40 | both halves | 3e-04 |  |
| [[DHRS4]] | -0.49 | -0.20 / -0.47 | both halves | 7e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*5 arrows, 5 of them with an alert ⚠; grade A 0, B 5, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[BSN]] | B | BSN activity raises OTUD7A's level | lines that do not express BSN (17) vs lines expressing it (33) | 2.63× lower at baseline in the lines without BSN | 0.007 | ⚠ within organs, on part of the lines; also absent: HRK, SPTB, CACNA2D2; maybe low, not absent |
| [[MED12L]] | B | MED12L activity raises OTUD7A's level | lines that do not express MED12L (18) vs lines expressing it (32) | 1.82× lower at baseline in the lines without MED12L | 0.013 | ⚠ within organs, on part of the lines; also absent: SYNGR1, NPTX1, AP3B2 |
| [[TSPAN33]] | B | TSPAN33 activity raises OTUD7A's level | lines that do not express TSPAN33 (12) vs lines expressing it (38) | 2.41× lower at baseline in the lines without TSPAN33 | 0.014 | ⚠ within organs, on part of the lines; also absent: SRCIN1, CRACD, GNAZ; maybe low, not absent |
| [[OBSL1]] | B | OBSL1 activity raises OTUD7A's level | lines that do not express OBSL1 (6) vs lines expressing it (44) | 2.36× lower at baseline in the lines without OBSL1 | 0.049 | ⚠ within organs, on part of the lines; also absent: PHC1, HECTD2, TPST1 |
| [[GNAZ]] | B | GNAZ activity raises OTUD7A's level | lines that do not express GNAZ (10) vs lines expressing it (40) | 2.22× lower at baseline in the lines without GNAZ | 0.079 | ⚠ within organs, on part of the lines; also absent: RNF220, TSPAN33, KIF26A; maybe low, not absent |

### Downstream of this gene

*7 arrows, 7 of them with an alert ⚠; grade A 0, B 7, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[KRBA2]] | B | OTUD7A activity raises KRBA2's level | lines that do not express OTUD7A (6) vs lines expressing it (44) | 1.96× lower at baseline in the lines without OTUD7A | 0.010 | ⚠ within organs, on part of the lines; also absent: ENSG00000256673, WWOX, RUNDC3A-AS1; maybe low, not absent |
| [[CARD8]] | B | OTUD7A activity raises CARD8's level | lines that do not express OTUD7A (6) vs lines expressing it (44) | 1.62× lower at baseline in the lines without OTUD7A | 0.013 | ⚠ within organs, on part of the lines; also absent: ENSG00000256673, WWOX, RUNDC3A-AS1; maybe low, not absent |
| [[SGSM1]] | B | OTUD7A activity raises SGSM1's level | lines that do not express OTUD7A (6) vs lines expressing it (44) | 1.75× lower at baseline in the lines without OTUD7A | 0.039 | ⚠ within organs, on part of the lines; also absent: ENSG00000256673, WWOX, RUNDC3A-AS1; maybe low, not absent |
| [[TSPAN33]] | B | OTUD7A activity raises TSPAN33's level | lines that do not express OTUD7A (6) vs lines expressing it (44) | 2.04× lower at baseline in the lines without OTUD7A | 0.060 | ⚠ within organs, on part of the lines; also absent: ENSG00000256673, WWOX, RUNDC3A-AS1; maybe low, not absent |
| [[SLC29A4]] | B | OTUD7A activity raises SLC29A4's level | lines that do not express OTUD7A (6) vs lines expressing it (44) | 2.55× lower at baseline in the lines without OTUD7A | 0.074 | ⚠ within organs, on part of the lines; also absent: ENSG00000256673, WWOX, RUNDC3A-AS1; maybe low, not absent |
| [[VPS52]] | B | OTUD7A activity raises VPS52's level | lines that do not express OTUD7A (6) vs lines expressing it (44) | 1.28× lower at baseline in the lines without OTUD7A | 0.099 | ⚠ within organs, on part of the lines; also absent: ENSG00000256673, WWOX, RUNDC3A-AS1; maybe low, not absent |
| [[PNISR-AS1]] | B | OTUD7A activity raises PNISR-AS1's level | lines that do not express OTUD7A (6) vs lines expressing it (44) | 1.41× lower at baseline in the lines without OTUD7A | 0.0998 | ⚠ within organs, on part of the lines; also absent: ENSG00000256673, WWOX, RUNDC3A-AS1; maybe low, not absent |

## Where it sits

- **Module**: [[Module 115]]; 42 genes; every member is in the + arm (projection on the module's main direction 0.613). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (0.8, 34.6); signed map (-10.4, 46.2). **Vector** length 76.7, 15.1% of its response variance represented; |z| ≥ 3 in 1,110 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +10.0 | +35.1 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +8.5 | +19.0 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | +5.5 | +26.6 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | +3.8 | +42.0 |
|  | [[Panobinostat (drug)]] 5 µM |  | +3.7 | +43.4 |
|  | [[Brivudine (drug)]] 5 µM |  | +3.5 | +16.9 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | +2.6 | +1.9 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.2 | +4.1 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | +1.5 | +2.1 |
| fall | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -2.9 | -3.1 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~0% of this change | -2.8 | -3.1 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.5 | -1.0 |
|  | [[TAK-901 (drug)]] 5 µM |  | -2.1 | -4.7 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | -1.8 | +8.0 |
|  | [[Sulfatinib (drug)]] 5 µM |  | -1.8 | -3.3 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -1.6 | -2.6 |
|  | [[PH-797804 (drug)]] 5 µM |  | -1.1 | -1.9 |
|  | [[ERK5-IN-2 (drug)]] 5 µM |  | -1.1 | +0.3 |
|  | [[Osimertinib (mesylate) (drug)]] 5 µM |  | -1.0 | -1.9 |

## What is on record

|  |  |
|---|---|
| Name | OTU deubiquitinase 7A |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 15q13.3 — chr15:31,475,398-31,870,789 (-) |
| Ensembl biotype | protein_coding |
| Also known as | CEZANNE2; previously C15orf16, OTUD7 |
| Gene groups (HGNC) | OTU domain containing; Zinc fingers A20-type |
| Reactome | 2 pathways, smallest: Ovarian tumor domain proteases; Deubiquitination |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8TE49](https://www.uniprot.org/uniprotkb/Q8TE49) (OTU domain-containing protein 7A):

> Deubiquitinase, which cleaves 'Lys-11'-linked polyubiquitin chains. Might be required for PA28-20S proteasome assembly (Probable).

**Summary**, from NCBI Gene [161725](https://www.ncbi.nlm.nih.gov/gene/161725):

> The protein encoded by this gene is a deubiquitinizing enzyme and possible tumor suppressor. The encoded protein acts on TNF receptor associated factor 6 (TRAF6) to control nuclear factor kappa B expression. However, this gene is downregulated by SNAIL1 in hepatocellular carcinoma cells, contributing to their progression and malignancy. [provided by RefSeq, Aug 2016]

**Accessions** — [HGNC:20718](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:20718) · Entrez [161725](https://www.ncbi.nlm.nih.gov/gene/161725) · UniProt [Q8TE49](https://www.uniprot.org/uniprotkb/Q8TE49) · Ensembl [ENSG00000169918](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000169918)

## Data

Gene col 9874: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9874); `tables/drug_effects.parquet` (35 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9874, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9874]; `tensor/DDL_lfc|DDL_z.npy` [9874]; `embed/gene_vectors.npy` [9874]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9874 or target_col == 9874). Every well: [[OTUD7A — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/OTUD7A.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
