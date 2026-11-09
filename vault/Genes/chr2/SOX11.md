---
symbol: "SOX11"
type: "gene"
col: 10759
ensembl_id: "ENSG00000176887"
name: "SRY-box transcription factor 11"
location: "2p25.2"
module: 9
arm: "+"
pooled_cpm: 9.43
n_lines_expressing: 13
n_dd_up: 26
n_dd_down: 1
n_dd_up_clean: 16
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 4
direction_downstream: 9
tags: ["gene", "module/009"]
generated_by: "tahoemap"
---

# SOX11

*SRY-box transcription factor 11* — 2p25.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 26 drug-doses (10 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 4.50× (z +15.4, q 0e+00, up in 10 of 11 measured lines).
> Pooled over the cell lines (median), lowered significantly by 1 drug-dose (none with an alert); the strongest is [[Anethole trithione (drug)]] 0.5 µM: 0.555× (z -4.3, q 0.011, down in 0 of 11 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.05 µM in 1 line (SHP-77 0.161×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 5 µM in 1 line (H4 0.161×; ⚠ toxic; transcription drop).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ABCC9]] (+0.62, fdr 1e-05), [[LINC00958]] (+0.61, fdr 1e-05), [[LINC02241]] (+0.60, fdr 2e-05); moves opposite to [[SEPTIN7P14]] (-0.51, fdr 3e-05), [[NUDT21]] (-0.50, fdr 3e-05), [[GGCX]] (-0.50, fdr 9e-05).
> It is in [[Module 009]], a single-armed module (Neuronal System).
> Probable direction (from the cell lines, not proof of direct regulation): 4 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); 9 go from it, the strongest it → [[OFCC1]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 26 in all, 10 with an alert ⚠; shown: the 15 strongest and the 7 next strongest without an alert. 26 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 10 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10759.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **4.50×** | +15.4 | 0e+00 | 10/11 (A498, HOP62, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **3.09×** | +11.5 | 3e-28 | 9/11 (A498, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~24% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **4.26×** | +10.5 | 2e-23 | 3/11 (HOP62, HS-578T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.43×** | +8.6 | 2e-15 | 1/8 (HOP62) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.88×** | +7.1 | 2e-10 | 2/8 (A498, HOP62) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.29×** | +6.0 | 2e-07 | 10/11 (A-172, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here) |
| [[Auranofin (drug)]] 5 µM |  | **2.25×** | +5.8 | 4e-07 | 7/11 (A-172, A498, …) | top dose only |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~27% of this change | **2.02×** | +5.1 | 3e-05 | 3/8 (CHP-212, SHP-77, …) | inconsistent across doses | low cells (technical?) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | **1.96×** | +4.9 | 8e-05 | 2/10 (H4, A-172) | top dose only |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.95×** | +4.6 | 2e-04 | 4/9 (BT-474, A498, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.92×** | +4.5 | 3e-04 | 4/11 (HOP62, H4, …) | top dose only | cell-cycle shift (explains ~5% here); position effect removed |
| [[Tucidinostat (drug)]] 5 µM |  | **1.52×** | +4.3 | 9e-04 | 7/11 (SHP-77, SNU-423, …) | rises with dose |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.84×** | +4.2 | 1e-03 | 5/9 (A498, SNU-423, …) | top dose only | cell-cycle shift (explains ~21% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.47×** | +3.9 | 0.004 | 5/11 (HOP62, BT-474, …) | top dose only |  |
| [[vincristine (drug)]] 0.5 µM |  | **2.02×** | +3.6 | 0.011 | 4/11 (BT-474, SHP-77, …) | two highest doses | low cells (technical?); noisy plate (z scaled); position effect removed |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.64×** | +3.6 | 0.013 | 9/11 (A-172, A498, …) | rises with dose | cell-cycle shift (explains ~18% here) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **1.40×** | +3.4 | 0.019 | 5/11 (SHP-77, BT-474, …) | rises with dose |  |
| [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | **1.59×** | +3.3 | 0.025 | 2/11 (A498, HOP62) | inconsistent across doses | position effect removed |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.57×** | +3.1 | 0.048 | 4/10 (HOP62, A498, …) | top dose only | cell-cycle shift (explains ~1% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **1.53×** | +3.1 | 0.054 | 1/11 (A498) | inconsistent across doses | cell-cycle shift (explains ~8% here); position effect removed |
| [[Peretinoin (drug)]] 5 µM |  | **1.55×** | +3.0 | 0.062 | 6/10 (BT-474, A498, …) | rises with dose | position effect removed |
| [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM |  | **1.51×** | +3.0 | 0.066 | 1/10 (SNU-423) | inconsistent across doses | low cells (technical?) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 1 in all, none with an alert. 1 of them lowers it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 10759.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.05 µM in 1 line (SHP-77 0.161×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 5 µM in 1 line (H4 0.161×; ⚠ toxic; transcription drop).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Anethole trithione (drug)]] 0.5 µM |  | **0.555×** | -4.3 | 0.011 | 0/11 | two highest doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.04 per unit of S-phase module lfc, +0.40 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10759. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A498 (line)]] | wt | 25.9 | 9 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 16.4× (z +28.1) | — |
| [[A-172 (line)]] | wt | 136 | 6 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 6.84× (z +20.5) | — |
| [[HOP62 (line)]] | alt | 16.8 | 6 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 9.99× (z +18.9) | — |
| [[BT-474 (line)]] | alt | 49.3 | 5 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.51× (z +11.7) | — |
| [[SHP-77 (line)]] | alt | 109 | 1 | 1 (1 ⚠) | [[Vinblastine (sulfate) (drug)]] 5 µM 2.42× (z +9.9) | [[Dinaciclib (drug)]] 0.05 µM 0.161× (z -13.5) ⚠ toxic; transcription drop |
| [[H4 (line)]] | wt | 38.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.161× (z -9.0) ⚠ toxic; transcription drop |
| [[HS-578T (line)]] | alt | 2.36 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 15.2× (z +9.3) | — |
| [[A-427 (line)]] | wt | 0.754 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 0.603 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 1.52 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 0.787 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 0.907 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 0.686 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 0.603 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 94.9 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 0.757 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 0.792 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 0.739 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 0.762 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 0.683 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 0.904 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.03 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 0.669 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 0.701 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 0.675 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 0.930 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 0.659 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.604 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 0.703 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 0.594 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 0.635 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 8.52 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 2.04 n.m. | — | — | — | — |
| [[NCI-H2347 (line)]] | alt | 1.90 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 0.763 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 9.58 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 0.990 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 0.580 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 0.583 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 0.778 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 0.885 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 0.668 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 0.811 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 6.74 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 35.9 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 0.964 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 3.56 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 0.674 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 0.976 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 0.671 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10759), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*90 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ABCC9]] | +0.62 | +0.55 / +0.55 | both halves | 1e-05 |  |
| [[LINC00958]] | +0.61 | +0.61 / +0.52 | both halves | 1e-05 |  |
| [[LINC02241]] | +0.60 | +0.63 / +0.48 | both halves | 2e-05 |  |
| [[LINC01828]] | +0.60 | +0.57 / +0.58 | both halves | 1e-05 |  |
| [[LYPD1]] | +0.58 | +0.59 / +0.44 | both halves | 3e-05 |  |
| [[XIRP2]] | +0.57 | +0.43 / +0.48 | both halves | 3e-05 |  |
| [[MSR1]] | +0.56 | +0.65 / +0.48 | both halves | 2e-05 |  |
| [[FAM110B]] | +0.56 | +0.48 / +0.48 | both halves | 2e-05 |  |
| [[NRG1]] | +0.55 | +0.47 / +0.49 | both halves | 2e-05 |  |
| [[LINC01695]] | +0.54 | +0.48 / +0.52 | both halves | 2e-05 |  |
| [[FMN2]] | +0.54 | +0.63 / +0.50 | both halves | 1e-05 |  |
| [[NTRK3]] | +0.54 | +0.54 / +0.47 | both halves | 2e-05 |  |

## Genes that move opposite

*10 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SEPTIN7P14]] | -0.51 | -0.44 / -0.43 | both halves | 3e-05 |  |
| [[NUDT21]] | -0.50 | -0.43 / -0.47 | both halves | 3e-05 |  |
| [[GGCX]] | -0.50 | -0.55 / -0.36 | both halves | 9e-05 |  |
| [[SUGT1P4-STRA6LP-CCDC180]] | -0.49 | -0.38 / -0.41 | both halves | 6e-05 |  |
| [[OXNAD1]] | -0.49 | -0.46 / -0.42 | both halves | 4e-05 |  |
| [[ANAPC5]] | -0.48 | -0.38 / -0.42 | both halves | 6e-05 |  |
| [[MSTO2P]] | -0.47 | -0.51 / -0.37 | both halves | 8e-05 |  |
| [[GLT8D1]] | -0.47 | -0.50 / -0.36 | both halves | 9e-05 |  |
| [[SHQ1]] | -0.45 | -0.47 / -0.31 | both halves | 2e-04 |  |
| [[STRA6LP]] | -0.45 | -0.32 / -0.41 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 2, C 2.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers SOX11's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 5.9% of all compounds | 0.044 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[SPHK1]] | B | SPHK1 activity lowers SOX11's level | lines that do not express SPHK1 (12) vs lines expressing it (38) | 1.47× higher at baseline in the lines without SPHK1 | 0.052 | ⚠ within organs, on part of the lines; also absent: TMEM158, CAV1, NR3C1 |
| [[EPHA4]] | C | EPHA4 activity raises SOX11's level | lines that do not express EPHA4 (19) vs lines expressing it (31) | 2.79× lower at baseline in the lines without EPHA4 | 0.082 | ⚠ within organs, on part of the lines; also absent: SNAI2, GNG2, TNFSF10; co-absent with the target |
| [[KCND2]] | C | KCND2 activity raises SOX11's level | lines that do not express KCND2 (32) vs lines expressing it (18) | 3.44× lower at baseline in the lines without KCND2 | 0.084 | ⚠ within organs, on part of the lines; also absent: ENSG00000285330, SYT4, DCT; maybe low, not absent; co-absent with the target |

### Downstream of this gene

*9 arrows, 9 of them with an alert ⚠; grade A 0, B 3, C 6.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[OFCC1]] | B | SOX11 activity raises OFCC1's level | lines that do not express SOX11 (37) vs lines expressing it (13) | 2.06× lower at baseline in the lines without SOX11 | 0.049 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: VCAM1, DPP10, RUNX1T1 |
| [[XIRP2]] | B | SOX11 activity raises XIRP2's level | lines that do not express SOX11 (37) vs lines expressing it (13) | 1.31× lower at baseline in the lines without SOX11 | 0.082 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: VCAM1, DPP10, RUNX1T1 |
| [[MIR4300HG]] | B | SOX11 activity raises MIR4300HG's level | lines that do not express SOX11 (37) vs lines expressing it (13) | 1.57× lower at baseline in the lines without SOX11 | 0.095 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: VCAM1, DPP10, RUNX1T1 |
| [[B3GALT1]] | C | SOX11 activity raises B3GALT1's level | lines that do not express SOX11 (37) vs lines expressing it (13) | 2.04× lower at baseline in the lines without SOX11 | 0.064 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: VCAM1, DPP10, RUNX1T1; co-absent with the target |
| [[ANKRD30B]] | C | SOX11 activity raises ANKRD30B's level | lines that do not express SOX11 (37) vs lines expressing it (13) | 2.11× lower at baseline in the lines without SOX11 | 0.067 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: VCAM1, DPP10, RUNX1T1; co-absent with the target |
| [[COLEC10]] | C | SOX11 activity raises COLEC10's level | lines that do not express SOX11 (37) vs lines expressing it (13) | 1.30× lower at baseline in the lines without SOX11 | 0.080 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: VCAM1, DPP10, RUNX1T1; co-absent with the target |
| [[INHBA]] | C | SOX11 activity raises INHBA's level | lines that do not express SOX11 (37) vs lines expressing it (13) | 4.43× lower at baseline in the lines without SOX11 | 0.082 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: VCAM1, DPP10, RUNX1T1; co-absent with the target |
| [[SSTR2]] | C | SOX11 activity raises SSTR2's level | lines that do not express SOX11 (37) vs lines expressing it (13) | 2.25× lower at baseline in the lines without SOX11 | 0.089 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: VCAM1, DPP10, RUNX1T1; co-absent with the target |
| [[LINC02220]] | C | SOX11 activity raises LINC02220's level | lines that do not express SOX11 (37) vs lines expressing it (13) | 1.65× lower at baseline in the lines without SOX11 | 0.089 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: VCAM1, DPP10, RUNX1T1; co-absent with the target |

## Where it sits

- **Module**: [[Module 009]] — Neuronal System; 222 genes; every member is in the + arm (projection on the module's main direction 0.522). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (35.7, 28.3); signed map (37.9, 28.3). **Vector** length 37.2, 10.4% of its response variance represented; |z| ≥ 3 in 294 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +3.7 | +15.4 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +3.4 | +10.5 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +3.1 | +4.3 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +2.9 | +8.6 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +2.9 | +11.5 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.4 | +5.8 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +1.5 | +3.9 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +1.4 | +2.3 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +1.3 | +1.7 |
| fall | [[Clobetasol propionate (drug)]] 5 µM |  | -1.3 | -1.9 |
|  | [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | -1.2 | -1.1 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -1.2 | -2.0 |
|  | [[Budesonide (drug)]] 5 µM |  | -1.2 | -2.0 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -1.1 | -2.1 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -1.1 | -2.6 |

## What is on record

|  |  |
|---|---|
| Name | SRY-box transcription factor 11 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 2p25.2 — chr2:5,692,384-5,701,385 (+) |
| Ensembl biotype | protein_coding |
| Gene groups (HGNC) | SRY-box transcription factors |
| Matched by | ensembl_id |

**Function**, from UniProt [P35716](https://www.uniprot.org/uniprotkb/P35716) (Transcription factor SOX-11):

> Transcription factor that acts as a transcriptional activator. Binds cooperatively with POU3F2/BRN2 or POU3F1/OCT6 to gene promoters, which enhances transcriptional activation (By similarity). Acts as a transcriptional activator of TEAD2 by binding to its gene promoter and first intron (By similarity). Plays a redundant role with SOX4 and SOX12 in cell survival of developing tissues such as the neural tube, branchial arches and somites, thereby contributing to organogenesis (By similarity).

**Summary**, from NCBI Gene [6664](https://www.ncbi.nlm.nih.gov/gene/6664):

> This intronless gene encodes a member of the SOX (SRY-related HMG-box) family of transcription factors involved in the regulation of embryonic development and in the determination of the cell fate. The encoded protein may act as a transcriptional regulator after forming a protein complex with other proteins. The protein may function in the developing nervous system and play a role in tumorigenesis. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:11191](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:11191) · Entrez [6664](https://www.ncbi.nlm.nih.gov/gene/6664) · UniProt [P35716](https://www.uniprot.org/uniprotkb/P35716) · Ensembl [ENSG00000176887](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000176887)

## Data

Gene col 10759: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10759); `tables/drug_effects.parquet` (27 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10759, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10759]; `tensor/DDL_lfc|DDL_z.npy` [10759]; `embed/gene_vectors.npy` [10759]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10759 or target_col == 10759). Every well: [[SOX11 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SOX11.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
