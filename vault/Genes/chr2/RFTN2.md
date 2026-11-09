---
symbol: "RFTN2"
type: "gene"
col: 8603
ensembl_id: "ENSG00000162944"
name: "raftlin family member 2"
location: "2q33.1"
module: 191
arm: "+"
pooled_cpm: 2.11
n_lines_expressing: 50
n_dd_up: 24
n_dd_down: 0
n_dd_up_clean: 18
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 10
direction_downstream: 0
tags: ["gene", "module/191"]
generated_by: "tahoemap"
---

# RFTN2

*raftlin family member 2* — 2q33.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 24 drug-doses (6 with an alert ⚠); the strongest is [[Auranofin (drug)]] 5 µM: 7.26× (z +19.1, q 0e+00, up in 32 of 35 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CFAP20DC-DT]] (+0.76, fdr 7e-06), [[KCNAB1]] (+0.73, fdr 7e-06), [[SGCD]] (+0.73, fdr 1e-05).
> It is in [[Module 191]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 10 arrows point to it, the strongest [[TP63]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 24 in all, 6 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 24 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8603.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Auranofin (drug)]] 5 µM |  | **7.26×** | +19.1 | 0e+00 | 32/35 (C32, HT-29, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 5 µM |  | **3.90×** | +18.5 | 0e+00 | 23/32 (NCI-H460, A-172, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **3.40×** | +16.6 | 0e+00 | 21/27 (HEC-1-A, HOP62, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.91×** | +12.6 | 2e-34 | 0/1 | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **3.25×** | +11.3 | 1e-27 | 7/10 (SW480, HT-29, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.47×** | +8.0 | 9e-14 | 0/2 | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.46×** | +8.0 | 1e-13 | 13/28 (HEC-1-A, NCI-H2030, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | **2.13×** | +7.0 | 2e-10 | 18/37 (NCI-H460, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.96×** | +6.4 | 7e-09 | 2/17 (NCI-H1573, PANC-1) | top dose only | cell-cycle shift (explains ~1% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.45×** | +5.1 | 2e-05 | 5/43 (PANC-1, NCI-H460, …) | top dose only |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.65×** | +4.6 | 2e-04 | 5/23 (A549, NCI-H460, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.62×** | +4.4 | 4e-04 | 7/31 (NCI-H460, A498, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 5 µM |  | **1.37×** | +4.3 | 9e-04 | 7/44 (C32, SK-MEL-2, …) | top dose only | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.58×** | +4.2 | 0.001 | 4/16 (NCI-H460, HEC-1-A, …) | top dose only | cell-cycle shift (explains ~1% here) |
| [[Cobimetinib (drug)]] 0.5 µM |  | **1.52×** | +4.0 | 0.002 | 9/37 (C32, SK-MEL-2, …) | rises with dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.55×** | +3.9 | 0.004 | 5/39 (RKO, A498, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Cobimetinib (drug)]] 5 µM |  | **1.52×** | +3.9 | 0.004 | 8/28 (C32, SW480, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.51×** | +3.7 | 0.006 | 6/34 (C32, LOX-IMVI, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM |  | **1.45×** | +3.5 | 0.012 | 2/17 (LS 180, NCI-H23) | inconsistent across doses | low cells (technical?) |
| [[Panobinostat (drug)]] 5 µM |  | **1.42×** | +3.3 | 0.024 | 13/45 (SW480, SW1417, …) | rises with dose | cell-cycle shift (explains ~0% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 2 in all, 1 with an alert ⚠. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 8603.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Daptomycin (drug)]] 0.5 µM | ⚠ unreliable plate only | 0.686× | -3.7 | 0.15 | 12/37 (SK-MEL-2, AsPC-1, …) | inconsistent across doses |  |
| [[S-Adenosyl-L-methionine (disulfate tosylate) (drug)]] 5 µM |  | 0.780× | -3.4 | 0.18 | 6/43 (Hs 766T, RKO, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.01 per unit of S-phase module lfc, +0.03 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8603. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 1.43 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 13.0× (z +9.0) | — |
| [[C32 (line)]] | wt | 18.3 | 1 | 0 | [[Auranofin (drug)]] 5 µM 7.06× (z +8.8) | — |
| [[HEC-1-A (line)]] | alt | 1.83 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 11.4× (z +8.7) | — |
| [[NCI-H460 (line)]] | wt | 2.01 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 7.22× (z +9.9) | — |
| [[A-427 (line)]] | wt | 0.853 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 1.04 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 2.62 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 1.29 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 1.09 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 1.17 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 1.54 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 1.11 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 11.6 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 1.76 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 2.94 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 2.01 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 1.19 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 1.06 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 1.12 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 1.15 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 2.45 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 5.31 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 1.11 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 1.09 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 1.23 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 1.72 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 1.60 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 6.91 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 2.31 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 0.959 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 1.22 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 3.98 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 2.61 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 0.856 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 2.66 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 4.60 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 0.871 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 0.813 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 1.01 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 5.75 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 1.38 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 5.49 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 1.10 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 1.51 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 1.59 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 1.48 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 2.87 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 1.26 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 1.05 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 2.28 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8603), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CFAP20DC-DT]] | +0.76 | +0.77 / +0.66 | both halves | 7e-06 |  |
| [[KCNAB1]] | +0.73 | +0.71 / +0.68 | both halves | 7e-06 |  |
| [[SGCD]] | +0.73 | +0.79 / +0.56 | both halves | 1e-05 |  |
| [[HULC]] | +0.71 | +0.71 / +0.67 | both halves | 7e-06 |  |
| [[GUCY1A2]] | +0.69 | +0.64 / +0.60 | both halves | 7e-06 |  |
| [[SEC1P]] | +0.69 | +0.68 / +0.59 | both halves | 7e-06 |  |
| [[ESR1]] | +0.68 | +0.67 / +0.61 | both halves | 7e-06 |  |
| [[DNAH3]] | +0.67 | +0.69 / +0.61 | both halves | 7e-06 |  |
| [[LINC02398]] | +0.67 | +0.61 / +0.58 | both halves | 7e-06 |  |
| [[DPP6]] | +0.66 | +0.63 / +0.55 | both halves | 1e-05 |  |
| [[MYO16]] | +0.66 | +0.65 / +0.57 | both halves | 1e-05 |  |
| [[MIR4300HG]] | +0.66 | +0.71 / +0.53 | both halves | 1e-05 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*10 arrows, 10 of them with an alert ⚠; grade A 0, B 10, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TP63]] | B | TP63 activity raises RFTN2's level | lines that do not express TP63 (39) vs lines expressing it (11) | 1.97× lower at baseline in the lines without TP63 | 0.015 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: SOX10, ENSG00000241168, TYR |
| [[NR1H4]] | B | NR1H4 activity raises RFTN2's level | lines that do not express NR1H4 (34) vs lines expressing it (16) | 1.45× lower at baseline in the lines without NR1H4 | 0.016 | ⚠ within organs, on part of the lines; co-occurs with KRAS, TP53; also absent: LINC01320, DCT, S100A1; maybe low, not absent |
| [[CNTN6]] | B | CNTN6 activity raises RFTN2's level | lines that do not express CNTN6 (38) vs lines expressing it (12) | 1.81× lower at baseline in the lines without CNTN6 | 0.022 | ⚠ within organs, on part of the lines; co-occurs with KRAS, TP53; also absent: ENSG00000234426, LINC02476, SPARC; maybe low, not absent |
| [[TOP2A]] | B | TOP2A activity lowers RFTN2's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 4.5% of all compounds | 0.026 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[LINC02240]] | B | LINC02240 activity raises RFTN2's level | lines that do not express LINC02240 (35) vs lines expressing it (15) | 1.76× lower at baseline in the lines without LINC02240 | 0.029 | ⚠ within organs, on part of the lines; co-occurs with KRAS, TP53; also absent: LINC02941, CHL1, EDNRB; maybe low, not absent |
| [[CHRNA7]] | B | CHRNA7 activity raises RFTN2's level | lines that do not express CHRNA7 (19) vs lines expressing it (31) | 1.35× lower at baseline in the lines without CHRNA7 | 0.061 | ⚠ within organs, on part of the lines; also absent: LRRC4B, NKD2, IGFL4; maybe low, not absent |
| [[LINC00504]] | B | LINC00504 activity raises RFTN2's level | lines that do not express LINC00504 (31) vs lines expressing it (19) | 1.38× lower at baseline in the lines without LINC00504 | 0.073 | ⚠ within organs, on part of the lines; also absent: ENSG00000287598, LINC02930, ENSG00000287474 |
| [[HAND2-AS1]] | B | HAND2-AS1 activity raises RFTN2's level | lines that do not express HAND2-AS1 (20) vs lines expressing it (30) | 1.49× lower at baseline in the lines without HAND2-AS1 | 0.074 | ⚠ within organs, on part of the lines; also absent: LINC02269, NPTX1, VAT1L; maybe low, not absent |
| [[PDZRN3]] | B | PDZRN3 activity raises RFTN2's level | lines that do not express PDZRN3 (30) vs lines expressing it (20) | 1.45× lower at baseline in the lines without PDZRN3 | 0.082 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: ENSG00000237268, ENSG00000253642, ENSG00000288098 |
| [[LINC02269]] | B | LINC02269 activity raises RFTN2's level | lines that do not express LINC02269 (17) vs lines expressing it (33) | 1.63× lower at baseline in the lines without LINC02269 | 0.088 | ⚠ within organs, on part of the lines; also absent: HAND2-AS1, C19orf81, TUSC3; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 191]]; 18 genes; every member is in the + arm (projection on the module's main direction 0.682). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (23.0, 26.9); signed map (30.5, 14.0). **Vector** length 50.8, 6.35% of its response variance represented; |z| ≥ 3 in 1,195 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Auranofin (drug)]] 5 µM |  | +6.8 | +19.1 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +5.6 | +18.5 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +3.8 | +12.6 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +3.8 | +11.3 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +3.8 | +16.6 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +1.8 | +5.1 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +1.6 | +3.9 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +1.4 | +2.5 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | +1.4 | +2.8 |
| fall | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.3 | +1.4 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.8 | -0.8 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -1.7 | -0.6 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | -1.6 | -0.5 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift | -1.6 | +0.3 |
|  | [[Brivudine (drug)]] 5 µM |  | -1.4 | -0.9 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -1.0 | -2.2 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -1.0 | -0.8 |
|  | [[Irinotecan (hydrochloride) (drug)]] 5 µM |  | -1.0 | -1.0 |
|  | [[Diphenhydramine (drug)]] 0.05 µM |  | -0.9 | -1.6 |

## What is on record

|  |  |
|---|---|
| Name | raftlin family member 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 2q33.1 — chr2:197,568,224-197,676,045 (-) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ30574, Raftlin-2; previously C2orf11 |
| Matched by | ensembl_id |

**Function**, from UniProt [Q52LD8](https://www.uniprot.org/uniprotkb/Q52LD8) (Raftlin-2):

> Upon bacterial lipopolysaccharide stimulation, mediates clathrin-dependent internalization of TLR4 in dendritic cells, resulting in activation of TICAM1-mediated signaling and subsequent IFNB1 production. May regulate B-cell antigen receptor-mediated signaling.

**Summary**, from NCBI Gene [130132](https://www.ncbi.nlm.nih.gov/gene/130132):

> Predicted to act upstream of or within dsRNA transport and response to exogenous dsRNA. Predicted to be located in plasma membrane. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:26402](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:26402) · Entrez [130132](https://www.ncbi.nlm.nih.gov/gene/130132) · UniProt [Q52LD8](https://www.uniprot.org/uniprotkb/Q52LD8) · Ensembl [ENSG00000162944](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000162944)

## Data

Gene col 8603: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8603); `tables/drug_effects.parquet` (26 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8603, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8603]; `tensor/DDL_lfc|DDL_z.npy` [8603]; `embed/gene_vectors.npy` [8603]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8603 or target_col == 8603). Every well: [[RFTN2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/RFTN2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
