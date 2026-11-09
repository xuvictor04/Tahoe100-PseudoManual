---
symbol: "MATCAP1"
type: "gene"
col: 12133
ensembl_id: "ENSG00000196123"
name: "microtubule associated tyrosine carboxypeptidase 1"
location: "16q22.1"
module: 23
arm: "-"
pooled_cpm: 8.32
n_lines_expressing: 50
n_dd_up: 8
n_dd_down: 18
n_dd_up_clean: 6
n_dd_down_clean: 14
in_vector_space: true
direction_upstream: 3
direction_downstream: 0
tags: ["gene", "module/023"]
generated_by: "tahoemap"
---

# MATCAP1

*microtubule associated tyrosine carboxypeptidase 1* — 16q22.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 8 drug-doses (2 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 2.95× (z +11.8, q 4e-29, up in 42 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 18 drug-doses (4 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 0.5 µM: 0.553× (z -6.4, q 7e-08, down in 26 of 41 measured lines).
> Its strongest partners by |cos| (74 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 26 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[RHPN1]] (+0.68, fdr 1e-04), [[TCIRG1]] (+0.65, fdr 5e-05), [[KCTD17]] (+0.63, fdr 0.001, ⚠ one half only (not replicated)), [[SKIC2]] (+0.63, fdr 1e-05); moves opposite to [[UBXN2A]] (-0.63, fdr 7e-05), [[PPP1R12A-AS2]] (-0.62, fdr 1e-04), [[N4BP2L1]] (-0.62, fdr 2e-04).
> It sits in the **-** arm of [[Module 023]].
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[HDAC6]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 3 with an alert ⚠. 8 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 12133.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **2.95×** | +11.8 | 4e-29 | 42/47 (A498, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here) |
| [[Belinostat (drug)]] 5 µM |  | **2.48×** | +9.9 | 2e-20 | 39/47 (A498, SW480, …) | rises with dose | cell-cycle shift (explains ~15% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **2.40×** | +9.5 | 5e-19 | 38/46 (A498, MIA PaCa-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.56×** | +4.8 | 2e-04 | 20/47 (NCI-H460, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **1.46×** | +4.1 | 0.004 | 20/44 (A498, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~10% here) |
| [[Cobimetinib (drug)]] 5 µM |  | **1.45×** | +3.9 | 0.009 | 11/45 (NCI-H2030, NCI-H1573, …) | rises with dose | position effect removed |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.11× | +3.7 | 0.017 | 3/48 (HOP62, LOX-IMVI, …) | inconsistent across doses |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change | **1.40×** | +3.5 | 0.029 | 6/17 (J82, PANC-1, …) | inconsistent across doses | composition shift |
| [[Abemaciclib (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.36×** | +3.3 | 0.058 | 6/47 (hTERT-HPNE, NCI-H460, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 18 in all, 4 with an alert ⚠. 18 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 12133.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.553×** | -6.4 | 7e-08 | 26/41 (NCI-H460, hTERT-HPNE, …) | two highest doses | cell-cycle shift (explains ~21% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.690×** | -5.7 | 3e-06 | 24/42 (NCI-H460, NCI-H1792, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~46% of this change | **0.692×** | -5.6 | 3e-06 | 24/44 (NCI-H460, Hs 766T, …) | two highest doses | composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **0.586×** | -5.6 | 3e-06 | 24/45 (NCI-H460, NCI-H1792, …) | rises with dose | cell-cycle shift (explains ~22% here); composition shift; position effect removed |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.600×** | -5.5 | 3e-06 | 24/43 (BT-474, H4, …) | rises with dose | cell-cycle shift (explains ~1% here); position effect removed |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.625×** | -4.9 | 7e-05 | 19/40 (A-172, H4, …) | top dose only | cell-cycle shift (explains ~0% here); position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.637×** | -4.9 | 7e-05 | 21/47 (NCI-H23, SHP-77, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here); composition shift; position effect removed |
| [[Ribociclib (drug)]] 0.05 µM | ⚠ unreliable plate only; position not correctable | **0.656×** | -4.6 | 3e-04 | 19/47 (SW 900, HEC-1-A, …) | inconsistent across doses |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.675×** | -4.3 | 0.001 | 18/46 (SW 900, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here); position effect removed |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **0.761×** | -4.2 | 0.002 | 16/46 (Hs 766T, H4, …) | all doses, stronger at high dose |  |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.689×** | -4.1 | 0.003 | 18/46 (SHP-77, NCI-H23, …) | rises with dose | cell-cycle shift (explains ~1% here); position effect removed |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.699×** | -3.9 | 0.005 | 16/46 (NCI-H460, NCI-H2030, …) | rises with dose | cell-cycle shift (explains ~10% here); position effect removed |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.703×** | -3.8 | 0.006 | 15/47 (A-427, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[TAK-901 (drug)]] 5 µM |  | **0.528×** | -3.6 | 0.012 | 11/44 (NCI-H460, SW480, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~6% here); composition shift; noisy plate (z scaled) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.724×** | -3.4 | 0.027 | 16/36 (RKO, A549, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Peretinoin (drug)]] 5 µM |  | **0.731×** | -3.3 | 0.037 | 10/45 (hTERT-HPNE, NCI-H23, …) | rises with dose | position effect removed |
| [[Selinexor (drug)]] 5 µM |  | **0.816×** | -3.1 | 0.060 | 10/48 (NCI-H23, HCT15, …) | top dose only | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **0.754×** | -3.1 | 0.069 | 9/44 (hTERT-HPNE, NCI-H460, …) | all doses, stronger at high dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.36 per unit of S-phase module lfc, -0.33 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 12133. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[BT-474 (line)]] | alt | 8.05 | 0 | 4 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0709× (z -10.7) ⚠ toxic; transcription drop · without an alert: [[Talc (drug)]] 0.05 µM 0.0736× (z -10.5) |
| [[NCI-H460 (line)]] | wt | 16.8 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.129× (z -14.2) |
| [[Hs 766T (line)]] | wt | 8.36 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.127× (z -11.7) ⚠ cell-cycle shift, explains ~46% of this change · without an alert: [[Bergenin (drug)]] 0.5 µM 0.0961× (z -9.4) |
| [[NCI-H2030 (line)]] | alt | 11.2 | 0 | 2 (2 ⚠) | — | [[Daptomycin (drug)]] 0.5 µM 0.102× (z -10.9) ⚠ unreliable plate only |
| [[C-33 A (line)]] | alt | 9.70 | 0 | 1 | — | [[Palmatine (chloride) (drug)]] 0.5 µM 0.0717× (z -10.5) |
| [[HCT15 (line)]] | alt | 11.2 | 0 | 1 | — | [[Ciclopirox (drug)]] 0.05 µM 0.0658× (z -9.8) |
| [[LoVo (line)]] | wt | 8.55 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.250× (z -10.9) ⚠ cell-cycle shift, explains ~46% of this change |
| [[LOX-IMVI (line)]] | wt | 6.71 | 0 | 1 | — | [[Saquinavir (drug)]] 0.05 µM 0.144× (z -8.5) |
| [[NCI-H1792 (line)]] | alt | 12.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.168× (z -8.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change |
| [[RKO (line)]] | wt | 9.19 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.115× (z -9.1) ⚠ toxic |
| [[RPMI-7951 (line)]] | alt | 9.31 | 0 | 1 | — | [[Bergenin (drug)]] 0.5 µM 0.0977× (z -8.9) |
| [[SW 900 (line)]] | alt | 8.32 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.143× (z -10.9) ⚠ cell-cycle shift, explains ~46% of this change |
| [[A-172 (line)]] | wt | 12.0 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 6.47 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 4.76 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 4.99 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 9.05 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 3.74 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 8.12 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 5.04 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 14.5 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 8.88 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 9.95 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 6.41 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 7.49 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 8.79 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 8.93 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 5.63 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 10.2 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 5.05 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 7.13 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 14.4 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 4.83 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 9.03 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 8.99 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 4.52 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 2.74 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 9.69 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 5.85 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 3.86 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 4.50 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 15.5 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 3.51 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 4.53 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 3.66 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 8.77 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 6.83 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 6.12 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 7.84 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 17.8 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 12133), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*42 of its nearest partners move with it, 7 of them with an alert (⚠; 7 not replicated); shown: the 12 strongest and the 2 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RHPN1]] | +0.68 | +0.63 / +0.35 | both halves | 1e-04 |  |
| [[TCIRG1]] | +0.65 | +0.63 / +0.39 | both halves | 5e-05 |  |
| [[KCTD17]] | +0.63 | +0.65 / +0.17 | ⚠ one half (not replicated) | 0.001 |  |
| [[SKIC2]] | +0.63 | +0.53 / +0.50 | both halves | 1e-05 |  |
| [[CHTF18]] | +0.61 | +0.50 / +0.32 | both halves | 1e-04 |  |
| [[PLPPR2]] | +0.60 | +0.44 / +0.35 | both halves | 1e-04 |  |
| [[CEP131]] | +0.60 | +0.46 / +0.17 | ⚠ not reproduced | 0.001 |  |
| [[INTS1]] | +0.58 | +0.55 / +0.38 | both halves | 7e-05 |  |
| [[CADM4]] | +0.58 | +0.46 / +0.26 | both halves | 4e-04 |  |
| [[PLOD1]] | +0.58 | +0.54 / +0.52 | both halves | 1e-05 |  |
| [[TUBGCP6]] | +0.57 | +0.44 / +0.46 | both halves | 3e-05 |  |
| [[NCKIPSD]] | +0.57 | +0.55 / +0.41 | both halves | 4e-05 |  |
| [[NXPH4]] | +0.57 | +0.52 / +0.31 | both halves | 2e-04 |  |
| [[SIPA1]] | +0.57 | +0.47 / +0.22 | both halves | 6e-04 |  |

## Genes that move opposite

*58 of its nearest partners move opposite, 19 of them with an alert (⚠; 19 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[UBXN2A]] | -0.63 | -0.60 / -0.38 | both halves | 7e-05 |  |
| [[PPP1R12A-AS2]] | -0.62 | -0.51 / -0.33 | both halves | 1e-04 |  |
| [[N4BP2L1]] | -0.62 | -0.56 / -0.31 | both halves | 2e-04 |  |
| [[CCDC122]] | -0.62 | -0.56 / -0.29 | both halves | 3e-04 |  |
| [[ATE1OSP]] | -0.61 | -0.53 / -0.27 | both halves | 3e-04 |  |
| [[YARS2]] | -0.59 | -0.49 / -0.23 | both halves | 5e-04 |  |
| [[RXYLT1]] | -0.59 | -0.49 / -0.39 | both halves | 5e-05 |  |
| [[ZBTB8A]] | -0.59 | -0.52 / -0.24 | both halves | 5e-04 |  |
| [[EIF3J-DT]] | -0.59 | -0.50 / -0.31 | both halves | 2e-04 |  |
| [[DNAI4]] | -0.58 | -0.54 / -0.29 | both halves | 2e-04 |  |
| [[HSPBAP1]] | -0.58 | -0.46 / -0.44 | both halves | 3e-05 |  |
| [[CASS4]] | -0.57 | -0.50 / -0.23 | both halves | 5e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 2, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HDAC6]] | B | HDAC6 activity lowers MATCAP1's level | compounds that target HDAC6: 2 of 2 raise it (Belinostat, Panobinostat) | 100% of the class's compounds vs 1.4% of all compounds | 0.071 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[FGFR4]] | B | FGFR4 activity lowers MATCAP1's level | lines that do not express FGFR4 (11) vs lines expressing it (39) | 1.18× higher at baseline in the lines without FGFR4 | 0.072 | ⚠ within organs, on part of the lines; also absent: CAMSAP3, PATJ, LLGL2; maybe low, not absent |
| [[RFX3-DT]] | C | RFX3-DT activity raises MATCAP1's level | lines that do not express RFX3-DT (3) vs lines expressing it (47) | 1.63× lower at baseline in the lines without RFX3-DT | 0.089 | ⚠ few lines (3 vs 47); within organs, on part of the lines; co-absent genes; also absent: POGLUT2, ANAPC1P4, WDR35; maybe low, not absent; its own permutation p |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 023]]; 179 genes; this gene is in the **-** arm (projection on the module's main direction -0.576). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.34).
- **Nodal map** (x, y) = (6.1, -4.9); signed map (-30.8, 0.4). **Vector** length 75.8, 13.0% of its response variance represented; |z| ≥ 3 in 990 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Panobinostat (drug)]] 0.5 µM |  | +5.2 | +9.5 |
|  | [[Panobinostat (drug)]] 5 µM |  | +5.1 | +11.8 |
|  | [[Belinostat (drug)]] 5 µM |  | +4.6 | +9.9 |
|  | [[Belinostat (drug)]] 0.5 µM |  | +2.7 | +4.1 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change | +2.2 | +3.5 |
|  | [[venetoclax (drug)]] 5 µM |  | +2.0 | +1.2 |
|  | [[Sapanisertib (drug)]] 0.5 µM |  | +1.8 | +1.5 |
|  | [[Dimethyl fumarate (drug)]] 5 µM |  | +1.8 | +1.8 |
|  | [[Infigratinib (drug)]] 0.05 µM |  | +1.5 | +1.2 |
|  | [[TAK-733 (drug)]] 5 µM |  | +1.5 | +1.9 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -4.3 | -5.7 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -4.1 | -6.4 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~46% of this change | -3.1 | -5.6 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | -3.0 | -4.9 |
|  | [[Harringtonine (drug)]] 5 µM |  | -2.6 | -5.6 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -2.5 | -1.8 |
|  | [[AZD-8055 (drug)]] 0.5 µM |  | -2.1 | -1.9 |
|  | [[Rapamycin (drug)]] 5 µM |  | -2.1 | -2.0 |
|  | [[Temsirolimus (drug)]] 5 µM |  | -1.9 | -1.7 |
|  | [[Peretinoin (drug)]] 5 µM |  | -1.9 | -3.3 |

## What is on record

|  |  |
|---|---|
| Name | microtubule associated tyrosine carboxypeptidase 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 16q22.1 — chr16:67,175,599-67,184,040 (-) |
| Ensembl biotype | protein_coding |
| Also known as | LOC653319, TMCP1; previously KIAA0895L |
| Gene groups (HGNC) | Microtubule associated tyrosine carboxypeptidase family |
| Matched by | ensembl_id |

**Function**, from UniProt [Q68EN5](https://www.uniprot.org/uniprotkb/Q68EN5) (Microtubule-associated tyrosine carboxypeptidase 1):

> Tyrosine carboxypeptidase that removes the C-terminal tyrosine residue of alpha-tubulin, thereby regulating microtubule dynamics and function. Also able to remove the C-terminal phenylalanine residue of alpha-tubulin TUBA8. Recognizes adjacent tubulin dimers along the same protofilament.

**Summary**, from NCBI Gene [653319](https://www.ncbi.nlm.nih.gov/gene/653319):

> Enables tubulin-tyrosine carboxypeptidase activity. Predicted to be involved in brain development. Is active in microtubule. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:34408](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:34408) · Entrez [653319](https://www.ncbi.nlm.nih.gov/gene/653319) · UniProt [Q68EN5](https://www.uniprot.org/uniprotkb/Q68EN5) · Ensembl [ENSG00000196123](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000196123)

## Data

Gene col 12133: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 12133); `tables/drug_effects.parquet` (27 rows, flagged included); `relations/gene_relations.parquet` (col_a == 12133, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 12133]; `tensor/DDL_lfc|DDL_z.npy` [12133]; `embed/gene_vectors.npy` [12133]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 12133 or target_col == 12133). Every well: [[MATCAP1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MATCAP1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
