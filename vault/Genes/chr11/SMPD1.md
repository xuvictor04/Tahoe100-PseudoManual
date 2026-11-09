---
symbol: "SMPD1"
type: "gene"
col: 9280
ensembl_id: "ENSG00000166311"
name: "sphingomyelin phosphodiesterase 1"
location: "11p15.4"
module: 50
arm: "+"
pooled_cpm: 6.86
n_lines_expressing: 48
n_dd_up: 20
n_dd_down: 3
n_dd_up_clean: 10
n_dd_down_clean: 3
in_vector_space: true
direction_upstream: 8
direction_downstream: 1
tags: ["gene", "module/050"]
generated_by: "tahoemap"
---

# SMPD1

*sphingomyelin phosphodiesterase 1* — 11p15.4

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 20 drug-doses (10 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 2.29× (z +10.7, q 9e-24, up in 27 of 38 measured lines).
> Pooled over the cell lines (median), lowered significantly by 3 drug-doses (none with an alert); the strongest is [[Ixazomib citrate (drug)]] 5 µM: 0.567× (z -5.2, q 1e-04, down in 22 of 44 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[RTL8C]] (+0.58, fdr 1e-04), [[ATP6AP1]] (+0.57, fdr 1e-05), [[COL1A1]] (+0.57, fdr 3e-05); moves opposite to [[GSTO2]] (-0.52, fdr 3e-04), [[DKC1]] (-0.51, fdr 2e-05), [[CENPV]] (-0.48, fdr 4e-05).
> It is in [[Module 050]], a single-armed module (Extracellular matrix organization).
> Probable direction (from the cell lines, not proof of direct regulation): 8 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); 1 goes from it, the strongest it → cells under [[ERK5-IN-2 (drug)]] 0.5 µM (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 21 in all, 11 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 20 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 10 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9280.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **2.29×** | +10.7 | 9e-24 | 27/38 (LoVo, AsPC-1, …) | rises with dose | cell-cycle shift (explains ~4% here); composition shift; position effect removed |
| [[Panobinostat (drug)]] 0.5 µM |  | **3.20×** | +10.6 | 1e-23 | 41/46 (PANC-1, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **3.14×** | +10.4 | 4e-23 | 37/46 (PANC-1, MIA PaCa-2, …) | all doses, stronger at high dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.22×** | +10.3 | 1e-22 | 30/37 (SW480, LS 180, …) | rises with dose | cell-cycle shift (explains ~15% here); position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | **2.90×** | +9.3 | 2e-18 | 10/13 (HOP62, SNU-423, …) | all doses, stronger at high dose | composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change | **2.65×** | +8.9 | 7e-17 | 18/27 (HOP62, C32, …) | all doses, stronger at high dose | composition shift; position effect removed |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **2.43×** | +8.1 | 6e-14 | 34/45 (PANC-1, A549, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | **2.27×** | +6.8 | 7e-10 | 9/17 (NCI-H2030, HS-578T, …) | all doses, stronger at high dose | composition shift; position effect removed |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **2.05×** | +6.3 | 2e-08 | 26/37 (A498, PANC-1, …) | top dose only |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.62×** | +6.2 | 4e-08 | 24/45 (MIA PaCa-2, NCI-H2347, …) | top dose only |  |
| [[Harringtonine (drug)]] 5 µM |  | **1.89×** | +5.6 | 1e-06 | 21/45 (MIA PaCa-2, COLO 205, …) | top dose only | cell-cycle shift (explains ~11% here); composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~25% of this change | **1.86×** | +5.4 | 3e-06 | 18/29 (NCI-H2030, HT-29, …) | inconsistent across doses |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.72×** | +4.9 | 4e-05 | 15/27 (SW1417, HOP62, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~13% here); position effect removed |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.68×** | +4.7 | 1e-04 | 19/46 (PANC-1, SK-MEL-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **1.70×** | +4.6 | 1e-04 | 18/35 (SW480, NCI-H2030, …) | top dose only | position effect removed |
| [[Belinostat (drug)]] 0.5 µM |  | **1.63×** | +4.4 | 3e-04 | 18/36 (PANC-1, SK-MEL-2, …) | rises with dose | cell-cycle shift (explains ~18% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.71×** | +3.9 | 0.004 | 13/36 (LoVo, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here); noisy plate (z scaled); position effect removed |
| [[Selinexor (drug)]] 5 µM |  | **1.34×** | +3.7 | 0.007 | 15/45 (J82, SW480, …) | top dose only | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.85×** | +3.4 | 0.018 | 4/32 (A-172, LS 180, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled); position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, none with an alert. 3 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 9280.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.567×** | -5.2 | 1e-04 | 22/44 (HT-29, A498, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Verteporfin (drug)]] 5 µM |  | **0.608×** | -4.4 | 0.003 | 19/39 (NCI-H2030, hTERT-HPNE, …) | top dose only | position effect removed |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.615×** | -4.2 | 0.004 | 21/41 (HS-578T, MIA PaCa-2, …) | inconsistent across doses | cell-cycle shift (explains ~14% here); position effect removed |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | 0.709× | -3.2 | 0.21 | 16/42 (MIA PaCa-2, J82, …) | rises with dose |  |
| [[Digitoxin (drug)]] 0.05 µM |  | 0.714× | -3.1 | 0.21 | 14/42 (SNU-1, RKO, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.51 per unit of S-phase module lfc, -0.03 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9280. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 5.03 | 3 (2 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 8.37× (z +10.2) ⚠ cell-cycle shift, explains ~27% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 7.22× (z +9.5) | — |
| [[SK-MEL-2 (line)]] | alt | 5.53 | 0 | 2 (1 ⚠) | — | [[Sunitinib (drug)]] 5 µM 0.0592× (z -9.7) ⚠ toxic · without an alert: [[Verteporfin (drug)]] 5 µM 0.0708× (z -8.7) |
| [[SW480 (line)]] | alt | 4.08 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.17× (z +8.8) | — |
| [[AsPC-1 (line)]] | alt | 3.09 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 11.3× (z +9.1) | — |
| [[COLO 205 (line)]] | alt | 2.97 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 15.1× (z +8.6) | — |
| [[HT-29 (line)]] | alt | 4.33 | 0 | 1 | — | [[Ixazomib citrate (drug)]] 5 µM 0.0465× (z -10.3) |
| [[hTERT-HPNE (line)]] | wt | 23.4 | 0 | 1 | — | [[Verteporfin (drug)]] 5 µM 0.132× (z -10.0) |
| [[LoVo (line)]] | wt | 2.17 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 10.7× (z +10.2) | — |
| [[NCI-H2030 (line)]] | alt | 15.7 | 0 | 1 | — | [[Verteporfin (drug)]] 5 µM 0.122× (z -11.6) |
| [[SNU-423 (line)]] | alt | 18.8 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.14× (z +8.5) | — |
| [[A-172 (line)]] | wt | 43.5 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 5.39 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 13.7 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 2.68 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 5.53 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 3.30 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 1.79 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 10.3 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 2.82 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 2.48 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 12.7 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 5.50 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 3.29 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 3.10 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 8.69 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 5.04 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 15.2 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 9.09 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 2.15 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 5.67 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 2.96 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 2.38 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 1.61 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 4.29 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 5.85 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 1.53 n.m. | — | — | — | — |
| [[NCI-H2347 (line)]] | alt | 4.01 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 3.67 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 5.59 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 7.30 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 2.36 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 2.98 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 12.5 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 1.96 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 5.03 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 17.5 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 9.46 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 3.33 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 5.77 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 3.07 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9280), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*78 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RTL8C]] | +0.58 | +0.34 / +0.66 | both halves | 1e-04 |  |
| [[ATP6AP1]] | +0.57 | +0.54 / +0.53 | both halves | 1e-05 |  |
| [[COL1A1]] | +0.57 | +0.49 / +0.45 | both halves | 3e-05 |  |
| [[CTSA]] | +0.55 | +0.48 / +0.43 | both halves | 3e-05 | pathway: Glycosphingolipid catabolism |
| [[LRPAP1]] | +0.55 | +0.51 / +0.48 | both halves | 2e-05 |  |
| [[SPARC]] | +0.55 | +0.41 / +0.51 | both halves | 4e-05 |  |
| [[APLP1]] | +0.55 | +0.43 / +0.59 | both halves | 3e-05 |  |
| [[BACE1]] | +0.54 | +0.56 / +0.51 | both halves | 1e-05 |  |
| [[COL1A2]] | +0.53 | +0.45 / +0.45 | both halves | 3e-05 |  |
| [[EMC7]] | +0.50 | +0.48 / +0.49 | both halves | 2e-05 |  |
| [[PRAF2]] | +0.50 | +0.38 / +0.51 | both halves | 7e-05 |  |
| [[HLA-A]] | +0.50 | +0.59 / +0.39 | both halves | 5e-05 |  |

## Genes that move opposite

*22 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GSTO2]] | -0.52 | -0.29 / -0.41 | both halves | 3e-04 |  |
| [[DKC1]] | -0.51 | -0.48 / -0.52 | both halves | 2e-05 |  |
| [[CENPV]] | -0.48 | -0.43 / -0.41 | both halves | 4e-05 |  |
| [[CACYBP]] | -0.48 | -0.50 / -0.43 | both halves | 3e-05 |  |
| [[HSPD1]] | -0.47 | -0.44 / -0.44 | both halves | 3e-05 |  |
| [[HSPE1]] | -0.47 | -0.43 / -0.43 | both halves | 3e-05 |  |
| [[PNN]] | -0.45 | -0.29 / -0.44 | both halves | 2e-04 |  |
| [[CCT6A]] | -0.45 | -0.34 / -0.43 | both halves | 1e-04 |  |
| [[EEF1E1]] | -0.44 | -0.49 / -0.33 | both halves | 1e-04 |  |
| [[SFXN4]] | -0.43 | -0.45 / -0.33 | both halves | 1e-04 |  |
| [[CCT4]] | -0.43 | -0.35 / -0.39 | both halves | 1e-04 |  |
| [[DFFA]] | -0.43 | -0.36 / -0.39 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*8 arrows, 8 of them with an alert ⚠; grade A 0, B 8, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers SMPD1's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 3.9% of all compounds | 0.020 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[FBN1]] | B | FBN1 activity raises SMPD1's level | lines that do not express FBN1 (28) vs lines expressing it (22) | 1.98× lower at baseline in the lines without FBN1 | 0.020 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: GYPC, TENM2, ENSG00000280241 |
| [[SPARC]] | B | SPARC activity raises SMPD1's level | lines that do not express SPARC (34) vs lines expressing it (16) | 2.47× lower at baseline in the lines without SPARC | 0.024 | ⚠ within organs, on part of the lines; co-occurs with KRAS, TP53; also absent: ITGA4, MMP2, ENSG00000222032 |
| [[PSMB5]] | B | PSMB5 activity raises SMPD1's level | compounds that target PSMB5: 2 of 2 lower it (Bortezomib, Ixazomib / Ixazomib citrate) | 100% of the class's compounds vs 0.8% of all compounds | 0.044 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[COL1A2]] | B | COL1A2 activity raises SMPD1's level | lines that do not express COL1A2 (37) vs lines expressing it (13) | 2.34× lower at baseline in the lines without COL1A2 | 0.047 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: PKD1L1-AS1, FCRLA, PSG5 |
| [[MMP2]] | B | MMP2 activity raises SMPD1's level | lines that do not express MMP2 (34) vs lines expressing it (16) | 2.19× lower at baseline in the lines without MMP2 | 0.078 | ⚠ within organs, on part of the lines; co-occurs with KRAS, TP53; also absent: ITGA4, SPARC, APCDD1L |
| [[COL3A1]] | B | COL3A1 activity raises SMPD1's level | lines that do not express COL3A1 (35) vs lines expressing it (15) | 1.80× lower at baseline in the lines without COL3A1 | 0.088 | ⚠ within organs, on part of the lines; co-occurs with KRAS, TP53; also absent: THY1, PDGFRB, ZNF677 |
| [[APLP1]] | B | APLP1 activity raises SMPD1's level | lines that do not express APLP1 (12) vs lines expressing it (38) | 1.55× lower at baseline in the lines without APLP1 | 0.097 | ⚠ within organs, on part of the lines; also absent: ENSG00000291283, CTXN1, SUSD4; maybe low, not absent |

### Downstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| cells under [[ERK5-IN-2 (drug)]] 0.5 µM | C | SMPD1's natural level lowers the cells' numbers under ERK5-IN-2 0.5 µM (makes them more sensitive) | SMPD1's natural level across 46 lines (lineage-adjusted; a glimpse) | r -0.58 | 0.517 over the table, 0.099 within its drug-dose | ⚠ within its drug-dose only (a lead); tissue can mimic it |

## Where it sits

- **Module**: [[Module 050]] — Extracellular matrix organization; 92 genes; every member is in the + arm (projection on the module's main direction 0.395). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.27; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (24.5, -39.8); signed map (-27.1, -37.2). **Vector** length 67.5, 12.3% of its response variance represented; |z| ≥ 3 in 919 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM |  | +3.6 | +10.7 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | +2.4 | +9.3 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change | +2.4 | +8.9 |
|  | [[Idarubicin (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift | +2.3 | +2.8 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +2.3 | +2.4 |
|  | [[Bimiralisib (drug)]] 0.5 µM |  | +1.8 | +2.5 |
|  | [[Binimetinib (drug)]] 5 µM |  | +1.8 | +2.6 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +1.7 | +6.2 |
|  | [[9-ING-41 (drug)]] 0.5 µM |  | +1.7 | +2.7 |
| fall | [[Ixazomib citrate (drug)]] 5 µM |  | -3.7 | -5.2 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | -3.5 | -4.2 |
|  | [[Auranofin (drug)]] 5 µM |  | -2.8 | -1.0 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -2.7 | -3.2 |
|  | [[Verteporfin (drug)]] 5 µM |  | -2.3 | -4.4 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | -1.7 | -1.5 |
|  | [[Glycyrrhizic acid (drug)]] 0.5 µM |  | -1.7 | -1.8 |

## What is on record

|  |  |
|---|---|
| Name | sphingomyelin phosphodiesterase 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 11p15.4 — chr11:6,390,440-6,394,998 (+) |
| Ensembl biotype | protein_coding |
| Also known as | ASM |
| Gene groups (HGNC) | Saposin B type domain containing |
| Reactome | 7 pathways, smallest: Glycosphingolipid catabolism; Regulation of clotting cascade; Coagulation pathway |
| Matched by | ensembl_id |

**Function**, from UniProt [P17405](https://www.uniprot.org/uniprotkb/P17405) (Sphingomyelin phosphodiesterase):

> Converts sphingomyelin to ceramide. Exists as two enzymatic forms that arise from alternative trafficking of a single protein precursor, one that is targeted to the endolysosomal compartment, whereas the other is released extracellularly. However, in response to various forms of stress, lysosomal exocytosis may represent a major source of the secretory form.; In the lysosomes, converts sphingomyelin to ceramide. Plays an important role in the export of cholesterol from the intraendolysosomal …

**Summary**, from NCBI Gene [6609](https://www.ncbi.nlm.nih.gov/gene/6609):

> The protein encoded by this gene is a lysosomal acid sphingomyelinase that converts sphingomyelin to ceramide. The encoded protein also has phospholipase C activity. Defects in this gene are a cause of Niemann-Pick disease type A (NPA) and Niemann-Pick disease type B (NPB). Multiple transcript variants encoding different isoforms have been identified. [provided by RefSeq, Jul 2010]

**Accessions** — [HGNC:11120](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:11120) · Entrez [6609](https://www.ncbi.nlm.nih.gov/gene/6609) · UniProt [P17405](https://www.uniprot.org/uniprotkb/P17405) · Ensembl [ENSG00000166311](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000166311)

## Data

Gene col 9280: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9280); `tables/drug_effects.parquet` (26 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9280, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9280]; `tensor/DDL_lfc|DDL_z.npy` [9280]; `embed/gene_vectors.npy` [9280]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9280 or target_col == 9280). Every well: [[SMPD1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SMPD1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
