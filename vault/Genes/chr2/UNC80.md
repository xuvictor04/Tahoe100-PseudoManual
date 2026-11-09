---
symbol: "UNC80"
type: "gene"
col: 6876
ensembl_id: "ENSG00000144406"
name: "unc-80 subunit of NALCN channel complex"
location: "2q34"
module: 9
arm: "+"
pooled_cpm: 2.35
n_lines_expressing: 34
n_dd_up: 28
n_dd_down: 0
n_dd_up_clean: 17
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 16
direction_downstream: 3
tags: ["gene", "module/009"]
generated_by: "tahoemap"
---

# UNC80

*unc-80 subunit of NALCN channel complex* — 2q34

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 28 drug-doses (11 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 5.79× (z +18.0, q 0e+00, up in 9 of 14 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[GLRA3]] (+0.75, fdr 7e-06), [[SPOCK3]] (+0.72, fdr 7e-06), [[MIR325HG]] (+0.71, fdr 7e-06).
> It is in [[Module 009]], a single-armed module (Neuronal System).
> Probable direction (from the cell lines, not proof of direct regulation): 16 arrows point to it, the strongest [[CALCA]] → it (grade B ⚠); 3 go from it, the strongest it → [[COL25A1]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 28 in all, 11 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 28 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 11 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6876.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **5.79×** | +18.0 | 0e+00 | 9/14 (HEC-1-A, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~2% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **3.92×** | +14.0 | 5e-42 | 11/15 (C32, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~1% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **4.41×** | +10.8 | 1e-24 | 1/3 (C32) | all doses, flat | cell-cycle shift (explains ~11% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **4.16×** | +9.9 | 4e-21 | 1/1 (SHP-77) | all doses, flat | cell-cycle shift (explains ~10% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **3.87×** | +9.1 | 1e-17 | 0/2 | all doses, flat | cell-cycle shift (explains ~8% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **2.37×** | +8.8 | 1e-16 | 13/22 (NCI-H1573, NCI-H460, …) | rises with dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **3.20×** | +8.4 | 3e-15 | 7/19 (NCI-H460, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **2.29×** | +6.0 | 1e-07 | 0/5 | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~5% here) |
| [[Auranofin (drug)]] 5 µM |  | **2.29×** | +6.0 | 1e-07 | 3/11 (HOP62, NCI-H460, …) | top dose only |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.09×** | +5.3 | 5e-06 | 0/4 | top dose only | cell-cycle shift (explains ~12% here) |
| [[Panobinostat (drug)]] 5 µM |  | **1.93×** | +4.8 | 1e-04 | 10/22 (NCI-H1573, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.88×** | +4.6 | 2e-04 | 6/12 (NCI-H1573, SK-MEL-2, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[AZD2858 (drug)]] 0.5 µM | ⚠ toxic | **2.37×** | +4.4 | 4e-04 | 0/2 | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.86×** | +4.3 | 6e-04 | 1/11 (NCI-H460) | rises with dose | cell-cycle shift (explains ~11% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.81×** | +4.3 | 7e-04 | 3/11 (C32, A-172, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 5 µM |  | **1.50×** | +4.1 | 0.001 | 1/22 (SHP-77) | top dose only | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Saquinavir (drug)]] 0.5 µM |  | **1.69×** | +3.8 | 0.005 | 1/7 (NCI-H1573) | two highest doses |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.59×** | +3.2 | 0.039 | 0/7 | inconsistent across doses | cell-cycle shift (explains ~15% here) |
| [[Isocorydine (drug)]] 0.5 µM |  | **1.55×** | +3.2 | 0.039 | 1/8 (HEC-1-A) | inconsistent across doses |  |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.55×** | +3.2 | 0.039 | 7/18 (NCI-H1573, SK-MEL-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here) |
| [[XRK3F2 (drug)]] 0.5 µM |  | **1.84×** | +3.2 | 0.039 | 0/3 | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 2 in all, none with an alert. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 6876.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Anethole trithione (drug)]] 0.5 µM |  | 0.648× | -3.2 | 0.35 | 0/24 | inconsistent across doses |  |
| [[Fusidic acid (drug)]] 5 µM |  | 0.745× | -3.1 | 0.35 | 3/23 (HEC-1-A, KATO III, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.21 per unit of S-phase module lfc, +0.01 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6876. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H1573 (line)]] | alt | 1.35 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 16.2× (z +8.8) | — |
| [[A-172 (line)]] | wt | 0.654 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 0.652 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 0.542 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 0.538 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 0.877 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 0.569 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 0.660 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 3.44 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 6.20 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 0.688 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 2.05 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 0.621 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 0.671 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 0.713 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 0.716 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 0.623 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 0.641 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 7.09 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 0.551 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 0.628 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 0.970 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 0.533 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 0.593 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 0.607 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 0.659 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 0.555 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.500 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 0.562 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 0.799 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 4.12 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 0.649 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 0.468 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 0.640 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 4.48 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 1.26 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 0.498 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 0.553 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 0.587 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 0.724 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 77.8 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 6.46 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 0.570 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 0.578 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 0.999 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 0.708 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 0.805 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 0.579 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 0.677 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 0.566 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6876), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GLRA3]] | +0.75 | +0.65 / +0.76 | both halves | 7e-06 | **novel candidate** |
| [[SPOCK3]] | +0.72 | +0.73 / +0.63 | both halves | 7e-06 | **novel candidate** |
| [[MIR325HG]] | +0.71 | +0.64 / +0.74 | both halves | 7e-06 |  |
| [[COL21A1]] | +0.71 | +0.71 / +0.69 | both halves | 7e-06 |  |
| [[NRXN1]] | +0.71 | +0.72 / +0.74 | both halves | 7e-06 | **novel candidate** |
| [[NELL1]] | +0.70 | +0.66 / +0.64 | both halves | 7e-06 |  |
| [[RALYL]] | +0.70 | +0.70 / +0.72 | both halves | 7e-06 |  |
| [[CNBD1]] | +0.70 | +0.64 / +0.74 | both halves | 7e-06 |  |
| [[MYT1L]] | +0.69 | +0.70 / +0.67 | both halves | 7e-06 |  |
| [[ABCA13]] | +0.68 | +0.73 / +0.58 | both halves | 7e-06 | STRING 417 |
| [[GRIA1]] | +0.68 | +0.62 / +0.69 | both halves | 7e-06 |  |
| [[LINC02306]] | +0.67 | +0.72 / +0.65 | both halves | 7e-06 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*16 arrows, 16 of them with an alert ⚠; grade A 0, B 16, C 0. Shown: the 12 strongest; 4 more arrows (4 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CALCA]] | B | CALCA activity raises UNC80's level | lines that do not express CALCA (45) vs lines expressing it (5) | 3.21× lower at baseline in the lines without CALCA | 0.010 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: SYT4, CGA, RIT2 |
| [[AK4P3]] | B | AK4P3 activity raises UNC80's level | lines that do not express AK4P3 (36) vs lines expressing it (14) | 2.21× lower at baseline in the lines without AK4P3 | 0.016 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: APOA1, ENSG00000232252, TF |
| [[SYT4]] | B | SYT4 activity raises UNC80's level | lines that do not express SYT4 (44) vs lines expressing it (6) | 2.89× lower at baseline in the lines without SYT4 | 0.019 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: CALCA, ENSG00000232252, CGA |
| [[RIT2]] | B | RIT2 activity raises UNC80's level | lines that do not express RIT2 (44) vs lines expressing it (6) | 2.58× lower at baseline in the lines without RIT2 | 0.020 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: CALCA, KCNB2, SYT4 |
| [[KCNB2]] | B | KCNB2 activity raises UNC80's level | lines that do not express KCNB2 (43) vs lines expressing it (7) | 2.20× lower at baseline in the lines without KCNB2 | 0.025 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: RIT2, CALCA, SRRM4; maybe low, not absent |
| [[SRRM4]] | B | SRRM4 activity raises UNC80's level | lines that do not express SRRM4 (41) vs lines expressing it (9) | 2.28× lower at baseline in the lines without SRRM4 | 0.035 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: KCNB2, RIT2, CALCA; maybe low, not absent |
| [[SPINK5]] | B | SPINK5 activity raises UNC80's level | lines that do not express SPINK5 (35) vs lines expressing it (15) | 1.87× lower at baseline in the lines without SPINK5 | 0.035 | ⚠ within organs, on part of the lines; also absent: TFF2, ST6GALNAC1, ENSG00000248588 |
| [[CGA]] | B | CGA activity raises UNC80's level | lines that do not express CGA (44) vs lines expressing it (6) | 2.75× lower at baseline in the lines without CGA | 0.043 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: CALCA, SYT4, RIT2 |
| [[TOP2A]] | B | TOP2A activity lowers UNC80's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 5.9% of all compounds | 0.044 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[AGMO]] | B | AGMO activity raises UNC80's level | lines that do not express AGMO (30) vs lines expressing it (20) | 1.74× lower at baseline in the lines without AGMO | 0.055 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000275016, SCG3, ENSG00000258657 |
| [[ASCL1]] | B | ASCL1 activity raises UNC80's level | lines that do not express ASCL1 (41) vs lines expressing it (9) | 2.47× lower at baseline in the lines without ASCL1 | 0.057 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: ENSG00000232252, ENSG00000275016, SYT4 |
| [[DGKB]] | B | DGKB activity raises UNC80's level | lines that do not express DGKB (23) vs lines expressing it (27) | 1.64× lower at baseline in the lines without DGKB | 0.060 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: ENSG00000287862, MIR2052HG, RMST; maybe low, not absent |

### Downstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[COL25A1]] | B | UNC80 activity raises COL25A1's level | lines that do not express UNC80 (16) vs lines expressing it (34) | 1.70× lower at baseline in the lines without UNC80 | 0.050 | ⚠ within organs, on part of the lines; also absent: PPFIA2, GAS7, COP1-DT; maybe low, not absent |
| [[PLCL1]] | B | UNC80 activity raises PLCL1's level | lines that do not express UNC80 (16) vs lines expressing it (34) | 1.56× lower at baseline in the lines without UNC80 | 0.081 | ⚠ within organs, on part of the lines; also absent: PPFIA2, GAS7, COP1-DT; maybe low, not absent |
| [[AK4P3]] | B | UNC80 activity raises AK4P3's level | lines that do not express UNC80 (16) vs lines expressing it (34) | 2.92× lower at baseline in the lines without UNC80 | 0.090 | ⚠ within organs, on part of the lines; also absent: PPFIA2, GAS7, COP1-DT; maybe low, not absent |

## Where it sits

- **Module**: [[Module 009]] — Neuronal System; 222 genes; every member is in the + arm (projection on the module's main direction 0.653). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (24.6, 30.4); signed map (34.5, 17.8). **Vector** length 28.7, 5.08% of its response variance represented; |z| ≥ 3 in 479 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *Neuronal System* (reactome, mean cos +0.52 to 15).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM |  | +4.0 | +14.0 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +3.7 | +9.9 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +3.5 | +10.8 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +3.3 | +18.0 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +3.2 | +9.1 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +3.2 | +8.8 |
|  | [[Auranofin (drug)]] 5 µM |  | +1.6 | +6.0 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +1.4 | +3.1 |
|  | [[Verteporfin (drug)]] 5 µM |  | +0.9 | +1.2 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +0.9 | +1.3 |
| fall | [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | -1.1 | -1.7 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -0.9 | -2.1 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -0.9 | -2.1 |
|  | [[Fenofibrate (drug)]] 0.05 µM |  | -0.8 | -2.8 |
|  | [[Mebendazole (drug)]] 5 µM |  | -0.7 | -1.4 |
|  | [[(S)-Crizotinib (drug)]] 0.05 µM |  | -0.7 | -2.4 |

## What is on record

|  |  |
|---|---|
| Name | unc-80 subunit of NALCN channel complex |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 2q34 — chr2:209,771,569-209,999,300 (+) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ33496, KIAA1843, UNC-80; previously C2orf21 |
| Gene groups (HGNC) | NALCN channel complex subunits |
| Reactome | 3 pathways, smallest: Stimuli-sensing channels; Ion channel transport; Transport of small molecules |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8N2C7](https://www.uniprot.org/uniprotkb/Q8N2C7) (Protein unc-80 homolog):

> Auxilary subunit of the NALCN channelosome complex, which regulates the resting membrane potential by depolarizing sodium leak currents. The NALCN channelosome complex is a voltage-gated ion channel responsible for the resting Na(+) permeability that controls neuronal excitability. The NALCN channelosome is constitutively active and conducts monovalent cations but is blocked by physiological concentrations of extracellular divalent cations. Activated by neuropeptides substance P, neurotensin, …

**Summary**, from NCBI Gene [285175](https://www.ncbi.nlm.nih.gov/gene/285175):

> The protein encoded by this gene is a component of a voltage-independent 'leak' ion-channel complex, in which it performs essential functions, such as serving as a bridge between two other components (sodium leak channel non-selective and UNC79) and as a scaffold for Src kinases. Leak channels play an importnat role in establishment and maintenance of resting membrane potentials in neurons. Mutations in this gene are associated with congenital infantile encephalopathy, intellectual disability …

**Accessions** — [HGNC:26582](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:26582) · Entrez [285175](https://www.ncbi.nlm.nih.gov/gene/285175) · UniProt [Q8N2C7](https://www.uniprot.org/uniprotkb/Q8N2C7) · Ensembl [ENSG00000144406](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000144406)

## Data

Gene col 6876: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6876); `tables/drug_effects.parquet` (30 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6876, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6876]; `tensor/DDL_lfc|DDL_z.npy` [6876]; `embed/gene_vectors.npy` [6876]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6876 or target_col == 6876). Every well: [[UNC80 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/UNC80.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
