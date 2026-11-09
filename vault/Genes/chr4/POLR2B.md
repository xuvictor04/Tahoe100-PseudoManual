---
symbol: "POLR2B"
type: "gene"
col: 512
ensembl_id: "ENSG00000047315"
name: "RNA polymerase II subunit B"
location: "4q12"
module: 20
arm: "+"
pooled_cpm: 117.57
n_lines_expressing: 50
n_dd_up: 29
n_dd_down: 3
n_dd_up_clean: 18
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/020"]
generated_by: "tahoemap"
---

# POLR2B

*RNA polymerase II subunit B* — 4q12

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 29 drug-doses (11 with an alert ⚠); the strongest is [[TAK-901 (drug)]] 5 µM: 3.59× (z +15.9, q 0e+00, up in 47 of 49 measured lines).
> Pooled over the cell lines (median), lowered significantly by 3 drug-doses (1 with an alert ⚠); the strongest is [[Harringtonine (drug)]] 0.5 µM: 0.704× (z -8.4, q 3e-14, down in 34 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 6 here, 3 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.05 µM in 2 lines (RKO 0.340×, A-427 0.402×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change); [[Homoharringtonine (drug)]] 0.5 µM in 1 line (A-427 0.355×; ⚠ cell-cycle shift, explains ~0% of this change); [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM in 1 line (SW 1271 0.0802×); [[Atazanavir (sulfate) (drug)]] 5 µM in 1 line (NCI-H596 0.162×); [[Harringtonine (drug)]] 0.5 µM in 1 line (KATO III 0.570×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TM9SF2]] (+0.68, fdr 1e-05), [[SUMO1]] (+0.68, fdr 7e-06), [[STRAP]] (+0.64, fdr 7e-06); moves opposite to [[SERTAD1]] (-0.62, fdr 7e-06), [[TRIM47]] (-0.61, fdr 3e-05), [[C11orf68]] (-0.61, fdr 4e-05).
> It sits in the **+** arm of [[Module 020]] (Cap-dependent Translation Initiation).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 37 in all, 17 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 29 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 11 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 512.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[TAK-901 (drug)]] 5 µM |  | **3.59×** | +15.9 | 0e+00 | 47/49 (SW480, LoVo, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~2% here); composition shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **2.60×** | +11.9 | 3e-30 | 47/48 (SW480, LS 180, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Panobinostat (drug)]] 5 µM |  | **1.64×** | +11.8 | 6e-30 | 47/48 (SW480, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here) |
| [[Belinostat (drug)]] 5 µM |  | **1.61×** | +11.3 | 2e-27 | 46/48 (NCI-H1792, LoVo, …) | rises with dose | cell-cycle shift (explains ~16% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.58×** | +11.0 | 6e-26 | 40/48 (LoVo, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.58×** | +10.4 | 2e-23 | 37/44 (LoVo, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.55×** | +10.4 | 3e-23 | 34/49 (LoVo, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~24% here); composition shift |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.49×** | +9.4 | 3e-19 | 40/48 (NCI-H23, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.48×** | +9.3 | 6e-19 | 43/48 (SW480, PANC-1, …) | rises with dose | cell-cycle shift (explains ~5% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.46×** | +9.1 | 8e-18 | 37/48 (LoVo, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here); composition shift |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.41×** | +7.9 | 1e-13 | 34/47 (LoVo, NCI-H1573, …) | top dose only | cell-cycle shift (explains ~12% here) |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **1.83×** | +7.5 | 3e-12 | 29/38 (LOX-IMVI, NCI-H1573, …) | top dose only | noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.23×** | +7.0 | 1e-10 | 25/48 (NCI-H1792, NCI-H1573, …) | top dose only | cell-cycle shift (explains ~1% here); composition shift |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.34×** | +7.0 | 1e-10 | 35/48 (A-172, SW480, …) | rises with dose |  |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.32×** | +6.6 | 2e-09 | 32/48 (LoVo, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.28×** | +5.9 | 2e-07 | 28/48 (SW480, RKO, …) | top dose only |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.27×** | +5.4 | 2e-06 | 30/48 (PANC-1, A-172, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[TAK-901 (drug)]] 0.05 µM |  | **1.24×** | +4.9 | 3e-05 | 23/47 (LOX-IMVI, HEC-1-A, …) | inconsistent across doses |  |
| [[GSK1059615 (drug)]] 5 µM |  | **1.40×** | +4.2 | 6e-04 | 30/49 (MIA PaCa-2, LoVo, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[NG25 (drug)]] 5 µM |  | **1.39×** | +4.1 | 0.001 | 28/47 (RKO, LoVo, …) | top dose only | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, 1 with an alert ⚠. 3 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 512.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 6 here, 3 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.05 µM in 2 lines (RKO 0.340×, A-427 0.402×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change); [[Homoharringtonine (drug)]] 0.5 µM in 1 line (A-427 0.355×; ⚠ cell-cycle shift, explains ~0% of this change); [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM in 1 line (SW 1271 0.0802×); [[Atazanavir (sulfate) (drug)]] 5 µM in 1 line (NCI-H596 0.162×); [[Harringtonine (drug)]] 0.5 µM in 1 line (KATO III 0.570×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Harringtonine (drug)]] 0.5 µM |  | **0.704×** | -8.4 | 3e-14 | 34/48 (KATO III, AsPC-1, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 0.05 µM |  | **0.825×** | -4.2 | 0.006 | 25/47 (HepG2/C3A, H4, …) | all doses, flat | low cells (technical?) |
| [[Ribociclib (drug)]] 0.05 µM | ⚠ unreliable plate only; position not correctable | **0.806×** | -4.2 | 0.006 | 24/49 (BT-474, SW480, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Estrone sulfate (potassium) (drug)]] 5 µM |  | 0.861× | -3.6 | 0.054 | 14/48 (SW 1088, RPMI-7951, …) | top dose only |  |
| [[Folic acid (drug)]] 5 µM |  | 0.911× | -3.2 | 0.18 | 4/48 (HS-578T, CFPAC-1, …) | top dose only |  |
| [[Filgotinib (drug)]] 0.05 µM |  | 0.879× | -3.1 | 0.20 | 7/48 (LOX-IMVI, LS 180, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.15 per unit of S-phase module lfc, -0.01 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 512. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LoVo (line)]] | wt | 123 | 12 (6 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.85× (z +22.6) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 2.72× (z +16.7) | — |
| [[SW480 (line)]] | alt | 136 | 11 (4 ⚠) | 0 | [[TAK-901 (drug)]] 5 µM 4.75× (z +16.7) | — |
| [[NCI-H23 (line)]] | alt | 230 | 10 (3 ⚠) | 0 | [[TAK-901 (drug)]] 5 µM 4.33× (z +12.5) | — |
| [[NCI-H460 (line)]] | wt | 90.4 | 8 (4 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.75× (z +14.4) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 5 µM 2.02× (z +10.3) | — |
| [[NCI-H1573 (line)]] | alt | 101 | 6 (2 ⚠) | 0 | [[TAK-901 (drug)]] 5 µM 5.70× (z +12.4) | — |
| [[NCI-H1792 (line)]] | alt | 96.5 | 6 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.90× (z +12.6) | — |
| [[KATO III (line)]] | alt | 116 | 4 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 3.37× (z +17.6) ⚠ toxic; transcription drop · without an alert: [[TAK-901 (drug)]] 5 µM 4.76× (z +12.3) | [[Harringtonine (drug)]] 0.5 µM 0.570× (z -8.5) |
| [[CFPAC-1 (line)]] | alt | 102 | 4 (1 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 2.00× (z +9.8) | — |
| [[HOP62 (line)]] | alt | 91.5 | 4 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 5.04× (z +20.8) ⚠ toxic; transcription drop · without an alert: [[TAK-901 (drug)]] 5 µM 3.99× (z +9.7) | — |
| [[LS 180 (line)]] | wt | 146 | 4 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.81× (z +14.6) | — |
| [[PANC-1 (line)]] | alt | 89.1 | 4 (1 ⚠) | 0 | [[TAK-901 (drug)]] 5 µM 5.51× (z +13.6) | — |
| [[RKO (line)]] | wt | 168 | 3 | 1 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 4.62× (z +11.8) | [[Dinaciclib (drug)]] 0.05 µM 0.340× (z -14.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change |
| [[A-172 (line)]] | wt | 75.8 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 2.26× (z +11.0) | — |
| [[A-427 (line)]] | wt | 149 | 1 | 2 (2 ⚠) | [[TAK-901 (drug)]] 5 µM 3.20× (z +8.6) | [[Homoharringtonine (drug)]] 0.5 µM 0.355× (z -14.7) ⚠ cell-cycle shift, explains ~0% of this change |
| [[H4 (line)]] | wt | 125 | 2 (2 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 5 µM 3.43× (z +11.9) ⚠ toxic; transcription drop | [[Bortezomib (drug)]] 5 µM 0.145× (z -10.2) ⚠ toxic |
| [[HEC-1-A (line)]] | alt | 111 | 3 | 0 | [[TAK-901 (drug)]] 5 µM 4.10× (z +10.3) | — |
| [[Hs 766T (line)]] | wt | 98.4 | 3 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.12× (z +12.2) ⚠ toxic; transcription drop · without an alert: [[TAK-901 (drug)]] 5 µM 5.98× (z +10.4) | — |
| [[HS-578T (line)]] | alt | 85.1 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.77× (z +9.1) | — |
| [[J82 (line)]] | alt | 91.3 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.37× (z +15.8) ⚠ toxic; transcription drop | — |
| [[LOX-IMVI (line)]] | wt | 79.1 | 3 | 0 | [[TAK-901 (drug)]] 0.05 µM 2.91× (z +12.2) | — |
| [[MIA PaCa-2 (line)]] | alt | 95.0 | 3 (1 ⚠) | 0 | [[TAK-901 (drug)]] 5 µM 5.46× (z +9.9) | — |
| [[SNU-423 (line)]] | alt | 90.4 | 3 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.41× (z +9.8) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 5 µM 2.16× (z +8.9) | — |
| [[RPMI-7951 (line)]] | alt | 100 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.50× (z +13.2) ⚠ toxic; transcription drop | — |
| [[SW1417 (line)]] | alt | 103 | 2 | 0 | [[TAK-901 (drug)]] 5 µM 4.01× (z +9.6) | — |
| [[C-33 A (line)]] | alt | 156 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 3.83× (z +8.7) | — |
| [[COLO 205 (line)]] | alt | 99.6 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 6.01× (z +10.0) | — |
| [[HT-29 (line)]] | alt | 111 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 3.31× (z +8.8) | — |
| [[NCI-H2030 (line)]] | alt | 113 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.42× (z +9.6) ⚠ toxic; transcription drop | — |
| [[NCI-H596 (line)]] | alt | 125 | 0 | 1 | — | [[Atazanavir (sulfate) (drug)]] 5 µM 0.162× (z -9.7) |
| [[Panc 03.27 (line)]] | alt | 102 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 5.09× (z +9.7) | — |
| [[SHP-77 (line)]] | alt | 202 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 3.69× (z +9.5) | — |
| [[SK-MEL-2 (line)]] | alt | 126 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 4.40× (z +9.8) | — |
| [[SNU-1 (line)]] | wt | 118 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 6.85× (z +9.4) | — |
| [[SW 1271 (line)]] | alt | 97.9 | 0 | 1 | — | [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM 0.0802× (z -11.0) |
| [[SW 900 (line)]] | alt | 172 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.34× (z +10.6) ⚠ toxic; transcription drop | — |
| [[A498 (line)]] | wt | 157 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 86.8 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 172 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 98.5 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 109 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 104 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 127 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 120 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 98.8 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 102 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 109 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 170 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 361 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 129 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 185 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 512), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*68 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TM9SF2]] | +0.68 | +0.53 / +0.68 | both halves | 1e-05 |  |
| [[SUMO1]] | +0.68 | +0.61 / +0.69 | both halves | 7e-06 | pathway: Nucleotide Excision Repair |
| [[STRAP]] | +0.64 | +0.59 / +0.65 | both halves | 7e-06 |  |
| [[OPA1]] | +0.63 | +0.54 / +0.63 | both halves | 1e-05 |  |
| [[NUDT21]] | +0.62 | +0.54 / +0.58 | both halves | 1e-05 | pathway: Dengue Virus-Host Interactions |
| [[DDOST]] | +0.61 | +0.53 / +0.62 | both halves | 1e-05 |  |
| [[PPHLN1]] | +0.60 | +0.65 / +0.59 | both halves | 7e-06 |  |
| [[TMEM248]] | +0.60 | +0.50 / +0.58 | both halves | 1e-05 |  |
| [[COPS7B]] | +0.59 | +0.60 / +0.59 | both halves | 7e-06 | pathway: Formation of TC-NER Pre-Incision Complex; STRING 504 |
| [[RPS3A]] | +0.59 | +0.52 / +0.64 | both halves | 1e-05 | pathway: Influenza Infection |
| [[SDHAP4]] | +0.59 | +0.53 / +0.58 | both halves | 1e-05 |  |
| [[RPA1]] | +0.59 | +0.48 / +0.61 | both halves | 2e-05 | pathway: Chromosome Maintenance; STRING 410 |

## Genes that move opposite

*32 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SERTAD1]] | -0.62 | -0.62 / -0.61 | both halves | 7e-06 |  |
| [[TRIM47]] | -0.61 | -0.43 / -0.68 | both halves | 3e-05 |  |
| [[C11orf68]] | -0.61 | -0.42 / -0.67 | both halves | 4e-05 |  |
| [[TP53RK]] | -0.60 | -0.33 / -0.67 | both halves | 1e-04 |  |
| [[CMTR2]] | -0.59 | -0.48 / -0.58 | both halves | 2e-05 |  |
| [[RPP25L]] | -0.58 | -0.41 / -0.63 | both halves | 4e-05 |  |
| [[TNFRSF12A]] | -0.58 | -0.63 / -0.55 | both halves | 1e-05 |  |
| [[C14orf119]] | -0.57 | -0.41 / -0.62 | both halves | 4e-05 |  |
| [[KCTD11]] | -0.57 | -0.54 / -0.60 | both halves | 1e-05 |  |
| [[CDKN2AIP]] | -0.56 | -0.42 / -0.56 | both halves | 4e-05 |  |
| [[DYNLL1]] | -0.56 | -0.49 / -0.58 | both halves | 1e-05 | pathway: Affinity selection of immunoglobulins |
| [[BTG1]] | -0.56 | -0.56 / -0.61 | both halves | 1e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 020]] — Cap-dependent Translation Initiation; 191 genes; this gene is in the **+** arm (projection on the module's main direction 0.546). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.29).
- **Nodal map** (x, y) = (-10.6, -14.7); signed map (-25.4, -33.0). **Vector** length 100, 30.1% of its response variance represented; |z| ≥ 3 in 1,246 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +9.1 | +10.4 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +8.8 | +10.4 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | +7.2 | +5.3 |
|  | [[PH-797804 (drug)]] 5 µM |  | +5.9 | +11.9 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | +5.2 | +5.3 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +3.4 | +2.9 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | +3.1 | +4.9 |
|  | [[GSK1059615 (drug)]] 5 µM |  | +2.6 | +4.2 |
|  | [[Cabozantinib (S-malate) (drug)]] 5 µM |  | +2.2 | +0.7 |
| fall | [[Harringtonine (drug)]] 0.5 µM |  | -12.1 | -8.4 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | -11.2 | -2.8 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -6.5 | -2.3 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -5.2 | +1.4 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -4.1 | -4.2 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -2.7 | +0.1 |
|  | [[PF-06260933 (drug)]] 5 µM |  | -2.3 | -2.5 |
|  | [[Peretinoin (drug)]] 5 µM |  | -1.6 | +0.1 |

## What is on record

|  |  |
|---|---|
| Name | RNA polymerase II subunit B |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 4q12 — chr4:56,977,722-57,031,158 (+) |
| Ensembl biotype | protein_coding |
| Also known as | RPB2 |
| Gene groups (HGNC) | RNA polymerase subunits |
| Reactome | 75 pathways, smallest: Signaling by FGFR2 IIIa TM; PIWI-interacting RNA (piRNA) biogenesis; Abortive elongation of HIV-1 transcript in the absence of Tat |
| Matched by | ensembl_id |

**Function**, from UniProt [P30876](https://www.uniprot.org/uniprotkb/P30876) (DNA-directed RNA polymerase II subunit RPB2):

> Catalytic core component of RNA polymerase II (Pol II), a DNA-dependent RNA polymerase which synthesizes mRNA precursors and many functional non-coding RNAs using the four ribonucleoside triphosphates as substrates (By similarity). Pol II-mediated transcription cycle proceeds through transcription initiation, transcription elongation and transcription termination stages. During transcription initiation, Pol II pre-initiation complex (PIC) is recruited to DNA promoters, with focused-type …

**Summary**, from NCBI Gene [5431](https://www.ncbi.nlm.nih.gov/gene/5431):

> This gene encodes the second largest subunit of RNA polymerase II (Pol II), a DNA-dependent RNA polymerase that catalyzes the transcription of DNA into precursors of mRNA, snRNA and microRNA. This subunit and the largest subunit form opposite sides of the center cleft of Pol II. Deletion of the flap loop region of this subunit results in a decrease in the rate of transcriptional elongation. Alternative splicing results in multiple transcript variants. [provided by RefSeq, Dec 2014]

**Accessions** — [HGNC:9188](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:9188) · Entrez [5431](https://www.ncbi.nlm.nih.gov/gene/5431) · UniProt [P30876](https://www.uniprot.org/uniprotkb/P30876) · Ensembl [ENSG00000047315](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000047315)

## Data

Gene col 512: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 512); `tables/drug_effects.parquet` (43 rows, flagged included); `relations/gene_relations.parquet` (col_a == 512, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 512]; `tensor/DDL_lfc|DDL_z.npy` [512]; `embed/gene_vectors.npy` [512]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 512 or target_col == 512). Every well: [[POLR2B — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/POLR2B.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
