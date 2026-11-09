---
symbol: "SCUBE3"
type: "gene"
col: 7071
ensembl_id: "ENSG00000146197"
name: "signal peptide, CUB domain and EGF like domain containing 3"
location: "6p21.3"
module: 13
arm: "+"
pooled_cpm: 4.88
n_lines_expressing: 24
n_dd_up: 23
n_dd_down: 0
n_dd_up_clean: 11
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 18
direction_downstream: 2
tags: ["gene", "module/013"]
generated_by: "tahoemap"
---

# SCUBE3

*signal peptide, CUB domain and EGF like domain containing 3* — 6p21.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 23 drug-doses (12 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 5.21× (z +15.5, q 0e+00, up in 6 of 8 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 2.00× (z +9.2, q 8e-18, up in 4 of 14 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Digitoxin (drug)]] 5 µM in 1 line (A-172 0.0890×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~50% of this change); [[Homoharringtonine (drug)]] 5 µM in 1 line (HS-578T 0.172×; ⚠ cell-cycle shift, explains ~16% of this change); [[Homoharringtonine (drug)]] 0.5 µM in 1 line (hTERT-HPNE 0.102×); [[Ouabain (Octahydrate) (drug)]] 5 µM in 1 line (HS-578T 0.0994×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[DKK3]] (+0.72, fdr 7e-06), [[PRSS23]] (+0.69, fdr 7e-06), [[COL6A1]] (+0.69, fdr 7e-06); moves opposite to [[TNFAIP6]] (-0.47, fdr 4e-04), [[DTNB]] (-0.45, fdr 4e-05).
> It is in [[Module 013]], a single-armed module (epithelial mesenchymal transition).
> Probable direction (from the cell lines, not proof of direct regulation): 18 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); 2 go from it, the strongest it → [[COL1A2]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 23 in all, 12 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 23 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 12 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7071.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **5.21×** | +15.5 | 0e+00 | 6/8 (PANC-1, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **4.46×** | +12.7 | 2e-34 | 5/5 (PANC-1, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **3.72×** | +10.8 | 8e-25 | 5/5 (PANC-1, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.00×** | +9.2 | 8e-18 | 4/14 (SNU-423, C32, …) | top dose only | cell-cycle shift (explains ~4% here) |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **2.57×** | +4.6 | 4e-04 | 3/4 (NCI-H2347, hTERT-HPNE, …) | top dose only | noisy plate (z scaled) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.38×** | +4.3 | 0.002 | 2/20 (A-172, C32) | top dose only |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.65×** | +4.3 | 0.002 | 0/12 | top dose only | cell-cycle shift (explains ~9% here) |
| [[Panobinostat (drug)]] 5 µM |  | **1.54×** | +4.1 | 0.003 | 2/21 (Panc 03.27, SW 1088) | rises with dose | cell-cycle shift (explains ~16% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.36×** | +4.0 | 0.003 | 6/20 (BT-474, SK-MEL-2, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.59×** | +3.9 | 0.005 | 0/6 | top dose only | cell-cycle shift (explains ~8% here) |
| [[AZD2858 (drug)]] 0.5 µM | ⚠ toxic | **1.80×** | +3.9 | 0.005 | 0/6 | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **2.08×** | +3.6 | 0.015 | 0/6 | top dose only | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[XRK3F2 (drug)]] 0.5 µM |  | **1.71×** | +3.6 | 0.015 | 0/6 | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Omeprazole (drug)]] 0.5 µM |  | **1.46×** | +3.5 | 0.016 | 2/13 (SNU-423, HOP62) | inconsistent across doses |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.49×** | +3.4 | 0.027 | 2/7 (PANC-1, NCI-H2347) | top dose only | cell-cycle shift (explains ~13% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.47×** | +3.3 | 0.037 | 0/8 | rises with dose | cell-cycle shift (explains ~12% here) |
| [[Selinexor (drug)]] 5 µM |  | **1.27×** | +3.2 | 0.044 | 0/20 | top dose only | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Trametinib (drug)]] 0.5 µM |  | **1.29×** | +3.0 | 0.076 | 0/19 | inconsistent across doses | noisy plate (z scaled) |
| [[Glycyrrhizic acid (drug)]] 0.05 µM |  | **1.42×** | +2.9 | 0.097 | 0/9 | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 2 in all, none with an alert. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 7071.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Digitoxin (drug)]] 5 µM in 1 line (A-172 0.0890×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~50% of this change); [[Homoharringtonine (drug)]] 5 µM in 1 line (HS-578T 0.172×; ⚠ cell-cycle shift, explains ~16% of this change); [[Homoharringtonine (drug)]] 0.5 µM in 1 line (hTERT-HPNE 0.102×); [[Ouabain (Octahydrate) (drug)]] 5 µM in 1 line (HS-578T 0.0994×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 0.5 µM |  | 0.697× | -3.4 | 0.36 | 6/18 (A-172, HS-578T, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Lucanthone (drug)]] 0.05 µM |  | 0.675× | -3.2 | 0.36 | 2/21 (NCI-H2030, SW 1088) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.14 per unit of S-phase module lfc, +0.04 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7071. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HS-578T (line)]] | alt | 22.3 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.172× (z -9.8) ⚠ cell-cycle shift, explains ~16% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0994× (z -9.1) |
| [[A-172 (line)]] | wt | 6.09 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0890× (z -10.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~50% of this change |
| [[hTERT-HPNE (line)]] | wt | 99.8 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.102× (z -9.7) |
| [[PANC-1 (line)]] | alt | 11.6 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 7.48× (z +11.1) ⚠ toxic; transcription drop | — |
| [[A-427 (line)]] | wt | 1.15 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 0.812 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 1.20 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 2.31 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 0.904 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 1.37 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 2.48 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 1.23 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 0.936 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 1.42 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 0.743 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 1.15 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 1.06 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 0.963 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 1.07 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 9.76 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 0.854 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 0.851 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 1.08 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 0.762 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 1.15 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 1.29 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 0.689 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 2.98 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 1.03 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 1.05 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 1.37 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 4.76 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 1.69 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 30.3 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 1.21 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 5.87 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 11.3 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 1.43 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 0.896 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 1.32 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 1.09 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 2.82 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 0.932 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 1.27 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 13.2 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 1.40 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 1.18 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 0.900 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 0.979 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 1.17 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7071), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*98 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DKK3]] | +0.72 | +0.63 / +0.73 | both halves | 7e-06 | **novel candidate** |
| [[PRSS23]] | +0.69 | +0.60 / +0.68 | both halves | 7e-06 | **novel candidate** |
| [[COL6A1]] | +0.69 | +0.63 / +0.64 | both halves | 7e-06 | pathway: Degradation of the extracellular matrix |
| [[ITGA11]] | +0.68 | +0.61 / +0.71 | both halves | 7e-06 | pathway: Extracellular matrix organization |
| [[DIRAS3]] | +0.66 | +0.66 / +0.56 | both halves | 1e-05 | **novel candidate** |
| [[COL1A2]] | +0.63 | +0.56 / +0.64 | both halves | 1e-05 | pathway: Degradation of the extracellular matrix |
| [[COL5A1]] | +0.63 | +0.65 / +0.59 | both halves | 7e-06 | pathway: Degradation of the extracellular matrix |
| [[APCDD1L]] | +0.62 | +0.52 / +0.65 | both halves | 1e-05 |  |
| [[COL6A2]] | +0.61 | +0.63 / +0.58 | both halves | 8e-06 | pathway: Degradation of the extracellular matrix |
| [[MMP14]] | +0.61 | +0.51 / +0.65 | both halves | 1e-05 | pathway: Degradation of the extracellular matrix |
| [[HHIP]] | +0.61 | +0.63 / +0.55 | both halves | 1e-05 |  |
| [[GDNF-AS1]] | +0.61 | +0.65 / +0.53 | both halves | 1e-05 |  |

## Genes that move opposite

*2 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TNFAIP6]] | -0.47 | -0.56 / -0.26 | both halves | 4e-04 |  |
| [[DTNB]] | -0.45 | -0.42 / -0.41 | both halves | 4e-05 | pathway: Extracellular matrix organization |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*18 arrows, 18 of them with an alert ⚠; grade A 0, B 2, C 16. Shown: the 12 strongest; 6 more arrows (6 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers SCUBE3's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 5.9% of all compounds | 0.044 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[NES]] | B | NES activity raises SCUBE3's level | lines that do not express NES (26) vs lines expressing it (24) | 1.89× lower at baseline in the lines without NES | 0.085 | ⚠ within organs, on part of the lines; also absent: LAPTM5, CSPG4, ENSG00000230490 |
| [[COL1A1]] | C | COL1A1 activity raises SCUBE3's level | lines that do not express COL1A1 (34) vs lines expressing it (16) | 2.81× lower at baseline in the lines without COL1A1 | 0.007 | ⚠ within organs, on part of the lines; also absent: DCN, LAYN, LINC01411; co-absent with the target |
| [[SPARC]] | C | SPARC activity raises SCUBE3's level | lines that do not express SPARC (34) vs lines expressing it (16) | 2.30× lower at baseline in the lines without SPARC | 0.015 | ⚠ within organs, on part of the lines; co-occurs with KRAS, TP53; also absent: ITGA4, MMP2, ENSG00000222032; co-absent with the target |
| [[GDNF]] | C | GDNF activity raises SCUBE3's level | lines that do not express GDNF (38) vs lines expressing it (12) | 2.32× lower at baseline in the lines without GDNF | 0.015 | ⚠ within organs, on part of the lines; co-occurs with KRAS, TP53; also absent: ENSG00000235749, ITIH5, TDRD9; co-absent with the target |
| [[MIR493HG]] | C | MIR493HG activity raises SCUBE3's level | lines that do not express MIR493HG (36) vs lines expressing it (14) | 2.83× lower at baseline in the lines without MIR493HG | 0.036 | ⚠ within organs, on part of the lines; also absent: MEG3, MEG8, ENSG00000232252; co-absent with the target |
| [[CTHRC1]] | C | CTHRC1 activity raises SCUBE3's level | lines that do not express CTHRC1 (26) vs lines expressing it (24) | 2.26× lower at baseline in the lines without CTHRC1 | 0.046 | ⚠ within organs, on part of the lines; also absent: ARMCX1, MAGI2-AS3, ITGA4; maybe low, not absent; co-absent with the target |
| [[CSPG4]] | C | CSPG4 activity raises SCUBE3's level | lines that do not express CSPG4 (31) vs lines expressing it (19) | 2.30× lower at baseline in the lines without CSPG4 | 0.057 | ⚠ within organs, on part of the lines; also absent: MMP2, PCDH18, AEBP1; co-absent with the target |
| [[PDGFRB]] | C | PDGFRB activity raises SCUBE3's level | lines that do not express PDGFRB (36) vs lines expressing it (14) | 2.22× lower at baseline in the lines without PDGFRB | 0.059 | ⚠ within organs, on part of the lines; co-occurs with KRAS, TP53; also absent: COL3A1, ALPK2, GREM2; co-absent with the target |
| [[DIRAS3]] | C | DIRAS3 activity raises SCUBE3's level | lines that do not express DIRAS3 (44) vs lines expressing it (6) | 3.43× lower at baseline in the lines without DIRAS3 | 0.060 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: ENSG00000230258, MTND1P23, APOB; co-absent with the target |
| [[DENND2A]] | C | DENND2A activity raises SCUBE3's level | lines that do not express DENND2A (23) vs lines expressing it (27) | 1.80× lower at baseline in the lines without DENND2A | 0.061 | ⚠ within organs, on part of the lines; also absent: PTPRN, SPARC, BAALC; maybe low, not absent; co-absent with the target |
| [[COL1A2]] | C | COL1A2 activity raises SCUBE3's level | lines that do not express COL1A2 (37) vs lines expressing it (13) | 2.57× lower at baseline in the lines without COL1A2 | 0.064 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: PKD1L1-AS1, FCRLA, PSG5; co-absent with the target |

### Downstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 0, C 2.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[COL1A2]] | C | SCUBE3 activity raises COL1A2's level | lines that do not express SCUBE3 (26) vs lines expressing it (24) | 7.13× lower at baseline in the lines without SCUBE3 | 0.052 | ⚠ within organs, on part of the lines; also absent: RNF175, ENSG00000263655, COL11A1; maybe low, not absent; co-absent with the target |
| [[COL6A2]] | C | SCUBE3 activity raises COL6A2's level | lines that do not express SCUBE3 (26) vs lines expressing it (24) | 6.28× lower at baseline in the lines without SCUBE3 | 0.055 | ⚠ within organs, on part of the lines; also absent: RNF175, ENSG00000263655, COL11A1; maybe low, not absent; co-absent with the target |

## Where it sits

- **Module**: [[Module 013]] — epithelial mesenchymal transition; 213 genes; every member is in the + arm (projection on the module's main direction 0.648). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.20; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (55.2, 18.1); signed map (23.3, 44.6). **Vector** length 31.4, 5.78% of its response variance represented; |z| ≥ 3 in 452 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *Assembly of collagen fibrils and other multimeric structures* (reactome, mean cos +0.51 to 10); *Collagen degradation* (reactome, mean cos +0.56 to 8); *Collagen chain trimerization* (reactome, mean cos +0.55 to 7).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +3.4 | +12.7 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +3.2 | +15.5 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +3.2 | +10.8 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +1.8 | +9.2 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | +1.4 | +4.3 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +1.0 | +4.0 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +1.0 | +4.3 |
|  | [[PH-797804 (drug)]] 5 µM |  | +0.6 | -0.3 |
|  | [[Filgotinib (drug)]] 5 µM |  | +0.6 | +1.7 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | +0.6 | +1.1 |
| fall | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -0.9 | -2.7 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | -0.9 | -3.4 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | -0.7 | -1.8 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -0.7 | -1.7 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -0.7 | -2.5 |
|  | [[Triamcinolone (drug)]] 0.5 µM |  | -0.7 | -2.0 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -0.6 | -2.2 |
|  | [[EX229 (drug)]] 5 µM |  | -0.6 | -0.2 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -0.6 | -1.0 |

## What is on record

|  |  |
|---|---|
| Name | signal peptide, CUB domain and EGF like domain containing 3 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 6p21.3 — chr6:35,213,956-35,253,079 (+) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ34743; previously CEGF3 |
| Reactome | 2 pathways, smallest: Degradation of the extracellular matrix; Extracellular matrix organization |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8IX30](https://www.uniprot.org/uniprotkb/Q8IX30) (Signal peptide, CUB and EGF-like domain-containing protein 3):

> Is a positive regulator of the BMP signaling pathway, required for proper chondrogenesis, osteogenesis and skeletal development. It acts as a coreceptor for BMP ligands, particularly BMP2 and BMP4, facilitating their interactions with BMP type I receptors. It is required for ligand-induced recruitment of BMP receptors to lipid rafts (By similarity). Binds to TGFBR2 and activates TGFB signaling. In lung cancer cells, could serve as an endogenous autocrine and paracrine ligand of TGFBR2, which …

**Summary**, from NCBI Gene [222663](https://www.ncbi.nlm.nih.gov/gene/222663):

> This gene encodes a member of the signal peptide, complement subcomponents C1r/C1s, Uegf, bone morphogenetic protein-1 and epidermal growth factor-like domain containing protein family. Overexpression of this gene in human embryonic kidney cells results in secretion of a glycosylated form of the protein that forms oligomers and tethers to the cell surface. This gene is upregulated in lung cancer tumor tissue compared to healthy tissue and is associated with loss of the epithelial marker …

**Accessions** — [HGNC:13655](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:13655) · Entrez [222663](https://www.ncbi.nlm.nih.gov/gene/222663) · UniProt [Q8IX30](https://www.uniprot.org/uniprotkb/Q8IX30) · Ensembl [ENSG00000146197](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000146197)

## Data

Gene col 7071: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7071); `tables/drug_effects.parquet` (25 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7071, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7071]; `tensor/DDL_lfc|DDL_z.npy` [7071]; `embed/gene_vectors.npy` [7071]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7071 or target_col == 7071). Every well: [[SCUBE3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SCUBE3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
