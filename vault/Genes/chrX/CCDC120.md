---
symbol: "CCDC120"
type: "gene"
col: 7155
ensembl_id: "ENSG00000147144"
name: "coiled-coil domain containing 120"
location: "Xp11.23"
module: 31
arm: "+"
pooled_cpm: 6.43
n_lines_expressing: 39
n_dd_up: 0
n_dd_down: 10
n_dd_up_clean: 0
n_dd_down_clean: 4
in_vector_space: true
direction_upstream: 22
direction_downstream: 38
tags: ["gene", "module/031"]
generated_by: "tahoemap"
---

# CCDC120

*coiled-coil domain containing 120* — Xp11.23

## At a glance

> [!summary] In this data
> No drug-dose raises it significantly in the pooled (median-over-lines) data.
> Pooled over the cell lines (median), lowered significantly by 10 drug-doses (6 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.491× (z -12.1, q 3e-31, down in 22 of 30 measured lines).
> Its strongest partners by |cos| (95 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 6 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[MYRF]] (+0.57, fdr 1e-05), [[LPIN3]] (+0.53, fdr 3e-05), [[CNKSR1]] (+0.53, fdr 2e-04); moves opposite to [[CENPBD2P]] (-0.44, fdr 2e-04), [[CFAP210]] (-0.43, fdr 7e-05), [[MLLT3]] (-0.41, fdr 2e-04).
> It is in [[Module 031]], a single-armed module (Formation of the cornified envelope).
> Probable direction (from the cell lines, not proof of direct regulation): 22 arrows point to it, the strongest [[CRYBG2]] → it (grade B ⚠); 38 go from it, the strongest it → [[ABL1]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

No drug-dose raises it in the pooled data (pooled over the cell lines, median: none with |z| ≥ 3 or q < 0.10). A response seen in fewer than about half of the measured lines does not reach the pooled data; see [[#In which cell lines]].

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 7 with an alert ⚠. 10 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 7155.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.491×** | -12.1 | 3e-31 | 22/30 (NCI-H23, SW480, …) | rises with dose | cell-cycle shift (explains ~14% here); position effect removed |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~48% of this change | **0.548×** | -7.3 | 1e-10 | 19/36 (PANC-1, NCI-H23, …) | all doses, stronger at high dose |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.592×** | -6.3 | 5e-08 | 18/31 (NCI-H23, LoVo, …) | two highest doses | cell-cycle shift (explains ~2% here) |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~50% of this change | **0.613×** | -5.6 | 3e-06 | 12/35 (SW480, A549, …) | all doses, stronger at high dose |  |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~43% of this change | **0.736×** | -5.2 | 2e-05 | 17/32 (NCI-H1573, CFPAC-1, …) | two highest doses | composition shift |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **0.601×** | -4.9 | 8e-05 | 15/30 (PANC-1, A-427, …) | top dose only | noisy plate (z scaled) |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~67% of this change | **0.673×** | -4.8 | 1e-04 | 14/35 (HOP62, NCI-H23, …) | top dose only |  |
| [[TAK-901 (drug)]] 5 µM |  | **0.553×** | -3.7 | 0.013 | 7/34 (HOP62, PANC-1, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~24% here); composition shift; noisy plate (z scaled) |
| [[Cobimetinib (drug)]] 5 µM |  | **0.704×** | -3.4 | 0.043 | 3/34 (C-33 A, KATO III, …) | top dose only | noisy plate (z scaled); position effect removed |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.756×** | -3.4 | 0.043 | 8/35 (AsPC-1, KATO III, …) | inconsistent across doses |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~52% of this change | 0.730× | -3.0 | 0.12 | 11/31 (PANC-1, KATO III, …) | top dose only | noisy plate (z scaled); position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.43 per unit of S-phase module lfc, -0.10 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7155. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HEC-1-A (line)]] | alt | 18.1 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.177× (z -9.9) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.420× (z -8.8) |
| [[NCI-H2347 (line)]] | alt | 9.73 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.234× (z -9.0) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.376× (z -8.6) |
| [[SW480 (line)]] | alt | 17.8 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.127× (z -12.7) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.367× (z -10.9) |
| [[KATO III (line)]] | alt | 14.2 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.117× (z -11.4) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.316× (z -8.7) |
| [[PANC-1 (line)]] | alt | 5.74 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.303× (z -10.0) |
| [[COLO 205 (line)]] | alt | 7.61 | 0 | 1 | — | [[Fluvoxamine (maleate) (drug)]] 0.5 µM 0.0666× (z -9.3) |
| [[HCT15 (line)]] | alt | 11.3 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.145× (z -10.2) |
| [[HOP62 (line)]] | alt | 2.24 | 0 | 1 | — | [[Diammonium Glycyrrhizinate (drug)]] 0.5 µM 0.0501× (z -10.3) |
| [[J82 (line)]] | alt | 4.04 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.151× (z -10.0) |
| [[NCI-H23 (line)]] | alt | 5.19 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.129× (z -11.2) |
| [[Panc 03.27 (line)]] | alt | 13.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.159× (z -9.8) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[A-172 (line)]] | wt | 0.649 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 6.51 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 2.72 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 4.96 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 1.16 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 6.51 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 11.8 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 5.75 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 1.20 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 12.1 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 5.25 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 0.894 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 5.26 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 3.29 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 0.635 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 8.23 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 0.840 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 6.97 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 0.779 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 8.74 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 2.26 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 8.72 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 2.22 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 3.34 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 6.37 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 1.06 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 6.64 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 4.03 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 0.672 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 6.02 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 3.26 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 4.45 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 0.726 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 3.70 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 3.92 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 0.646 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 3.22 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 16.5 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 4.86 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7155), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*86 of its nearest partners move with it, 4 of them with an alert (⚠; 3 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MYRF]] | +0.57 | +0.57 / +0.53 | both halves | 1e-05 |  |
| [[LPIN3]] | +0.53 | +0.44 / +0.59 | both halves | 3e-05 |  |
| [[CNKSR1]] | +0.53 | +0.31 / +0.61 | both halves | 2e-04 |  |
| [[ARHGEF16]] | +0.47 | +0.40 / +0.51 | both halves | 5e-05 |  |
| [[PCDH1]] | +0.47 | +0.38 / +0.47 | both halves | 6e-05 |  |
| [[SNRNP35]] | +0.46 | +0.47 / +0.45 | both halves | 3e-05 |  |
| [[CACFD1]] | +0.45 | +0.22 / +0.46 | both halves | 6e-04 |  |
| [[KIAA1522]] | +0.44 | +0.35 / +0.46 | both halves | 1e-04 |  |
| [[TRAF4]] | +0.44 | +0.17 / +0.52 | ⚠ one half (not replicated) | 0.001 |  |
| [[TEPSIN]] | +0.44 | +0.33 / +0.42 | both halves | 1e-04 |  |
| [[BAIAP3]] | +0.44 | +0.43 / +0.40 | both halves | 5e-05 |  |
| [[ARHGEF5]] | +0.43 | +0.32 / +0.53 | both halves | 2e-04 |  |
| [[ATG2A]] | +0.43 | +0.46 / +0.38 | both halves | 7e-05 |  |

## Genes that move opposite

*14 of its nearest partners move opposite, 2 of them with an alert (⚠; 2 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CENPBD2P]] | -0.44 | -0.48 / -0.30 | both halves | 2e-04 |  |
| [[CFAP210]] | -0.43 | -0.47 / -0.38 | both halves | 7e-05 |  |
| [[MLLT3]] | -0.41 | -0.29 / -0.45 | both halves | 2e-04 |  |
| [[ABL1]] | -0.40 | -0.19 / -0.45 | ⚠ not reproduced | 8e-04 |  |
| [[SLCO1C1]] | -0.40 | -0.30 / -0.37 | both halves | 2e-04 |  |
| [[TAOK1]] | -0.40 | -0.44 / -0.25 | both halves | 4e-04 |  |
| [[KIF9]] | -0.39 | -0.39 / -0.33 | both halves | 1e-04 |  |
| [[LINC01019]] | -0.39 | -0.32 / -0.39 | both halves | 2e-04 |  |
| [[PRPSAP1]] | -0.39 | -0.37 / -0.35 | both halves | 1e-04 |  |
| [[RRP12]] | -0.37 | -0.24 / -0.42 | both halves | 5e-04 |  |
| [[TDRD3]] | -0.37 | -0.35 / -0.33 | both halves | 1e-04 |  |
| [[USP3-AS1]] | -0.37 | -0.32 / -0.37 | both halves | 2e-04 |  |
| [[SEMA5A]] | -0.36 | -0.23 / -0.41 | both halves | 5e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*22 arrows, 22 of them with an alert ⚠; grade A 0, B 21, C 1. Shown: the 12 strongest; 10 more arrows (10 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CRYBG2]] | B | CRYBG2 activity raises CCDC120's level | lines that do not express CRYBG2 (23) vs lines expressing it (27) | 2.86× lower at baseline in the lines without CRYBG2 | 5e-04 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: SPINT1-AS1, SMPDL3B, LAD1 |
| [[SH2D3A]] | B | SH2D3A activity raises CCDC120's level | lines that do not express SH2D3A (24) vs lines expressing it (26) | 2.67× lower at baseline in the lines without SH2D3A | 0.001 | ⚠ within organs, on part of the lines; also absent: GRB7, MYO5B, CRB3 |
| [[B3GNT3]] | B | B3GNT3 activity raises CCDC120's level | lines that do not express B3GNT3 (31) vs lines expressing it (19) | 2.57× lower at baseline in the lines without B3GNT3 | 0.001 | ⚠ within organs, on part of the lines; also absent: CDH1, INAVA, SLC5A1 |
| [[GOLT1A]] | B | GOLT1A activity raises CCDC120's level | lines that do not express GOLT1A (24) vs lines expressing it (26) | 2.61× lower at baseline in the lines without GOLT1A | 0.001 | ⚠ within organs, on part of the lines; also absent: GRB7, RHOV, ELF3; maybe low, not absent |
| [[CNKSR1]] | B | CNKSR1 activity raises CCDC120's level | lines that do not express CNKSR1 (24) vs lines expressing it (26) | 2.57× lower at baseline in the lines without CNKSR1 | 0.001 | ⚠ within organs, on part of the lines; also absent: SPINT1, SLC52A3, ESRP2 |
| [[GRB7]] | B | GRB7 activity raises CCDC120's level | lines that do not express GRB7 (25) vs lines expressing it (25) | 2.76× lower at baseline in the lines without GRB7 | 0.001 | ⚠ within organs, on part of the lines; also absent: SH2D3A, CRB3, MISP |
| [[JUP]] | B | JUP activity raises CCDC120's level | lines that do not express JUP (16) vs lines expressing it (34) | 2.31× lower at baseline in the lines without JUP | 0.004 | ⚠ within organs, on part of the lines; co-occurs with TERT; also absent: ELF3, SHROOM3, ENSG00000253671 |
| [[ARHGEF5]], [[ARHGEF34P]] | B | ARHGEF5, ARHGEF34P activity raises CCDC120's level | lines that do not express ARHGEF5, ARHGEF34P (19) vs lines expressing them (31) | 2.36× lower at baseline in the lines without ARHGEF5, ARHGEF34P | 0.007 | ⚠ within organs, on part of the lines; also absent: ENSG00000284644, ESRP2, GOLT1A; co-absent genes |
| [[RASAL1]] | B | RASAL1 activity raises CCDC120's level | lines that do not express RASAL1 (25) vs lines expressing it (25) | 2.01× lower at baseline in the lines without RASAL1 | 0.008 | ⚠ within organs, on part of the lines; also absent: CSF2RA, SMPDL3B, SKAP1 |
| [[PTK2B]] | B | PTK2B activity raises CCDC120's level | lines that do not express PTK2B (10) vs lines expressing it (40) | 2.26× lower at baseline in the lines without PTK2B | 0.012 | ⚠ within organs, on part of the lines; maybe low, not absent |
| [[PCDH1]] | B | PCDH1 activity raises CCDC120's level | lines that do not express PCDH1 (20) vs lines expressing it (30) | 1.95× lower at baseline in the lines without PCDH1 | 0.015 | ⚠ within organs, on part of the lines; also absent: ENSG00000286736, ERBB3, TRIM29 |
| [[PDE9A]] | B | PDE9A activity raises CCDC120's level | lines that do not express PDE9A (16) vs lines expressing it (34) | 2.09× lower at baseline in the lines without PDE9A | 0.018 | ⚠ within organs, on part of the lines; also absent: NRARP, FBXO2, ENSG00000267748 |

### Downstream of this gene

*38 arrows, 38 of them with an alert ⚠; grade A 0, B 37, C 1. Shown: the 12 strongest; 26 more arrows (26 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ABL1]] | B | CCDC120 activity lowers ABL1's level | lines that do not express CCDC120 (11) vs lines expressing it (39) | 1.83× higher at baseline in the lines without CCDC120 | 8e-04 | ⚠ within organs, on part of the lines; also absent: PARD6B, LMTK3, AP1G2 |
| [[CNKSR1]] | B | CCDC120 activity raises CNKSR1's level | lines that do not express CCDC120 (11) vs lines expressing it (39) | 3.60× lower at baseline in the lines without CCDC120 | 0.002 | ⚠ within organs, on part of the lines; also absent: PARD6B, LMTK3, AP1G2 |
| [[RPS6KA1]] | B | CCDC120 activity raises RPS6KA1's level | lines that do not express CCDC120 (11) vs lines expressing it (39) | 1.73× lower at baseline in the lines without CCDC120 | 0.003 | ⚠ within organs, on part of the lines; also absent: PARD6B, LMTK3, AP1G2 |
| [[KIAA1522]] | B | CCDC120 activity raises KIAA1522's level | lines that do not express CCDC120 (11) vs lines expressing it (39) | 2.98× lower at baseline in the lines without CCDC120 | 0.003 | ⚠ within organs, on part of the lines; also absent: PARD6B, LMTK3, AP1G2 |
| [[JUP]] | B | CCDC120 activity raises JUP's level | lines that do not express CCDC120 (11) vs lines expressing it (39) | 4.11× lower at baseline in the lines without CCDC120 | 0.011 | ⚠ within organs, on part of the lines; also absent: PARD6B, LMTK3, AP1G2 |
| [[SLCO1C1]] | B | CCDC120 activity lowers SLCO1C1's level | lines that do not express CCDC120 (11) vs lines expressing it (39) | 1.80× higher at baseline in the lines without CCDC120 | 0.013 | ⚠ within organs, on part of the lines; also absent: PARD6B, LMTK3, AP1G2 |
| [[ARHGEF5]] | B | CCDC120 activity raises ARHGEF5's level | lines that do not express CCDC120 (11) vs lines expressing it (39) | 3.05× lower at baseline in the lines without CCDC120 | 0.016 | ⚠ within organs, on part of the lines; also absent: PARD6B, LMTK3, AP1G2 |
| [[SH2D3A]] | B | CCDC120 activity raises SH2D3A's level | lines that do not express CCDC120 (11) vs lines expressing it (39) | 3.96× lower at baseline in the lines without CCDC120 | 0.017 | ⚠ within organs, on part of the lines; also absent: PARD6B, LMTK3, AP1G2 |
| [[GOLT1A]] | B | CCDC120 activity raises GOLT1A's level | lines that do not express CCDC120 (11) vs lines expressing it (39) | 3.21× lower at baseline in the lines without CCDC120 | 0.020 | ⚠ within organs, on part of the lines; also absent: PARD6B, LMTK3, AP1G2 |
| [[KIF9]] | B | CCDC120 activity raises KIF9's level | lines that do not express CCDC120 (11) vs lines expressing it (39) | 1.45× lower at baseline in the lines without CCDC120 | 0.022 | ⚠ within organs, on part of the lines; also absent: PARD6B, LMTK3, AP1G2 |
| [[MYO15B]] | B | CCDC120 activity raises MYO15B's level | lines that do not express CCDC120 (11) vs lines expressing it (39) | 1.91× lower at baseline in the lines without CCDC120 | 0.023 | ⚠ within organs, on part of the lines; also absent: PARD6B, LMTK3, AP1G2 |
| [[PICK1]] | B | CCDC120 activity raises PICK1's level | lines that do not express CCDC120 (11) vs lines expressing it (39) | 2.04× lower at baseline in the lines without CCDC120 | 0.024 | ⚠ within organs, on part of the lines; also absent: PARD6B, LMTK3, AP1G2 |

## Where it sits

- **Module**: [[Module 031]] — Formation of the cornified envelope; 141 genes; every member is in the + arm (projection on the module's main direction 0.413). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.22; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-21.5, 26.8); signed map (-1.5, 2.9). **Vector** length 45.2, 6.45% of its response variance represented; |z| ≥ 3 in 639 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift | +2.1 | +2.7 |
|  | [[Fluvoxamine (drug)]] 0.5 µM |  | +1.1 | +1.8 |
|  | [[Tirabrutinib (hydrochloride) (drug)]] 0.5 µM |  | +1.0 | +2.4 |
|  | [[Vortioxetine (drug)]] 0.5 µM |  | +1.0 | +1.3 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +0.9 | +1.0 |
|  | [[Auranofin (drug)]] 5 µM |  | +0.9 | -1.5 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -3.0 | -12.1 |
|  | [[Idarubicin (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.1 | -2.0 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change | -1.8 | -2.1 |
|  | [[TAK-901 (drug)]] 5 µM |  | -1.6 | -3.7 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift | -1.4 | -1.9 |
|  | [[Verteporfin (drug)]] 5 µM |  | -1.3 | -1.1 |
|  | [[Sulfatinib (drug)]] 5 µM |  | -1.3 | -2.1 |
|  | [[Arbutin (drug)]] 5 µM |  | -1.2 | -1.3 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -1.2 | -1.1 |
|  | [[Bosentan (hydrate) (drug)]] 0.5 µM |  | -1.2 | -1.6 |

## What is on record

|  |  |
|---|---|
| Name | coiled-coil domain containing 120 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | Xp11.23 — chrX:49,053,572-49,069,857 (+) |
| Ensembl biotype | protein_coding |
| Also known as | JM11 |
| Matched by | ensembl_id |

**Function**, from UniProt [Q96HB5](https://www.uniprot.org/uniprotkb/Q96HB5) (Coiled-coil domain-containing protein 120):

> Centriolar protein required for centriole subdistal appendage assembly and microtubule anchoring in interphase cells. Together with CCDC68, cooperate with subdistal appendage components ODF2, NIN and CEP170 for hierarchical subdistal appendage assembly. Recruits NIN and CEP170 to centrosomes. Also required for neurite growth. Localizes CYTH2 to vesicles to allow its transport along neurites, and subsequent ARF6 activation and neurite growth.

**Summary**, from NCBI Gene [90060](https://www.ncbi.nlm.nih.gov/gene/90060):

> This gene encodes a protein that contains a coiled-coil domain. Several alternatively spliced transcript variants encoding multiple isoforms have been found for this gene. [provided by RefSeq, Nov 2012]

**Accessions** — [HGNC:28910](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:28910) · Entrez [90060](https://www.ncbi.nlm.nih.gov/gene/90060) · UniProt [Q96HB5](https://www.uniprot.org/uniprotkb/Q96HB5) · Ensembl [ENSG00000147144](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000147144)

## Data

Gene col 7155: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7155); `tables/drug_effects.parquet` (11 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7155, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7155]; `tensor/DDL_lfc|DDL_z.npy` [7155]; `embed/gene_vectors.npy` [7155]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7155 or target_col == 7155). Every well: [[CCDC120 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CCDC120.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
