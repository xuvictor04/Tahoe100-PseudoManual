---
symbol: "CXCL1"
type: "gene"
col: 8769
ensembl_id: "ENSG00000163739"
name: "C-X-C motif chemokine ligand 1"
location: "4q13.3"
module: 14
arm: "+"
pooled_cpm: 37.62
n_lines_expressing: 33
n_dd_up: 32
n_dd_down: 6
n_dd_up_clean: 19
n_dd_down_clean: 5
in_vector_space: true
direction_upstream: 9
direction_downstream: 7
tags: ["gene", "module/014"]
generated_by: "tahoemap"
---

# CXCL1

*C-X-C motif chemokine ligand 1* — 4q13.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 32 drug-doses (13 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 20.0× (z +31.0, q 0e+00, up in 31 of 31 measured lines).
> Pooled over the cell lines (median), lowered significantly by 6 drug-doses (1 with an alert ⚠); the strongest is [[Ponatinib (drug)]] 5 µM: 0.360× (z -7.5, q 5e-11, down in 24 of 31 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CXCL2]] (+0.80, fdr 7e-06), [[CXCL3]] (+0.77, fdr 7e-06), [[CXCL5]] (+0.68, fdr 7e-06); moves opposite to [[INPP5B]] (-0.52, fdr 3e-05), [[SAP130]] (-0.51, fdr 4e-05), [[MACO1]] (-0.51, fdr 2e-04).
> It is in [[Module 014]], a single-armed module (TNF-alpha signaling via NF-kB).
> Probable direction (from the cell lines, not proof of direct regulation): 9 arrows point to it, the strongest [[CXCL3]] → it (grade B ⚠); 7 go from it, the strongest it → [[CXCL3]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 32 in all, 13 with an alert ⚠; shown: the 15 strongest and the 7 next strongest without an alert. 32 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 13 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8769.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **20.0×** | +31.0 | 0e+00 | 31/31 (PANC-1, Panc 03.27, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **24.2×** | +22.4 | 0e+00 | 31/31 (PANC-1, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **8.41×** | +15.6 | 0e+00 | 27/31 (A498, hTERT-HPNE, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **5.61×** | +12.6 | 3e-34 | 29/31 (NCI-H460, SW 900, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change | **5.16×** | +12.0 | 4e-31 | 29/30 (NCI-H460, SW 900, …) | all doses, stronger at high dose |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change | **5.14×** | +12.0 | 5e-31 | 27/29 (NCI-H460, HOP62, …) | all doses, flat | composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **2.93×** | +11.1 | 1e-26 | 29/31 (A498, HT-29, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **4.90×** | +10.7 | 5e-25 | 28/29 (A549, HOP62, …) | all doses, flat | cell-cycle shift (explains ~23% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **4.29×** | +10.6 | 1e-24 | 26/31 (NCI-H460, SW 900, …) | all doses, stronger at high dose | composition shift; position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change | **4.34×** | +10.3 | 3e-23 | 24/28 (NCI-H460, HOP62, …) | all doses, flat | composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **8.05×** | +8.0 | 8e-14 | 30/31 (LoVo, BT-474, …) | rises with dose | plate-row cell shift; cell-cycle shift (explains ~17% here); composition shift; noisy plate (z scaled) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~28% of this change | **3.07×** | +7.9 | 1e-13 | 26/30 (NCI-H460, MIA PaCa-2, …) | top dose only | position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.12×** | +7.8 | 3e-13 | 17/31 (CFPAC-1, HOP62, …) | rises with dose | cell-cycle shift (explains ~8% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **3.08×** | +7.4 | 4e-12 | 22/30 (NCI-H460, SW 900, …) | all doses, stronger at high dose | position effect removed |
| [[Tucidinostat (drug)]] 0.5 µM |  | **2.69×** | +7.2 | 2e-11 | 25/31 (A498, HT-29, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 5 µM |  | **1.79×** | +6.0 | 5e-08 | 20/31 (Panc 03.27, SNU-423, …) | all doses, stronger at high dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 0.5 µM |  | **2.13×** | +5.5 | 1e-06 | 23/31 (Panc 03.27, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Belumosudil (drug)]] 5 µM |  | **2.17×** | +5.4 | 2e-06 | 24/31 (MIA PaCa-2, LoVo, …) | rises with dose |  |
| [[PH-797804 (drug)]] 5 µM |  | **3.32×** | +4.6 | 1e-04 | 19/30 (BT-474, Panc 03.27, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.80×** | +4.3 | 4e-04 | 21/31 (A498, SW 900, …) | all doses, stronger at high dose |  |
| [[Amsacrine (drug)]] 5 µM |  | **1.44×** | +3.8 | 0.004 | 15/31 (NCI-H2347, NCI-H1792, …) | top dose only | position effect removed |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.38×** | +3.3 | 0.020 | 18/31 (NCI-H1792, HOP62, …) | rises with dose | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 1 with an alert ⚠. 6 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 8769.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ponatinib (drug)]] 5 µM |  | **0.360×** | -7.5 | 5e-11 | 24/31 (NCI-H460, LOX-IMVI, …) | all doses, stronger at high dose |  |
| [[Auranofin (drug)]] 5 µM |  | **0.491×** | -5.2 | 6e-05 | 21/31 (LoVo, A498, …) | top dose only |  |
| [[NG25 (drug)]] 5 µM |  | **0.354×** | -4.0 | 0.014 | 17/30 (NCI-H460, NCI-H2030, …) | top dose only | cell-cycle shift (explains ~0% here); noisy plate (z scaled); position effect removed |
| [[Ipatasertib (drug)]] 5 µM |  | **0.368×** | -3.8 | 0.019 | 19/31 (SW 900, A549, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Ralimetinib dimesylate (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.595×** | -3.7 | 0.021 | 15/31 (A498, NCI-H1573, …) | inconsistent across doses |  |
| [[Clobetasol propionate (drug)]] 5 µM |  | **0.638×** | -3.3 | 0.097 | 11/31 (NCI-H460, A498, …) | rises with dose |  |
| [[Afatinib (drug)]] 5 µM |  | 0.588× | -3.1 | 0.12 | 16/31 (NCI-H2030, LS 180, …) | rises with dose | noisy plate (z scaled) |
| [[Dexamethasone (drug)]] 0.5 µM |  | 0.624× | -3.1 | 0.12 | 11/31 (A498, SK-MEL-2, …) | inconsistent across doses |  |
| [[Budesonide (drug)]] 5 µM |  | 0.653× | -3.1 | 0.12 | 15/31 (NCI-H460, A498, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.35 per unit of S-phase module lfc, +0.71 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8769. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 204 | 14 (9 ⚠) | 6 (1 ⚠) | [[Digitoxin (drug)]] 5 µM 13.7× (z +16.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 13.4× (z +16.1) | [[Trametinib (drug)]] 5 µM 0.146× (z -12.1) ⚠ cell-cycle shift, explains ~45% of this change · without an alert: [[NG25 (drug)]] 5 µM 0.0579× (z -9.3) |
| [[HOP62 (line)]] | alt | 37.0 | 10 (5 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 88.8× (z +24.7) | — |
| [[NCI-H1792 (line)]] | alt | 31.1 | 9 (4 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 32.7× (z +20.0) | — |
| [[SW 900 (line)]] | alt | 81.5 | 9 (5 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 36.5× (z +15.6) ⚠ cell-cycle shift, explains ~32% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 11.9× (z +15.2) | — |
| [[A498 (line)]] | wt | 53.3 | 8 | 0 | [[Homoharringtonine (drug)]] 0.5 µM 55.0× (z +18.1) | — |
| [[MIA PaCa-2 (line)]] | alt | 98.3 | 7 (3 ⚠) | 1 (1 ⚠) | [[Harringtonine (drug)]] 5 µM 23.4× (z +17.2) | [[Adagrasib (drug)]] 0.05 µM 0.458× (z -15.7) ⚠ position not correctable |
| [[hTERT-HPNE (line)]] | wt | 27.6 | 7 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 311× (z +24.0) | — |
| [[Panc 03.27 (line)]] | alt | 21.2 | 7 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 78.8× (z +25.9) | — |
| [[SNU-423 (line)]] | alt | 16.7 | 7 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 86.0× (z +22.1) | — |
| [[A549 (line)]] | wt | 35.1 | 6 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 15.6× (z +19.0) | — |
| [[LoVo (line)]] | wt | 36.5 | 4 (1 ⚠) | 2 (1 ⚠) | [[Harringtonine (drug)]] 5 µM 14.1× (z +13.8) | [[Belinostat (drug)]] 5 µM 0.149× (z -10.2) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.158× (z -9.9) |
| [[PANC-1 (line)]] | alt | 19.0 | 6 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 65.4× (z +30.0) | — |
| [[J82 (line)]] | alt | 33.3 | 5 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 65.6× (z +25.8) | — |
| [[LOX-IMVI (line)]] | wt | 52.0 | 5 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 8.37× (z +17.1) | — |
| [[NCI-H2347 (line)]] | alt | 13.2 | 5 | 0 | [[Homoharringtonine (drug)]] 5 µM 74.1× (z +22.5) | — |
| [[RPMI-7951 (line)]] | alt | 55.2 | 5 (1 ⚠) | 0 | [[Harringtonine (drug)]] 5 µM 114× (z +16.3) | — |
| [[BT-474 (line)]] | alt | 29.6 | 4 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 106× (z +22.5) | — |
| [[C32 (line)]] | wt | 11.4 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 480× (z +19.5) | — |
| [[CFPAC-1 (line)]] | alt | 82.5 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 43.0× (z +23.8) | — |
| [[HEC-1-A (line)]] | alt | 18.8 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 48.8× (z +20.8) | — |
| [[NCI-H2030 (line)]] | alt | 97.9 | 3 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 7.13× (z +14.3) | [[Adagrasib (drug)]] 0.05 µM 0.609× (z -8.9) ⚠ position not correctable |
| [[SK-MEL-2 (line)]] | alt | 30.6 | 4 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 25.1× (z +16.5) | — |
| [[SW1417 (line)]] | alt | 22.1 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 17.0× (z +16.9) | — |
| [[HT-29 (line)]] | alt | 22.3 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 21.3× (z +16.8) | — |
| [[LS 180 (line)]] | wt | 28.5 | 2 | 1 | [[Harringtonine (drug)]] 5 µM 20.9× (z +14.9) | [[Panobinostat (drug)]] 5 µM 0.186× (z -8.6) |
| [[NCI-H1573 (line)]] | alt | 49.8 | 2 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.97× (z +10.4) | [[Belinostat (drug)]] 5 µM 0.143× (z -9.0) ⚠ cell-cycle shift, explains ~0% of this change |
| [[AsPC-1 (line)]] | alt | 11.0 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 48.8× (z +21.3) | — |
| [[Hs 766T (line)]] | wt | 11.9 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 7.12× (z +9.7) | — |
| [[NCI-H23 (line)]] | alt | 23.0 | 0 | 2 (2 ⚠) | — | [[Adagrasib (drug)]] 0.05 µM 0.340× (z -14.6) ⚠ position not correctable |
| [[SW 1271 (line)]] | alt | 14.1 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 41.3× (z +9.4) | — |
| [[A-172 (line)]] | wt | 3.30 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 4.31 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 6.70 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 3.82 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 5.08 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 9.01 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 3.58 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 4.12 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 3.49 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 3.53 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 23.6 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 26.3 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 41.4 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 5.89 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 3.83 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 2.99 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 3.66 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 6.86 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 7.41 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 7.04 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8769), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*83 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CXCL2]] | +0.80 | +0.77 / +0.80 | both halves | 7e-06 | same gene group; pathway: HALLMARK_TNFA_SIGNALING_VIA_NFKB; STRING 996 |
| [[CXCL3]] | +0.77 | +0.75 / +0.77 | both halves | 7e-06 | same gene group; pathway: HALLMARK_IL6_JAK_STAT3_SIGNALING; STRING 996 |
| [[CXCL5]] | +0.68 | +0.62 / +0.66 | both halves | 7e-06 | same gene group; pathway: Chemokine receptors bind chemokines; STRING 999 |
| [[CXCL8]] | +0.67 | +0.62 / +0.73 | both halves | 7e-06 | same gene group; pathway: HALLMARK_EPITHELIAL_MESENCHYMAL_TRANSITION; STRING 957 |
| [[LINC02605]] | +0.66 | +0.61 / +0.68 | both halves | 7e-06 |  |
| [[CLDN1]] | +0.64 | +0.55 / +0.62 | both halves | 1e-05 |  |
| [[TRAF1]] | +0.63 | +0.60 / +0.58 | both halves | 7e-06 | pathway: HALLMARK_TNFA_SIGNALING_VIA_NFKB |
| [[HCP5]] | +0.60 | +0.48 / +0.57 | both halves | 2e-05 |  |
| [[SOCS2]] | +0.59 | +0.53 / +0.54 | both halves | 1e-05 |  |
| [[QPCT]] | +0.59 | +0.37 / +0.59 | both halves | 8e-05 |  |
| [[NFKB1]] | +0.58 | +0.54 / +0.48 | both halves | 2e-05 | pathway: HALLMARK_TNFA_SIGNALING_VIA_NFKB; STRING 963 |
| [[HIVEP2]] | +0.58 | +0.49 / +0.48 | both halves | 2e-05 |  |

## Genes that move opposite

*17 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[INPP5B]] | -0.52 | -0.44 / -0.44 | both halves | 3e-05 |  |
| [[SAP130]] | -0.51 | -0.41 / -0.47 | both halves | 4e-05 |  |
| [[MACO1]] | -0.51 | -0.60 / -0.31 | both halves | 2e-04 |  |
| [[SLC35E1]] | -0.49 | -0.42 / -0.48 | both halves | 4e-05 |  |
| [[ZFYVE21]] | -0.49 | -0.50 / -0.42 | both halves | 4e-05 |  |
| [[MAP3K9]] | -0.49 | -0.45 / -0.40 | both halves | 5e-05 |  |
| [[GPR155]] | -0.49 | -0.41 / -0.40 | both halves | 5e-05 |  |
| [[ZCCHC17]] | -0.49 | -0.41 / -0.43 | both halves | 4e-05 |  |
| [[SDHAP1]] | -0.49 | -0.45 / -0.43 | both halves | 3e-05 |  |
| [[RAB2A]] | -0.49 | -0.47 / -0.47 | both halves | 2e-05 |  |
| [[DHDDS]] | -0.48 | -0.44 / -0.44 | both halves | 3e-05 |  |
| [[TNPO3]] | -0.48 | -0.50 / -0.43 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*9 arrows, 9 of them with an alert ⚠; grade A 0, B 7, C 2.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CXCL3]] | B | CXCL3 activity raises CXCL1's level | lines that do not express CXCL3 (14) vs lines expressing it (36) | 3.23× lower at baseline in the lines without CXCL3 | 3e-04 | ⚠ within organs, on part of the lines; also absent: MGLL, SPTLC3, PCED1B |
| [[CXCL8]] | B | CXCL8 activity raises CXCL1's level | lines that do not express CXCL8 (20) vs lines expressing it (30) | 3.15× lower at baseline in the lines without CXCL8 | 0.002 | ⚠ within organs, on part of the lines; also absent: TMEM92-AS1, IL1R1, C15orf48 |
| [[CXCL2]] | B | CXCL2 activity raises CXCL1's level | lines that do not express CXCL2 (14) vs lines expressing it (36) | 2.82× lower at baseline in the lines without CXCL2 | 0.010 | ⚠ within organs, on part of the lines; also absent: TENT5A, GPR39, CXCL3 |
| [[CXCL5]] | B | CXCL5 activity raises CXCL1's level | lines that do not express CXCL5 (35) vs lines expressing it (15) | 2.98× lower at baseline in the lines without CXCL5 | 0.038 | ⚠ within organs, on part of the lines; also absent: ANXA10, IRAK3, TRBC2 |
| [[ZC3H12A]] | B | ZC3H12A activity raises CXCL1's level | lines that do not express ZC3H12A (5) vs lines expressing it (45) | 4.16× lower at baseline in the lines without ZC3H12A | 0.060 | ⚠ within organs, on part of the lines; co-absent genes; also absent: SMOX, SLC2A1, ENSG00000281883; maybe low, not absent; its own permutation p |
| [[TFPI2]] | B | TFPI2 activity raises CXCL1's level | lines that do not express TFPI2 (22) vs lines expressing it (28) | 2.12× lower at baseline in the lines without TFPI2 | 0.063 | ⚠ within organs, on part of the lines; also absent: DNAH11, GJA1, TRIM6 |
| [[IER3]] | B | IER3 activity raises CXCL1's level | lines that do not express IER3 (5) vs lines expressing it (45) | 3.98× lower at baseline in the lines without IER3 | 0.076 | ⚠ within organs, on part of the lines; also absent: ARHGAP18, SLC2A1, SHB |
| [[CCL20]] | C | CCL20 activity raises CXCL1's level | lines that do not express CCL20 (16) vs lines expressing it (34) | 3.18× lower at baseline in the lines without CCL20 | 0.015 | ⚠ within organs, on part of the lines; also absent: TGM2, CLDN16, GPR39; co-absent with the target |
| [[TM4SF1-AS1]] | C | TM4SF1-AS1 activity raises CXCL1's level | lines that do not express TM4SF1-AS1 (14) vs lines expressing it (36) | 2.70× lower at baseline in the lines without TM4SF1-AS1 | 0.047 | ⚠ within organs, on part of the lines; also absent: CXCL1, MBP, TM4SF1; co-absent with the target |

### Downstream of this gene

*7 arrows, 7 of them with an alert ⚠; grade A 0, B 7, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CXCL3]] | B | CXCL1 activity raises CXCL3's level | lines that do not express CXCL1 (17) vs lines expressing it (33) | 2.95× lower at baseline in the lines without CXCL1 | 0.014 | ⚠ within organs, on part of the lines; also absent: CCL20, CDCP1, C15orf48 |
| [[CXCL2]] | B | CXCL1 activity raises CXCL2's level | lines that do not express CXCL1 (17) vs lines expressing it (33) | 2.98× lower at baseline in the lines without CXCL1 | 0.019 | ⚠ within organs, on part of the lines; also absent: CCL20, CDCP1, C15orf48 |
| [[INPP5B]] | B | CXCL1 activity lowers INPP5B's level | lines that do not express CXCL1 (17) vs lines expressing it (33) | 1.34× higher at baseline in the lines without CXCL1 | 0.038 | ⚠ within organs, on part of the lines; also absent: CCL20, CDCP1, C15orf48 |
| [[TNIP1]] | B | CXCL1 activity raises TNIP1's level | lines that do not express CXCL1 (17) vs lines expressing it (33) | 1.45× lower at baseline in the lines without CXCL1 | 0.048 | ⚠ within organs, on part of the lines; also absent: CCL20, CDCP1, C15orf48 |
| [[PMAIP1]] | B | CXCL1 activity raises PMAIP1's level | lines that do not express CXCL1 (17) vs lines expressing it (33) | 1.75× lower at baseline in the lines without CXCL1 | 0.054 | ⚠ within organs, on part of the lines; also absent: CCL20, CDCP1, C15orf48 |
| [[ZC3H12A]] | B | CXCL1 activity raises ZC3H12A's level | lines that do not express CXCL1 (17) vs lines expressing it (33) | 1.66× lower at baseline in the lines without CXCL1 | 0.057 | ⚠ within organs, on part of the lines; also absent: CCL20, CDCP1, C15orf48 |
| [[TNIP1]] | B | CXCL1 activity strengthens TNIP1's drug response | lines that do not express CXCL1 (17) vs lines expressing it (32) | the lines without CXCL1 respond 0.68× as strongly (z diff +1.34); rises at some drug-doses, falls at others (29% from rises): Dinaciclib 5 µM: 0.73x vs 0.53x (z diff +3.7); Harringtonine 5 µM: 1.04x vs 1.54x (z diff +3.5); Dinaciclib 0.5 µM: 0.78x vs 0.61x (z diff +3.0) | 0.081 | ⚠ within organs, on part of the lines; also absent: CCL20, CDCP1, C15orf48; target measured in part of the lines; rises at some drug-doses, falls at others; artifact flags |

## Where it sits

- **Module**: [[Module 014]] — TNF-alpha signaling via NF-kB; 212 genes; every member is in the + arm (projection on the module's main direction 0.587). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.20; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (26.1, 5.8); signed map (41.9, 7.6). **Vector** length 116, 37.7% of its response variance represented; |z| ≥ 3 in 1,073 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +10.0 | +11.1 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +8.7 | +7.2 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +8.6 | +10.7 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +8.3 | +31.0 |
|  | [[Selinexor (drug)]] 5 µM |  | +8.2 | +6.0 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +5.2 | +3.3 |
|  | [[Belumosudil (drug)]] 5 µM |  | +3.1 | +5.4 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | +2.7 | +1.6 |
|  | [[Amsacrine (drug)]] 5 µM |  | +2.6 | +3.8 |
| fall | [[Auranofin (drug)]] 5 µM |  | -5.9 | -5.2 |
|  | [[NG25 (drug)]] 5 µM |  | -3.5 | -4.0 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -3.1 | -1.3 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.8 | -1.5 |
|  | [[Ponatinib (drug)]] 5 µM |  | -2.6 | -7.5 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -2.5 | -3.1 |
|  | [[Ipatasertib (drug)]] 5 µM |  | -2.5 | -3.8 |
|  | [[Niclosamide (olamine) (drug)]] 0.5 µM |  | -2.1 | -1.4 |

## What is on record

|  |  |
|---|---|
| Name | C-X-C motif chemokine ligand 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 4q13.3 — chr4:73,869,393-73,871,308 (+) |
| Ensembl biotype | protein_coding |
| Also known as | SCYB1, GROa, MGSA-a, NAP-3; previously MGSA, GRO1, FSP |
| Gene groups (HGNC) | Chemokine ligands |
| Hallmark sets | IL6_JAK_STAT3_SIGNALING, COMPLEMENT, EPITHELIAL_MESENCHYMAL_TRANSITION, TNFA_SIGNALING_VIA_NFKB |
| Reactome | 12 pathways, smallest: Chemokine receptors bind chemokines; Interleukin-10 signaling; Peptide ligand-binding receptors |
| Matched by | ensembl_id |

**Function**, from UniProt [P09341](https://www.uniprot.org/uniprotkb/P09341) (Growth-regulated alpha protein):

> Has chemotactic activity for neutrophils. May play a role in inflammation and exerts its effects on endothelial cells in an autocrine fashion. In vitro, the processed forms GRO-alpha(4-73), GRO-alpha(5-73) and GRO-alpha(6-73) show a 30-fold higher chemotactic activity.

**Summary**, from NCBI Gene [2919](https://www.ncbi.nlm.nih.gov/gene/2919):

> This antimicrobial gene encodes a member of the CXC subfamily of chemokines. The encoded protein is a secreted growth factor that signals through the G-protein coupled receptor, CXC receptor 2. This protein plays a role in inflammation and as a chemoattractant for neutrophils. Aberrant expression of this protein is associated with the growth and progression of certain tumors. A naturally occurring processed form of this protein has increased chemotactic activity. Alternate splicing results in …

**Accessions** — [HGNC:4602](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:4602) · Entrez [2919](https://www.ncbi.nlm.nih.gov/gene/2919) · UniProt [P09341](https://www.uniprot.org/uniprotkb/P09341) · Ensembl [ENSG00000163739](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000163739)

## Data

Gene col 8769: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8769); `tables/drug_effects.parquet` (41 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8769, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8769]; `tensor/DDL_lfc|DDL_z.npy` [8769]; `embed/gene_vectors.npy` [8769]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8769 or target_col == 8769). Every well: [[CXCL1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CXCL1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
