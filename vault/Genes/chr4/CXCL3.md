---
symbol: "CXCL3"
type: "gene"
col: 8766
ensembl_id: "ENSG00000163734"
name: "C-X-C motif chemokine ligand 3"
location: "4q13.3"
module: 14
arm: "+"
pooled_cpm: 38.15
n_lines_expressing: 36
n_dd_up: 35
n_dd_down: 5
n_dd_up_clean: 23
n_dd_down_clean: 5
in_vector_space: true
direction_upstream: 20
direction_downstream: 47
tags: ["gene", "module/014"]
generated_by: "tahoemap"
---

# CXCL3

*C-X-C motif chemokine ligand 3* — 4q13.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 35 drug-doses (12 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 22.7× (z +26.6, q 0e+00, up in 34 of 34 measured lines).
> Pooled over the cell lines (median), lowered significantly by 5 drug-doses (none with an alert); the strongest is [[Tirabrutinib (hydrochloride) (drug)]] 0.5 µM: 0.522× (z -3.9, q 0.028, down in 20 of 34 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CXCL2]] (+0.87, fdr 7e-06), [[CXCL1]] (+0.77, fdr 7e-06), [[TNFAIP2]] (+0.72, fdr 7e-06); moves opposite to [[AP1M1]] (-0.60, fdr 1e-05), [[PCMT1]] (-0.55, fdr 2e-04), [[SLC25A42]] (-0.52, fdr 2e-04).
> It is in [[Module 014]], a single-armed module (TNF-alpha signaling via NF-kB).
> Probable direction (from the cell lines, not proof of direct regulation): 20 arrows point to it, the strongest [[CSF3]] → it (grade B ⚠); 47 go from it, the strongest it → [[CXCL1]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 35 in all, 12 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 35 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 12 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8766.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **22.7×** | +26.6 | 0e+00 | 34/34 (NCI-H2347, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **39.0×** | +21.2 | 0e+00 | 34/34 (NCI-H2347, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~10% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **9.74×** | +13.7 | 1e-40 | 31/34 (HEC-1-A, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **6.95×** | +11.7 | 2e-29 | 29/34 (NCI-H460, A-172, …) | rises with dose | cell-cycle shift (explains ~8% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **3.57×** | +10.9 | 2e-25 | 26/34 (BT-474, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~4% here) |
| [[Selinexor (drug)]] 5 µM |  | **3.38×** | +10.4 | 2e-23 | 31/34 (MIA PaCa-2, A-172, …) | all doses, stronger at high dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 0.5 µM |  | **3.96×** | +8.3 | 8e-15 | 31/34 (KATO III, MIA PaCa-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[TAK-901 (drug)]] 5 µM |  | **12.3×** | +7.9 | 2e-13 | 33/34 (LoVo, SW1417, …) | rises with dose | plate-row cell shift; cell-cycle shift (explains ~11% here); composition shift; noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **4.02×** | +7.8 | 5e-13 | 27/31 (NCI-H460, A549, …) | all doses, flat | cell-cycle shift (explains ~23% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **3.49×** | +7.6 | 2e-12 | 26/34 (NCI-H460, SW 900, …) | all doses, stronger at high dose | composition shift; position effect removed |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | **3.39×** | +7.4 | 8e-12 | 28/33 (NCI-H460, SW 900, …) | rises with dose |  |
| [[Belumosudil (drug)]] 5 µM |  | **3.26×** | +6.9 | 3e-10 | 27/34 (NCI-H1792, MIA PaCa-2, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **3.25×** | +6.8 | 3e-10 | 24/32 (MIA PaCa-2, CFPAC-1, …) | inconsistent across doses | cell-cycle shift (explains ~1% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **3.01×** | +6.4 | 6e-09 | 25/33 (NCI-H460, MIA PaCa-2, …) | top dose only | cell-cycle shift (explains ~24% here) |
| [[Selinexor (drug)]] 0.05 µM |  | **2.54×** | +5.6 | 6e-07 | 29/34 (SW1417, HT-29, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.80×** | +5.0 | 2e-05 | 23/34 (HT-29, LS 180, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **2.11×** | +4.5 | 2e-04 | 20/34 (NCI-H460, A498, …) | all doses, stronger at high dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.99×** | +4.2 | 8e-04 | 16/34 (NCI-H2347, J82, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Osimertinib (mesylate) (drug)]] 5 µM |  | **1.95×** | +4.0 | 0.001 | 24/34 (SW1417, BT-474, …) | top dose only |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.96×** | +3.9 | 0.002 | 17/34 (MIA PaCa-2, RPMI-7951, …) | top dose only | cell-cycle shift (explains ~22% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, none with an alert. 5 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 8766.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tirabrutinib (hydrochloride) (drug)]] 0.5 µM |  | **0.522×** | -3.9 | 0.028 | 20/34 (NCI-H2030, SW 900, …) | inconsistent across doses |  |
| [[Auranofin (drug)]] 5 µM |  | **0.523×** | -3.9 | 0.028 | 20/34 (KATO III, NCI-H2347, …) | top dose only |  |
| [[Ponatinib (drug)]] 5 µM |  | **0.540×** | -3.7 | 0.031 | 20/34 (A549, SW480, …) | rises with dose |  |
| [[Dexamethasone (drug)]] 0.5 µM |  | **0.542×** | -3.7 | 0.031 | 20/34 (A549, A498, …) | inconsistent across doses | position effect removed |
| [[Ipatasertib (drug)]] 5 µM |  | **0.314×** | -3.6 | 0.031 | 22/34 (A549, KATO III, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Clobetasol propionate (drug)]] 0.5 µM |  | 0.599× | -3.1 | 0.19 | 15/34 (A498, hTERT-HPNE, …) | rises with dose |  |
| [[Clobetasol propionate (drug)]] 5 µM |  | 0.603× | -3.0 | 0.19 | 15/34 (A498, SW 1271, …) | rises with dose |  |
| [[Entecavir (monohydrate) (drug)]] 5 µM |  | 0.594× | -3.0 | 0.19 | 12/34 (NCI-H2030, NCI-H460, …) | top dose only | plate-row cell shift |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.33 per unit of S-phase module lfc, +0.54 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8766. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 32.5 | 12 (6 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 18.6× (z +15.5) | — |
| [[A-172 (line)]] | wt | 12.2 | 6 | 0 | [[Homoharringtonine (drug)]] 5 µM 151× (z +21.7) | — |
| [[LoVo (line)]] | wt | 64.4 | 3 | 3 (1 ⚠) | [[Harringtonine (drug)]] 5 µM 10.4× (z +12.4) | [[Belinostat (drug)]] 5 µM 0.141× (z -10.7) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.158× (z -10.1) |
| [[SW 900 (line)]] | alt | 50.8 | 6 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 35.2× (z +17.1) | — |
| [[HEC-1-A (line)]] | alt | 19.5 | 5 | 0 | [[Homoharringtonine (drug)]] 5 µM 110× (z +23.5) | — |
| [[MIA PaCa-2 (line)]] | alt | 36.1 | 5 | 0 | [[Homoharringtonine (drug)]] 5 µM 14.2× (z +15.1) | — |
| [[NCI-H1792 (line)]] | alt | 72.8 | 5 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 12.0× (z +14.6) | — |
| [[NCI-H2347 (line)]] | alt | 74.4 | 5 | 0 | [[Homoharringtonine (drug)]] 5 µM 67.4× (z +24.0) | — |
| [[A498 (line)]] | wt | 115 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 42.1× (z +18.2) | — |
| [[A549 (line)]] | wt | 77.9 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 12.2× (z +15.7) | — |
| [[HOP62 (line)]] | alt | 48.1 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 38.9× (z +18.2) | — |
| [[HS-578T (line)]] | alt | 95.5 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 22.0× (z +15.0) | — |
| [[J82 (line)]] | alt | 52.1 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 58.4× (z +20.6) | — |
| [[KATO III (line)]] | alt | 61.9 | 0 | 4 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.114× (z -14.0) |
| [[Panc 03.27 (line)]] | alt | 29.1 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 78.6× (z +23.5) | — |
| [[BT-474 (line)]] | alt | 18.6 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 162× (z +21.5) | — |
| [[CFPAC-1 (line)]] | alt | 108 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 29.5× (z +22.4) | — |
| [[hTERT-HPNE (line)]] | wt | 89.6 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 201× (z +20.1) | — |
| [[LS 180 (line)]] | wt | 57.9 | 1 | 2 | [[Harringtonine (drug)]] 5 µM 11.9× (z +12.5) | [[Panobinostat (drug)]] 5 µM 0.166× (z -9.4) |
| [[NCI-H1573 (line)]] | alt | 50.9 | 1 | 2 (1 ⚠) | [[Harringtonine (drug)]] 5 µM 9.72× (z +9.1) | [[Panobinostat (drug)]] 5 µM 0.132× (z -8.5) |
| [[NCI-H2030 (line)]] | alt | 37.5 | 3 | 0 | [[Harringtonine (drug)]] 5 µM 62.0× (z +14.8) | — |
| [[NCI-H2122 (line)]] | alt | 32.4 | 3 (1 ⚠) | 0 | [[Raltitrexed (drug)]] 5 µM 4.84× (z +13.6) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Fusidic acid (drug)]] 0.05 µM 3.10× (z +11.6) | — |
| [[SNU-423 (line)]] | alt | 18.7 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 65.8× (z +17.1) | — |
| [[SW1417 (line)]] | alt | 42.3 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 15.7× (z +16.9) | — |
| [[SW48 (line)]] | wt | 27.7 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 23.3× (z +12.7) | — |
| [[AsPC-1 (line)]] | alt | 37.0 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 40.9× (z +22.7) | — |
| [[H4 (line)]] | wt | 28.4 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 18.3× (z +10.7) | — |
| [[HT-29 (line)]] | alt | 23.2 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 18.5× (z +15.1) | — |
| [[LOX-IMVI (line)]] | wt | 20.5 | 2 | 0 | [[Harringtonine (drug)]] 5 µM 17.8× (z +10.3) | — |
| [[RPMI-7951 (line)]] | alt | 25.7 | 2 | 0 | [[Harringtonine (drug)]] 5 µM 91.0× (z +12.1) | — |
| [[SW480 (line)]] | alt | 10.7 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.93× (z +10.4) | [[Belinostat (drug)]] 5 µM 0.102× (z -10.5) ⚠ cell-cycle shift, explains ~0% of this change |
| [[Hs 766T (line)]] | wt | 13.4 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 10.6× (z +10.2) | — |
| [[SW 1088 (line)]] | alt | 77.7 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 36.7× (z +11.5) | — |
| [[SW 1271 (line)]] | alt | 20.5 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 55.7× (z +9.1) | — |
| [[A-427 (line)]] | wt | 3.58 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 6.14 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 3.16 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 7.54 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 6.81 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 13.4 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 3.74 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 4.77 n.m. | — | — | — | — |
| [[NCI-H23 (line)]] | alt | 5.57 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 44.1 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 8.55 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 7.45 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 6.10 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 5.81 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 2.65 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 3.23 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8766), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*91 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CXCL2]] | +0.87 | +0.85 / +0.87 | both halves | 7e-06 | same gene group; pathway: HALLMARK_TNFA_SIGNALING_VIA_NFKB; STRING 995 |
| [[CXCL1]] | +0.77 | +0.75 / +0.77 | both halves | 7e-06 | same gene group; pathway: HALLMARK_IL6_JAK_STAT3_SIGNALING; STRING 996 |
| [[TNFAIP2]] | +0.72 | +0.75 / +0.68 | both halves | 7e-06 | pathway: HALLMARK_TNFA_SIGNALING_VIA_NFKB |
| [[LINC02605]] | +0.70 | +0.68 / +0.66 | both halves | 7e-06 |  |
| [[NFKB1]] | +0.66 | +0.60 / +0.53 | both halves | 1e-05 | pathway: HALLMARK_TNFA_SIGNALING_VIA_NFKB; STRING 942 |
| [[DRAM1]] | +0.66 | +0.63 / +0.55 | both halves | 1e-05 | pathway: HALLMARK_TNFA_SIGNALING_VIA_NFKB |
| [[HCP5]] | +0.65 | +0.53 / +0.63 | both halves | 1e-05 |  |
| [[CLN5]] | +0.65 | +0.64 / +0.58 | both halves | 8e-06 |  |
| [[NFKBIA]] | +0.65 | +0.66 / +0.66 | both halves | 7e-06 | pathway: HALLMARK_TNFA_SIGNALING_VIA_NFKB; STRING 470 |
| [[STAT5A]] | +0.64 | +0.72 / +0.47 | both halves | 2e-05 | pathway: HALLMARK_TNFA_SIGNALING_VIA_NFKB |
| [[PATL2]] | +0.62 | +0.63 / +0.50 | both halves | 1e-05 |  |
| [[IRF1]] | +0.62 | +0.67 / +0.56 | both halves | 1e-05 | pathway: HALLMARK_IL6_JAK_STAT3_SIGNALING |

## Genes that move opposite

*9 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[AP1M1]] | -0.60 | -0.63 / -0.49 | both halves | 1e-05 |  |
| [[PCMT1]] | -0.55 | -0.61 / -0.32 | both halves | 2e-04 |  |
| [[SLC25A42]] | -0.52 | -0.32 / -0.36 | both halves | 2e-04 |  |
| [[AP2A1]] | -0.52 | -0.51 / -0.43 | both halves | 3e-05 |  |
| [[TCF3]] | -0.52 | -0.58 / -0.32 | both halves | 2e-04 |  |
| [[TPD52L2]] | -0.51 | -0.50 / -0.47 | both halves | 2e-05 |  |
| [[DIP2A]] | -0.51 | -0.61 / -0.38 | both halves | 7e-05 |  |
| [[DCUN1D2]] | -0.51 | -0.48 / -0.47 | both halves | 2e-05 |  |
| [[DPP9]] | -0.51 | -0.41 / -0.49 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*20 arrows, 20 of them with an alert ⚠; grade A 0, B 15, C 5. Shown: the 12 strongest; 8 more arrows (8 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CSF3]] | B | CSF3 activity raises CXCL3's level | lines that do not express CSF3 (27) vs lines expressing it (23) | 3.09× lower at baseline in the lines without CSF3 | 0.001 | ⚠ within organs, on part of the lines; also absent: CCBE1, LOX, RRAD |
| [[IL6]] | B | IL6 activity raises CXCL3's level | lines that do not express IL6 (32) vs lines expressing it (18) | 3.48× lower at baseline in the lines without IL6 | 0.006 | ⚠ within organs, on part of the lines; also absent: ENSG00000232949, STEAP1B-AS1, G0S2 |
| [[IL1A]] | B | IL1A activity raises CXCL3's level | lines that do not express IL1A (27) vs lines expressing it (23) | 2.68× lower at baseline in the lines without IL1A | 0.007 | ⚠ within organs, on part of the lines; also absent: EDNRA, ABI3BP, PLAT |
| [[TOP2A]] | B | TOP2A activity lowers CXCL3's level | compounds that target TOP2A: 5 of 5 raise it (Amsacrine, Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 100% of the class's compounds vs 6.4% of all compounds | 0.008 | ⚠ off-target possible; 5 compounds; artifact flags |
| [[CSF2]] | B | CSF2 activity raises CXCL3's level | lines that do not express CSF2 (26) vs lines expressing it (24) | 3.05× lower at baseline in the lines without CSF2 | 0.008 | ⚠ within organs, on part of the lines; co-occurs with ARID1A; also absent: IL6, CCBE1, G0S2 |
| [[G0S2]] | B | G0S2 activity raises CXCL3's level | lines that do not express G0S2 (33) vs lines expressing it (17) | 3.37× lower at baseline in the lines without G0S2 | 0.012 | ⚠ within organs, on part of the lines; also absent: IL6, EDNRA, RRAD |
| [[CXCL1]] | B | CXCL1 activity raises CXCL3's level | lines that do not express CXCL1 (17) vs lines expressing it (33) | 2.95× lower at baseline in the lines without CXCL1 | 0.014 | ⚠ within organs, on part of the lines; also absent: CCL20, CDCP1, C15orf48 |
| [[CTSS]] | B | CTSS activity raises CXCL3's level | lines that do not express CTSS (15) vs lines expressing it (35) | 3.01× lower at baseline in the lines without CTSS | 0.016 | ⚠ within organs, on part of the lines; also absent: LINC02257, NMRAL2P-1, CSF2; maybe low, not absent |
| [[RRAD]] | B | RRAD activity raises CXCL3's level | lines that do not express RRAD (31) vs lines expressing it (19) | 2.50× lower at baseline in the lines without RRAD | 0.016 | ⚠ within organs, on part of the lines; also absent: LOX, IL6, EDNRA |
| [[SERPINB7]] | B | SERPINB7 activity raises CXCL3's level | lines that do not express SERPINB7 (24) vs lines expressing it (26) | 2.61× lower at baseline in the lines without SERPINB7 | 0.026 | ⚠ within organs, on part of the lines; also absent: BASP1, DNAH11, SLC16A7 |
| [[CXCL5]] | B | CXCL5 activity raises CXCL3's level | lines that do not express CXCL5 (35) vs lines expressing it (15) | 2.39× lower at baseline in the lines without CXCL5 | 0.027 | ⚠ within organs, on part of the lines; also absent: ANXA10, IRAK3, TRBC2 |
| [[KMO]] | B | KMO activity raises CXCL3's level | lines that do not express KMO (18) vs lines expressing it (32) | 2.56× lower at baseline in the lines without KMO | 0.030 | ⚠ within organs, on part of the lines; co-occurs with ARID1A; also absent: SRPX2, IL1R1, TRIM6; maybe low, not absent |

### Downstream of this gene

*47 arrows, 47 of them with an alert ⚠; grade A 0, B 42, C 5. Shown: the 12 strongest; 35 more arrows (35 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CXCL1]] | B | CXCL3 activity raises CXCL1's level | lines that do not express CXCL3 (14) vs lines expressing it (36) | 3.23× lower at baseline in the lines without CXCL3 | 3e-04 | ⚠ within organs, on part of the lines; also absent: MGLL, SPTLC3, PCED1B |
| [[TNIP1]] | B | CXCL3 activity raises TNIP1's level | lines that do not express CXCL3 (14) vs lines expressing it (36) | 1.89× lower at baseline in the lines without CXCL3 | 0.001 | ⚠ within organs, on part of the lines; also absent: MGLL, SPTLC3, PCED1B |
| [[IL1A]] | B | CXCL3 activity raises IL1A's level | lines that do not express CXCL3 (14) vs lines expressing it (36) | 3.54× lower at baseline in the lines without CXCL3 | 0.001 | ⚠ within organs, on part of the lines; also absent: MGLL, SPTLC3, PCED1B |
| [[ICAM1]] | B | CXCL3 activity strengthens ICAM1's drug response | lines that do not express CXCL3 (10) vs lines expressing it (20) | the lines without CXCL3 respond 0.55× as strongly (z diff +2.45); strongest at Homoharringtonine 5 µM: 1.03x vs 4.05x (z diff +8.5) | 0.002 | ⚠ within organs, on part of the lines; also absent: MGLL, SPTLC3, PCED1B; target measured in part of the lines; artifact flags |
| [[AP1M1]] | B | CXCL3 activity strengthens AP1M1's drug response | lines that do not express CXCL3 (14) vs lines expressing it (33) | the lines without CXCL3 respond 0.41× as strongly (z diff +1.87); strongest at Homoharringtonine 5 µM: 0.85x vs 0.47x (z diff +3.8) | 0.010 | ⚠ within organs, on part of the lines; also absent: MGLL, SPTLC3, PCED1B; target measured in part of the lines; artifact flags |
| [[BCL3]] | B | CXCL3 activity raises BCL3's level | lines that do not express CXCL3 (14) vs lines expressing it (36) | 1.95× lower at baseline in the lines without CXCL3 | 0.010 | ⚠ within organs, on part of the lines; also absent: MGLL, SPTLC3, PCED1B |
| [[LINC02068]] | B | CXCL3 activity raises LINC02068's level | lines that do not express CXCL3 (14) vs lines expressing it (36) | 1.70× lower at baseline in the lines without CXCL3 | 0.015 | ⚠ within organs, on part of the lines; also absent: MGLL, SPTLC3, PCED1B |
| [[CTSS]] | B | CXCL3 activity raises CTSS's level | lines that do not express CXCL3 (14) vs lines expressing it (36) | 2.91× lower at baseline in the lines without CXCL3 | 0.015 | ⚠ within organs, on part of the lines; also absent: MGLL, SPTLC3, PCED1B |
| [[SERPINB7]] | B | CXCL3 activity raises SERPINB7's level | lines that do not express CXCL3 (14) vs lines expressing it (36) | 2.66× lower at baseline in the lines without CXCL3 | 0.016 | ⚠ within organs, on part of the lines; also absent: MGLL, SPTLC3, PCED1B |
| [[IRF1]] | B | CXCL3 activity raises IRF1's level | lines that do not express CXCL3 (14) vs lines expressing it (36) | 1.86× lower at baseline in the lines without CXCL3 | 0.016 | ⚠ within organs, on part of the lines; also absent: MGLL, SPTLC3, PCED1B |
| [[CSF2]] | B | CXCL3 activity raises CSF2's level | lines that do not express CXCL3 (14) vs lines expressing it (36) | 2.73× lower at baseline in the lines without CXCL3 | 0.018 | ⚠ within organs, on part of the lines; also absent: MGLL, SPTLC3, PCED1B |
| [[TNFAIP3]] | B | CXCL3 activity raises TNFAIP3's level | lines that do not express CXCL3 (14) vs lines expressing it (36) | 2.24× lower at baseline in the lines without CXCL3 | 0.018 | ⚠ within organs, on part of the lines; also absent: MGLL, SPTLC3, PCED1B |

## Where it sits

- **Module**: [[Module 014]] — TNF-alpha signaling via NF-kB; 212 genes; every member is in the + arm (projection on the module's main direction 0.729). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.20; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (26.0, 5.7); signed map (41.9, 7.6). **Vector** length 117, 39.0% of its response variance represented; |z| ≥ 3 in 1,055 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *Interleukin-10 signaling* (reactome, mean cos +0.55 to 9); *IkBA variant leads to EDA-ID* (reactome, mean cos +0.51 to 4); *Toll Like Receptor 3 (TLR3) Cascade* (reactome, mean cos +0.50 to 10).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Selinexor (drug)]] 5 µM |  | +10.2 | +10.4 |
|  | [[Selinexor (drug)]] 0.5 µM |  | +7.0 | +8.3 |
|  | [[Harringtonine (drug)]] 5 µM |  | +6.9 | +21.2 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +6.3 | +26.6 |
|  | [[Selinexor (drug)]] 0.05 µM |  | +4.9 | +5.6 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +4.7 | +5.0 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +3.5 | +1.5 |
|  | [[Binimetinib (drug)]] 5 µM |  | +3.4 | +2.2 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +2.9 | +1.6 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +2.8 | +4.5 |
| fall | [[Auranofin (drug)]] 5 µM |  | -7.5 | -3.9 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | -4.9 | -1.2 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -4.5 | -0.1 |
|  | [[Panobinostat (drug)]] 5 µM |  | -4.3 | -2.4 |
|  | [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift | -3.9 | -2.3 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -2.6 | -3.7 |
|  | [[Tofacitinib (drug)]] 0.5 µM |  | -2.3 | -1.0 |
|  | [[Tofacitinib (drug)]] 5 µM |  | -2.2 | -1.8 |
|  | [[Ipatasertib (drug)]] 5 µM |  | -2.0 | -3.6 |

## What is on record

|  |  |
|---|---|
| Name | C-X-C motif chemokine ligand 3 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 4q13.3 — chr4:74,036,589-74,038,807 (-) |
| Ensembl biotype | protein_coding |
| Also known as | SCYB3, GROg, MIP-2b, CINC-2b; previously GRO3 |
| Gene groups (HGNC) | Chemokine ligands |
| Hallmark sets | IL6_JAK_STAT3_SIGNALING, TNFA_SIGNALING_VIA_NFKB |
| Reactome | 7 pathways, smallest: Chemokine receptors bind chemokines; Peptide ligand-binding receptors; Class A/1 (Rhodopsin-like receptors) |
| Matched by | ensembl_id |

**Function**, from UniProt [P19876](https://www.uniprot.org/uniprotkb/P19876) (C-X-C motif chemokine 3):

> Ligand for CXCR2 (By similarity). Has chemotactic activity for neutrophils. May play a role in inflammation and exert its effects on endothelial cells in an autocrine fashion. In vitro, the processed form GRO-gamma(5-73) shows a fivefold higher chemotactic activity for neutrophilic granulocytes.

**Summary**, from NCBI Gene [2921](https://www.ncbi.nlm.nih.gov/gene/2921):

> This antimicrobial gene encodes a member of the CXC subfamily of chemokines. The encoded protein is a secreted growth factor that signals through the G-protein coupled receptor, CXC receptor 2. This protein plays a role in inflammation and as a chemoattractant for neutrophils. [provided by RefSeq, Sep 2014]

**Accessions** — [HGNC:4604](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:4604) · Entrez [2921](https://www.ncbi.nlm.nih.gov/gene/2921) · UniProt [P19876](https://www.uniprot.org/uniprotkb/P19876) · Ensembl [ENSG00000163734](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000163734)

## Data

Gene col 8766: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8766); `tables/drug_effects.parquet` (43 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8766, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8766]; `tensor/DDL_lfc|DDL_z.npy` [8766]; `embed/gene_vectors.npy` [8766]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8766 or target_col == 8766). Every well: [[CXCL3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CXCL3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
