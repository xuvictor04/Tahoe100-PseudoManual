---
symbol: "XAF1"
type: "gene"
col: 5334
ensembl_id: "ENSG00000132530"
name: "XIAP associated factor 1"
location: "17p13.2"
module: 32
arm: "+"
pooled_cpm: 47.41
n_lines_expressing: 36
n_dd_up: 24
n_dd_down: 55
n_dd_up_clean: 22
n_dd_down_clean: 44
in_vector_space: true
direction_upstream: 49
direction_downstream: 57
tags: ["gene", "module/032"]
generated_by: "tahoemap"
---

# XAF1

*XIAP associated factor 1* — 17p13.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 24 drug-doses (2 with an alert ⚠); the strongest is [[Cobimetinib (drug)]] 5 µM: 2.17× (z +6.2, q 3e-07, up in 30 of 33 measured lines).
> Pooled over the cell lines (median), lowered significantly by 55 drug-doses (11 with an alert ⚠); the strongest is [[Belinostat (drug)]] 5 µM: 0.0698× (z -22.1, q 0e+00, down in 33 of 34 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SAMD9L]] (+0.94, fdr 7e-06), [[RSAD2]] (+0.94, fdr 7e-06), [[OAS2]] (+0.94, fdr 7e-06).
> It is in [[Module 032]], a single-armed module (interferon alpha response).
> Probable direction (from the cell lines, not proof of direct regulation): 49 arrows point to it, the strongest [[OAS2]] → it (grade B ⚠); 57 go from it, the strongest it → [[N4BP1]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 24 in all, 2 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 24 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5334.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Cobimetinib (drug)]] 5 µM |  | **2.17×** | +6.2 | 3e-07 | 30/33 (Hs 766T, AsPC-1, …) | rises with dose |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.90×** | +5.4 | 2e-05 | 27/34 (NCI-H2347, HS-578T, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); position effect removed |
| [[Binimetinib (drug)]] 5 µM |  | **1.65×** | +4.4 | 0.002 | 26/34 (Hs 766T, CFPAC-1, …) | all doses, flat | noisy plate (z scaled) |
| [[Trametinib (drug)]] 0.05 µM |  | **1.43×** | +4.2 | 0.004 | 24/34 (Hs 766T, CFPAC-1, …) | all doses, flat | position effect removed |
| [[Binimetinib (drug)]] 0.05 µM |  | **1.42×** | +4.1 | 0.004 | 24/34 (Hs 766T, CFPAC-1, …) | all doses, flat |  |
| [[Trametinib (drug)]] 0.5 µM |  | **1.50×** | +4.1 | 0.004 | 23/34 (Hs 766T, AsPC-1, …) | all doses, flat | noisy plate (z scaled); position effect removed |
| [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **1.55×** | +4.0 | 0.005 | 22/34 (Hs 766T, CFPAC-1, …) | all doses, flat | noisy plate (z scaled); position effect removed |
| [[Cobimetinib (drug)]] 0.5 µM |  | **1.59×** | +3.9 | 0.006 | 23/33 (Hs 766T, MIA PaCa-2, …) | rises with dose |  |
| [[Binimetinib (drug)]] 0.5 µM |  | **1.44×** | +3.9 | 0.006 | 21/34 (Hs 766T, MIA PaCa-2, …) | all doses, flat | noisy plate (z scaled) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **1.62×** | +3.9 | 0.006 | 20/34 (Hs 766T, PANC-1, …) | all doses, stronger at high dose |  |
| [[Docetaxel (drug)]] 5 µM |  | **1.36×** | +3.6 | 0.014 | 23/34 (NCI-H2347, LoVo, …) | rises with dose |  |
| [[Abiraterone acetate (drug)]] 0.05 µM |  | **1.51×** | +3.5 | 0.024 | 20/34 (SK-MEL-2, HepG2/C3A, …) | inconsistent across doses |  |
| [[Omeprazole (drug)]] 0.05 µM |  | **1.51×** | +3.4 | 0.025 | 23/34 (A-172, SW 900, …) | inconsistent across doses |  |
| [[venetoclax (drug)]] 0.05 µM |  | **1.54×** | +3.4 | 0.027 | 21/34 (AsPC-1, SW 900, …) | inconsistent across doses |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **1.49×** | +3.4 | 0.028 | 20/34 (NCI-H1792, AsPC-1, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); position effect removed |
| [[Elimusertib hydrochloride (drug)]] 0.05 µM |  | **1.53×** | +3.4 | 0.028 | 19/34 (Hs 766T, MIA PaCa-2, …) | inconsistent across doses | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 55 in all, 11 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 55 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 11 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 5334.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Belinostat (drug)]] 5 µM |  | **0.0698×** | -22.1 | 0e+00 | 33/34 (LoVo, RPMI-7951, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.0854×** | -20.5 | 0e+00 | 34/34 (LoVo, RPMI-7951, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.112×** | -18.2 | 0e+00 | 34/34 (LoVo, RPMI-7951, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here) |
| [[Tofacitinib (drug)]] 5 µM |  | **0.259×** | -15.9 | 0e+00 | 27/34 (LoVo, KATO III, …) | rises with dose |  |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **0.208×** | -13.0 | 9e-37 | 32/34 (LoVo, A-172, …) | top dose only |  |
| [[Tofacitinib (citrate) (drug)]] 5 µM |  | **0.343×** | -12.6 | 3e-34 | 28/34 (LoVo, RPMI-7951, …) | all doses, stronger at high dose |  |
| [[Selinexor (drug)]] 5 µM |  | **0.358×** | -12.0 | 2e-31 | 30/34 (HS-578T, MIA PaCa-2, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.369×** | -11.7 | 1e-29 | 26/33 (A-172, SW 900, …) | top dose only | cell-cycle shift (explains ~18% here); composition shift |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.246×** | -11.7 | 1e-29 | 32/34 (A-172, RPMI-7951, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **0.294×** | -10.2 | 2e-22 | 33/34 (NCI-H1792, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here) |
| [[Tofacitinib (citrate) (drug)]] 0.5 µM |  | **0.329×** | -9.2 | 2e-18 | 28/34 (LoVo, KATO III, …) | all doses, stronger at high dose |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.317×** | -9.2 | 2e-18 | 26/32 (MIA PaCa-2, LoVo, …) | rises with dose | cell-cycle shift (explains ~15% here); position effect removed |
| [[Tofacitinib (drug)]] 0.5 µM |  | **0.349×** | -8.7 | 1e-16 | 28/34 (LoVo, NCI-H1792, …) | rises with dose |  |
| [[Auranofin (drug)]] 5 µM |  | **0.352×** | -8.7 | 2e-16 | 29/34 (LoVo, KATO III, …) | rises with dose |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.380×** | -8.0 | 4e-14 | 27/34 (LoVo, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~25% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.380×** | -8.0 | 4e-14 | 31/34 (LoVo, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.507×** | -7.9 | 6e-14 | 29/32 (A498, COLO 205, …) | top dose only | cell-cycle shift (explains ~12% here); position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.39 per unit of S-phase module lfc, -0.19 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5334. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LoVo (line)]] | wt | 149 | 0 | 22 (4 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.0185× (z -28.1) |
| [[MIA PaCa-2 (line)]] | alt | 57.8 | 0 | 20 (4 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.00748× (z -21.5) ⚠ toxic · without an alert: [[Belinostat (drug)]] 5 µM 0.0331× (z -15.5) |
| [[A549 (line)]] | wt | 53.8 | 0 | 18 (3 ⚠) | — | [[Belinostat (drug)]] 5 µM 0.0135× (z -19.2) |
| [[A-172 (line)]] | wt | 49.5 | 0 | 17 (4 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.0247× (z -21.1) |
| [[RPMI-7951 (line)]] | alt | 182 | 0 | 14 (4 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.0458× (z -25.1) |
| [[COLO 205 (line)]] | alt | 400 | 0 | 13 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.0326× (z -23.5) |
| [[HepG2_C3A (line)]] | wt | 40.8 | 0 | 13 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.107× (z -15.4) |
| [[NCI-H1792 (line)]] | alt | 25.3 | 0 | 13 (3 ⚠) | — | [[Belinostat (drug)]] 5 µM 0.0261× (z -18.8) |
| [[SW 900 (line)]] | alt | 92.3 | 0 | 13 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.0640× (z -18.8) |
| [[BT-474 (line)]] | alt | 26.8 | 0 | 12 | — | [[Panobinostat (drug)]] 5 µM 0.0481× (z -12.2) |
| [[CFPAC-1 (line)]] | alt | 97.3 | 1 (1 ⚠) | 11 (4 ⚠) | [[Harringtonine (drug)]] 5 µM 3.97× (z +9.2) ⚠ cell-cycle shift, explains ~94% of this change | [[Panobinostat (drug)]] 5 µM 0.0840× (z -17.1) |
| [[KATO III (line)]] | alt | 146 | 0 | 12 (3 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.0346× (z -22.4) |
| [[SK-MEL-2 (line)]] | alt | 64.6 | 0 | 11 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.0389× (z -19.9) |
| [[SNU-423 (line)]] | alt | 102 | 0 | 11 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.0361× (z -18.4) |
| [[NCI-H2347 (line)]] | alt | 42.2 | 3 (1 ⚠) | 7 | [[Homoharringtonine (drug)]] 0.5 µM 6.19× (z +12.6) | [[Tofacitinib (drug)]] 5 µM 0.236× (z -14.0) |
| [[AsPC-1 (line)]] | alt | 60.9 | 0 | 9 (2 ⚠) | — | [[Tofacitinib (drug)]] 5 µM 0.145× (z -15.8) |
| [[HS-578T (line)]] | alt | 79.2 | 2 | 7 | [[Homoharringtonine (drug)]] 0.5 µM 4.89× (z +10.3) | [[Panobinostat (drug)]] 5 µM 0.0328× (z -22.0) |
| [[NCI-H1573 (line)]] | alt | 24.3 | 0 | 8 | — | [[Panobinostat (drug)]] 5 µM 0.0390× (z -16.3) |
| [[Panc 03.27 (line)]] | alt | 87.2 | 2 (1 ⚠) | 6 | [[Homoharringtonine (drug)]] 0.5 µM 3.82× (z +9.1) | [[Panobinostat (drug)]] 5 µM 0.166× (z -12.1) |
| [[PANC-1 (line)]] | alt | 18.5 | 1 | 7 (1 ⚠) | [[Harringtonine (drug)]] 0.5 µM 3.92× (z +9.1) | [[Homoharringtonine (drug)]] 5 µM 0.201× (z -15.0) |
| [[A498 (line)]] | wt | 97.5 | 0 | 7 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.0803× (z -15.1) |
| [[Hs 766T (line)]] | wt | 62.7 | 0 | 6 | — | [[Panobinostat (drug)]] 5 µM 0.0929× (z -14.4) |
| [[H4 (line)]] | wt | 36.5 | 0 | 5 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.124× (z -13.7) |
| [[SHP-77 (line)]] | alt | 21.7 | 0 | 5 | — | [[Belinostat (drug)]] 5 µM 0.0182× (z -16.5) |
| [[SW1417 (line)]] | alt | 28.3 | 0 | 4 | — | [[Belinostat (drug)]] 5 µM 0.0953× (z -12.2) |
| [[C32 (line)]] | wt | 39.1 | 0 | 3 | — | [[Belinostat (drug)]] 5 µM 0.0377× (z -15.2) |
| [[HOP62 (line)]] | alt | 17.0 | 0 | 3 (1 ⚠) | — | [[Belinostat (drug)]] 5 µM 0.0658× (z -14.4) |
| [[hTERT-HPNE (line)]] | wt | 30.3 | 0 | 2 | — | [[Panobinostat (drug)]] 5 µM 0.156× (z -10.3) |
| [[J82 (line)]] | alt | 48.4 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 5.57× (z +9.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~65% of this change | [[Panobinostat (drug)]] 0.5 µM 0.178× (z -9.3) |
| [[CHP-212 (line)]] | wt | 20.7 | 0 | 1 | — | [[Belinostat (drug)]] 5 µM 0.0213× (z -10.3) |
| [[A-427 (line)]] | wt | 3.34 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 22.2 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 11.4 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 7.01 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 4.35 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 5.42 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 5.41 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 12.1 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 4.60 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 35.9 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 10.5 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 4.01 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 36.3 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 4.83 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 8.69 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 12.7 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 54.2 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 7.31 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 5.30 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 3.76 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5334), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SAMD9L]] | +0.94 | +0.87 / +0.96 | both halves | 7e-06 | pathway: HALLMARK_INTERFERON_GAMMA_RESPONSE; STRING 870 |
| [[RSAD2]] | +0.94 | +0.88 / +0.94 | both halves | 7e-06 | pathway: HALLMARK_INTERFERON_GAMMA_RESPONSE; STRING 900 |
| [[OAS2]] | +0.94 | +0.86 / +0.96 | both halves | 7e-06 | pathway: HALLMARK_INTERFERON_GAMMA_RESPONSE; STRING 933 |
| [[IFIT3]] | +0.93 | +0.87 / +0.94 | both halves | 7e-06 | pathway: HALLMARK_INTERFERON_GAMMA_RESPONSE; STRING 938 |
| [[MX1]] | +0.93 | +0.84 / +0.95 | both halves | 7e-06 | pathway: HALLMARK_INTERFERON_GAMMA_RESPONSE; STRING 925 |
| [[EPSTI1]] | +0.93 | +0.85 / +0.94 | both halves | 7e-06 | pathway: HALLMARK_INTERFERON_GAMMA_RESPONSE; STRING 862 |
| [[MX2]] | +0.92 | +0.85 / +0.94 | both halves | 7e-06 | pathway: HALLMARK_INTERFERON_GAMMA_RESPONSE; STRING 869 |
| [[CMPK2]] | +0.92 | +0.83 / +0.95 | both halves | 7e-06 | pathway: HALLMARK_INTERFERON_GAMMA_RESPONSE; STRING 653 |
| [[IFI35]] | +0.92 | +0.84 / +0.94 | both halves | 7e-06 | pathway: HALLMARK_INTERFERON_GAMMA_RESPONSE; STRING 852 |
| [[PARP9]] | +0.92 | +0.81 / +0.95 | both halves | 7e-06 | STRING 894 |
| [[OAS1]] | +0.91 | +0.84 / +0.94 | both halves | 7e-06 | pathway: Interferon Signaling; STRING 887 |
| [[IFI44]] | +0.91 | +0.82 / +0.93 | both halves | 7e-06 | pathway: HALLMARK_INTERFERON_GAMMA_RESPONSE; STRING 970 |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*49 arrows, 49 of them with an alert ⚠; grade A 0, B 33, C 16. Shown: the 12 strongest; 37 more arrows (37 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[OAS2]] | B | OAS2 activity raises XAF1's level | lines that do not express OAS2 (14) vs lines expressing it (36) | 4.66× lower at baseline in the lines without OAS2 | 0.001 | ⚠ within organs, on part of the lines; also absent: OAS1, CMPK2, MX1 |
| [[OAS1]] | B | OAS1 activity raises XAF1's level | lines that do not express OAS1 (13) vs lines expressing it (37) | 3.82× lower at baseline in the lines without OAS1 | 0.003 | ⚠ within organs, on part of the lines; also absent: OAS2, TRIM22, IFI27; maybe low, not absent |
| [[MX1]] | B | MX1 activity raises XAF1's level | lines that do not express MX1 (19) vs lines expressing it (31) | 3.34× lower at baseline in the lines without MX1 | 0.003 | ⚠ within organs, on part of the lines; also absent: OAS2, SRMS, EPSTI1 |
| [[MMP13]] | B | MMP13 activity raises XAF1's level | lines that do not express MMP13 (30) vs lines expressing it (20) | 2.68× lower at baseline in the lines without MMP13 | 0.004 | ⚠ within organs, on part of the lines; also absent: SOX11, AGT, STEAP4 |
| [[EPSTI1]] | B | EPSTI1 activity raises XAF1's level | lines that do not express EPSTI1 (25) vs lines expressing it (25) | 4.02× lower at baseline in the lines without EPSTI1 | 0.006 | ⚠ within organs, on part of the lines; also absent: UGT1A6, PKP1, ENSG00000271933 |
| [[PLAAT4]] | B | PLAAT4 activity raises XAF1's level | lines that do not express PLAAT4 (21) vs lines expressing it (29) | 3.03× lower at baseline in the lines without PLAAT4 | 0.011 | ⚠ within organs, on part of the lines; also absent: PTPRB, TNFSF10, EPSTI1 |
| [[FYB1]] | B | FYB1 activity raises XAF1's level | lines that do not express FYB1 (32) vs lines expressing it (18) | 2.90× lower at baseline in the lines without FYB1 | 0.014 | ⚠ within organs, on part of the lines; also absent: AMPH, IRAG2, ENSG00000266450 |
| [[APOL1]] | B | APOL1 activity raises XAF1's level | lines that do not express APOL1 (24) vs lines expressing it (26) | 3.79× lower at baseline in the lines without APOL1 | 0.018 | ⚠ within organs, on part of the lines; also absent: POU5F1, UGT1A6, NMRAL2P-1 |
| [[GBP1]] | B | GBP1 activity raises XAF1's level | lines that do not express GBP1 (16) vs lines expressing it (34) | 3.70× lower at baseline in the lines without GBP1 | 0.018 | ⚠ within organs, on part of the lines; also absent: GBP4, GBP2, SAMD9 |
| [[IFI44L]] | B | IFI44L activity raises XAF1's level | lines that do not express IFI44L (22) vs lines expressing it (28) | 3.12× lower at baseline in the lines without IFI44L | 0.031 | ⚠ within organs, on part of the lines; also absent: GBP1, EPSTI1, GBP4 |
| [[CTSS]] | B | CTSS activity raises XAF1's level | lines that do not express CTSS (15) vs lines expressing it (35) | 3.02× lower at baseline in the lines without CTSS | 0.033 | ⚠ within organs, on part of the lines; also absent: LINC02257, NMRAL2P-1, CSF2; maybe low, not absent |
| [[GBP5]] | B | GBP5 activity raises XAF1's level | lines that do not express GBP5 (24) vs lines expressing it (26) | 2.59× lower at baseline in the lines without GBP5 | 0.039 | ⚠ within organs, on part of the lines; also absent: ADAMTS16, EDNRA, CHSY3 |

### Downstream of this gene

*57 arrows, 57 of them with an alert ⚠; grade A 0, B 43, C 14. Shown: the 12 strongest; 45 more arrows (45 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[N4BP1]] | B | XAF1 activity raises N4BP1's level | lines that do not express XAF1 (14) vs lines expressing it (36) | 1.29× lower at baseline in the lines without XAF1 | 0.001 | ⚠ within organs, on part of the lines; also absent: SLC15A3, TRIM22, FBXO39 |
| [[OAS2]] | B | XAF1 activity raises OAS2's level | lines that do not express XAF1 (14) vs lines expressing it (36) | 4.80× lower at baseline in the lines without XAF1 | 0.002 | ⚠ within organs, on part of the lines; also absent: SLC15A3, TRIM22, FBXO39 |
| [[APOL6]] | B | XAF1 activity raises APOL6's level | lines that do not express XAF1 (14) vs lines expressing it (36) | 2.65× lower at baseline in the lines without XAF1 | 0.006 | ⚠ within organs, on part of the lines; also absent: SLC15A3, TRIM22, FBXO39 |
| [[TMEM140]] | B | XAF1 activity raises TMEM140's level | lines that do not express XAF1 (14) vs lines expressing it (36) | 2.63× lower at baseline in the lines without XAF1 | 0.007 | ⚠ within organs, on part of the lines; also absent: SLC15A3, TRIM22, FBXO39 |
| [[OAS1]] | B | XAF1 activity raises OAS1's level | lines that do not express XAF1 (14) vs lines expressing it (36) | 3.09× lower at baseline in the lines without XAF1 | 0.008 | ⚠ within organs, on part of the lines; also absent: SLC15A3, TRIM22, FBXO39 |
| [[CFB]] | B | XAF1 activity raises CFB's level | lines that do not express XAF1 (14) vs lines expressing it (36) | 4.49× lower at baseline in the lines without XAF1 | 0.010 | ⚠ within organs, on part of the lines; also absent: SLC15A3, TRIM22, FBXO39 |
| [[NLRC5]] | B | XAF1 activity raises NLRC5's level | lines that do not express XAF1 (14) vs lines expressing it (36) | 2.09× lower at baseline in the lines without XAF1 | 0.011 | ⚠ within organs, on part of the lines; also absent: SLC15A3, TRIM22, FBXO39 |
| [[PARP10]] | B | XAF1 activity raises PARP10's level | lines that do not express XAF1 (14) vs lines expressing it (36) | 1.89× lower at baseline in the lines without XAF1 | 0.013 | ⚠ within organs, on part of the lines; also absent: SLC15A3, TRIM22, FBXO39 |
| [[CMPK2]] | B | XAF1 activity raises CMPK2's level | lines that do not express XAF1 (14) vs lines expressing it (36) | 2.70× lower at baseline in the lines without XAF1 | 0.019 | ⚠ within organs, on part of the lines; also absent: SLC15A3, TRIM22, FBXO39 |
| [[IFI44L]] | B | XAF1 activity raises IFI44L's level | lines that do not express XAF1 (14) vs lines expressing it (36) | 4.49× lower at baseline in the lines without XAF1 | 0.021 | ⚠ within organs, on part of the lines; also absent: SLC15A3, TRIM22, FBXO39 |
| [[PLSCR1]] | B | XAF1 activity raises PLSCR1's level | lines that do not express XAF1 (14) vs lines expressing it (36) | 2.79× lower at baseline in the lines without XAF1 | 0.022 | ⚠ within organs, on part of the lines; also absent: SLC15A3, TRIM22, FBXO39 |
| [[PARP14]] | B | XAF1 activity raises PARP14's level | lines that do not express XAF1 (14) vs lines expressing it (36) | 2.23× lower at baseline in the lines without XAF1 | 0.025 | ⚠ within organs, on part of the lines; also absent: SLC15A3, TRIM22, FBXO39 |

## Where it sits

- **Module**: [[Module 032]] — interferon alpha response; 139 genes; every member is in the + arm (projection on the module's main direction 0.951). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.31; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (48.1, 53.5); signed map (64.3, 31.5). **Vector** length 145, 55.7% of its response variance represented; |z| ≥ 3 in 1,526 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *interferon alpha response* (hallmark, mean cos +0.79 to 56); *Interferon gamma signaling* (reactome, mean cos +0.79 to 17); *Antimicrobial mechanism of IFN-stimulated genes* (reactome, mean cos +0.85 to 21).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Harringtonine (drug)]] 0.5 µM |  | +10.8 | +5.4 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +9.0 | +2.5 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +5.9 | +2.4 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~94% of this change | +5.8 | -1.7 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +5.5 | +6.2 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +4.6 | -0.1 |
|  | [[Binimetinib (drug)]] 5 µM |  | +4.2 | +4.4 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | +4.0 | +3.9 |
| fall | [[Tofacitinib (drug)]] 5 µM |  | -9.3 | -15.9 |
|  | [[Tofacitinib (citrate) (drug)]] 5 µM |  | -7.8 | -12.6 |
|  | [[Tofacitinib (drug)]] 0.5 µM |  | -7.8 | -8.7 |
|  | [[Tofacitinib (citrate) (drug)]] 0.5 µM |  | -7.4 | -9.2 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | -7.0 | -13.0 |

## What is on record

|  |  |
|---|---|
| Name | XIAP associated factor 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 17p13.2 — chr17:6,755,447-6,775,647 (+) |
| Ensembl biotype | protein_coding |
| Also known as | BIRC4BP, XIAPAF1, HSXIAPAF1 |
| Gene groups (HGNC) | Zinc fingers TRAF-type |
| Hallmark sets | INTERFERON_GAMMA_RESPONSE |
| Reactome | 3 pathways, smallest: Interferon alpha/beta signaling; Interferon Signaling; Cytokine Signaling in Immune system |
| Matched by | ensembl_id |

**Function**, from UniProt [Q6GPH4](https://www.uniprot.org/uniprotkb/Q6GPH4) (XIAP-associated factor 1):

> Seems to function as a negative regulator of members of the IAP (inhibitor of apoptosis protein) family. Inhibits anti-caspase activity of BIRC4. Induces cleavage and inactivation of BIRC4 independent of caspase activation. Mediates TNF-induced apoptosis and is involved in apoptosis in trophoblast cells. May inhibit BIRC4 indirectly by activating the mitochondrial apoptosis pathway. After translocation to mitochondria, promotes translocation of BAX to mitochondria and cytochrome c release from …

**Summary**, from NCBI Gene [54739](https://www.ncbi.nlm.nih.gov/gene/54739):

> This gene encodes a protein which binds to and counteracts the inhibitory effect of a member of the IAP (inhibitor of apoptosis) protein family. IAP proteins bind to and inhibit caspases which are activated during apoptosis. The proportion of IAPs and proteins which interfere with their activity, such as the encoded protein, affect the progress of the apoptosis signaling pathway. Multiple transcript variants encoding different isoforms have been found for this gene. [provided by RefSeq, Feb …

**Accessions** — [HGNC:30932](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:30932) · Entrez [54739](https://www.ncbi.nlm.nih.gov/gene/54739) · UniProt [Q6GPH4](https://www.uniprot.org/uniprotkb/Q6GPH4) · Ensembl [ENSG00000132530](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000132530)

## Data

Gene col 5334: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5334); `tables/drug_effects.parquet` (79 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5334, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5334]; `tensor/DDL_lfc|DDL_z.npy` [5334]; `embed/gene_vectors.npy` [5334]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5334 or target_col == 5334). Every well: [[XAF1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/XAF1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
