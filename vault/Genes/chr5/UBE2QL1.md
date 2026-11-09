---
symbol: "UBE2QL1"
type: "gene"
col: 13253
ensembl_id: "ENSG00000215218"
name: "ubiquitin conjugating enzyme E2 QL1"
location: "5p15.31"
module: 155
arm: "+"
pooled_cpm: 6.07
n_lines_expressing: 18
n_dd_up: 14
n_dd_down: 2
n_dd_up_clean: 7
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 1
direction_downstream: 2
tags: ["gene", "module/155"]
generated_by: "tahoemap"
---

# UBE2QL1

*ubiquitin conjugating enzyme E2 QL1* — 5p15.31

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 14 drug-doses (7 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 4.38× (z +11.3, q 7e-27, up in 0 of 5 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.92× (z +7.3, q 3e-11, up in 2 of 11 measured lines).
> Pooled over the cell lines (median), lowered significantly by 2 drug-doses (none with an alert); the strongest is [[Artesunate (drug)]] 0.5 µM: 0.545× (z -4.8, q 8e-04, down in 2 of 14 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 12 here, 4 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 5 lines (NCI-H23 0.0498×, SHP-77 0.135×, A-172 0.225×, BT-474 0.0879×, …; ⚠ cell-cycle shift, explains ~0% of this change); [[Auranofin (drug)]] 5 µM in 3 lines (NCI-H23 0.0561×, SHP-77 0.152×, BT-474 0.0516×); [[Ouabain (Octahydrate) (drug)]] 5 µM in 2 lines (NCI-H23 0.0730×, SHP-77 0.222×); [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM in 1 line (A-172 0.159×).
> Its strongest partners by |cos| (98 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[C2CD4A]] (+0.70, fdr 7e-06), [[RET]] (+0.62, fdr 2e-05), [[CES1]] (+0.60, fdr 1e-05).
> It is in [[Module 155]], a single-armed module (MyD88 deficiency (TLR2/4)).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[PDE10A]] → it (grade C ⚠); 2 go from it, the strongest it → [[PDE10A]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 7 with an alert ⚠. 14 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 13253.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **4.38×** | +11.3 | 7e-27 | 0/5 | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **3.31×** | +9.5 | 5e-19 | 1/8 (NCI-H460) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.96×** | +8.0 | 3e-13 | 0/7 | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.92×** | +7.3 | 3e-11 | 2/11 (NCI-H460, A549) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.61×** | +5.4 | 9e-06 | 5/14 (NCI-H460, NCI-H2030, …) | rises with dose |  |
| [[AZD2858 (drug)]] 0.5 µM | ⚠ toxic | **2.30×** | +4.7 | 2e-04 | 0/7 | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[XRK3F2 (drug)]] 0.5 µM |  | **1.99×** | +3.9 | 0.007 | 0/8 | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Oxaprozin (drug)]] 0.5 µM |  | **1.62×** | +3.8 | 0.009 | 1/13 (NCI-H2030) | inconsistent across doses |  |
| [[LY-2584702 (tosylate salt) (drug)]] 5 µM | ⚠ toxic | **2.43×** | +3.7 | 0.014 | 1/5 (HS-578T) | top dose only | noisy plate (z scaled) |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.81×** | +3.4 | 0.041 | 1/10 (NCI-H460) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Imiquimod (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.52×** | +3.3 | 0.041 | 2/11 (SNU-423, A-172) | top dose only |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.55×** | +3.3 | 0.041 | 0/9 | top dose only | cell-cycle shift (explains ~0% here) |
| [[Clobetasol propionate (drug)]] 0.5 µM |  | **1.50×** | +3.2 | 0.055 | 7/13 (RPMI-7951, HS-578T, …) | inconsistent across doses |  |
| [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | **1.49×** | +3.2 | 0.059 | 0/14 | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 4 in all, none with an alert. 2 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 13253.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 12 here, 4 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 5 lines (NCI-H23 0.0498×, SHP-77 0.135×, A-172 0.225×, BT-474 0.0879×, …; ⚠ cell-cycle shift, explains ~0% of this change); [[Auranofin (drug)]] 5 µM in 3 lines (NCI-H23 0.0561×, SHP-77 0.152×, BT-474 0.0516×); [[Ouabain (Octahydrate) (drug)]] 5 µM in 2 lines (NCI-H23 0.0730×, SHP-77 0.222×); [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM in 1 line (A-172 0.159×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Artesunate (drug)]] 0.5 µM |  | **0.545×** | -4.8 | 8e-04 | 2/14 (BT-474, CHP-212) | inconsistent across doses |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | **0.566×** | -4.2 | 0.008 | 3/14 (BT-474, SHP-77, …) | inconsistent across doses |  |
| [[Sapanisertib (drug)]] 5 µM |  | 0.469× | -3.1 | 0.31 | 0/15 | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Raltitrexed (drug)]] 0.5 µM |  | 0.681× | -3.1 | 0.32 | 4/12 (RPMI-7951, A-172, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.08 per unit of S-phase module lfc, +0.02 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 13253. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H23 (line)]] | alt | 40.9 | 0 | 9 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0498× (z -23.0) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.0561× (z -15.6) |
| [[SHP-77 (line)]] | alt | 157 | 0 | 9 (6 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.135× (z -17.6) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.188× (z -14.7) |
| [[BT-474 (line)]] | alt | 34.6 | 0 | 6 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0879× (z -11.8) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.0516× (z -10.2) |
| [[A-172 (line)]] | wt | 26.5 | 0 | 3 (2 ⚠) | — | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM 0.159× (z -15.5) |
| [[HS-578T (line)]] | alt | 9.85 | 0 | 2 (2 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.0835× (z -9.5) ⚠ toxic |
| [[A549 (line)]] | wt | 2.91 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0680× (z -10.7) ⚠ cell-cycle shift, explains ~0% of this change |
| [[A-427 (line)]] | wt | 0.936 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 0.450 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 1.29 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 0.602 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 1.07 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 0.515 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 0.456 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 15.9 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 0.575 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 2.82 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 0.572 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 0.556 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 0.559 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 0.966 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 0.517 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 0.690 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 0.723 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 1.42 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 0.512 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 0.479 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 0.712 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 0.488 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.550 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 0.593 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 0.460 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 2.13 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 7.04 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 0.398 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 4.14 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 8.30 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 1.10 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 0.434 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 0.462 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 0.539 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 4.68 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 0.488 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 1.68 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 4.34 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 3.96 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 1.61 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 3.09 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 0.540 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 0.736 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 0.759 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 13253), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 2 of them with an alert (⚠; 2 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[C2CD4A]] | +0.70 | +0.73 / +0.61 | both halves | 7e-06 | **novel candidate** |
| [[RET]] | +0.62 | +0.59 / +0.48 | both halves | 2e-05 |  |
| [[CES1]] | +0.60 | +0.56 / +0.66 | both halves | 1e-05 |  |
| [[S100A9]] | +0.57 | +0.58 / +0.55 | both halves | 1e-05 |  |
| [[S100A8]] | +0.57 | +0.55 / +0.63 | both halves | 1e-05 |  |
| [[LINC01440]] | +0.54 | +0.54 / +0.62 | both halves | 1e-05 |  |
| [[SRRM4]] | +0.54 | +0.46 / +0.56 | both halves | 3e-05 |  |
| [[LINC02197]] | +0.53 | +0.47 / +0.52 | both halves | 2e-05 |  |
| [[ADARB2]] | +0.51 | +0.47 / +0.48 | both halves | 2e-05 |  |
| [[SERPINB4]] | +0.50 | +0.56 / +0.42 | both halves | 4e-05 |  |
| [[CHST8]] | +0.50 | +0.37 / +0.49 | both halves | 9e-05 |  |
| [[SLC6A11]] | +0.50 | +0.50 / +0.34 | both halves | 1e-04 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PDE10A]] | C | PDE10A activity raises UBE2QL1's level | lines that do not express PDE10A (24) vs lines expressing it (26) | 2.97× lower at baseline in the lines without PDE10A | 0.029 | ⚠ within organs, on part of the lines; also absent: ZMAT4, UBE2QL1, C10orf90; co-absent with the target |

### Downstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 0, C 2.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PDE10A]] | C | UBE2QL1 activity raises PDE10A's level | lines that do not express UBE2QL1 (32) vs lines expressing it (18) | 4.64× lower at baseline in the lines without UBE2QL1 | 0.035 | ⚠ within organs, on part of the lines; also absent: ZMAT4, NCAM1, FENDRR; co-absent with the target |
| [[ADARB2]] | C | UBE2QL1 activity raises ADARB2's level | lines that do not express UBE2QL1 (32) vs lines expressing it (18) | 3.04× lower at baseline in the lines without UBE2QL1 | 0.078 | ⚠ within organs, on part of the lines; also absent: ZMAT4, NCAM1, FENDRR; co-absent with the target |

## Where it sits

- **Module**: [[Module 155]] — MyD88 deficiency (TLR2/4); 29 genes; every member is in the + arm (projection on the module's main direction 0.612). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.35; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (35.9, 48.0); signed map (54.6, 24.0). **Vector** length 54.4, 17.4% of its response variance represented; |z| ≥ 3 in 430 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *MyD88 deficiency (TLR2/4)* (reactome, mean cos +0.52 to 4); *IRAK4 deficiency (TLR2/4)* (reactome, mean cos +0.52 to 4); *Regulation of TLR by endogenous ligand* (reactome, mean cos +0.52 to 4).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +5.3 | +9.5 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +5.3 | +11.3 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +5.0 | +8.0 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +3.6 | +5.4 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +3.3 | +7.3 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.3 | -0.8 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.9 | +3.4 |
|  | [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | +1.7 | +3.2 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +1.4 | +3.9 |
| fall | [[Artesunate (drug)]] 0.5 µM |  | -1.8 | -4.8 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -1.6 | -4.2 |
|  | [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | -1.5 | -2.6 |
|  | [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift | -1.5 | -1.9 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -1.4 | -1.2 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -1.4 | -2.2 |
|  | [[Rutin (trihydrate) (drug)]] 0.05 µM |  | -1.3 | -1.5 |

## What is on record

|  |  |
|---|---|
| Name | ubiquitin conjugating enzyme E2 QL1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 5p15.31 — chr5:6,448,859-6,496,723 (+) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ25076 |
| Gene groups (HGNC) | Ubiquitin conjugating enzymes E2 |
| Matched by | ensembl_id |

**Function**, from UniProt [A1L167](https://www.uniprot.org/uniprotkb/A1L167) (Ubiquitin-conjugating enzyme E2Q-like protein 1):

> Probable E2 ubiquitin-protein ligase that catalyzes the covalent attachment of ubiquitin to target proteins. May facilitate the monoubiquitination and degradation of MTOR and CCNE1 through interaction with FBXW7.

**Summary**, from NCBI Gene [134111](https://www.ncbi.nlm.nih.gov/gene/134111):

> Enables ubiquitin conjugating enzyme activity. Predicted to be involved in protein polyubiquitination. Located in nucleoplasm. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:37269](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:37269) · Entrez [134111](https://www.ncbi.nlm.nih.gov/gene/134111) · UniProt [A1L167](https://www.uniprot.org/uniprotkb/A1L167) · Ensembl [ENSG00000215218](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000215218)

## Data

Gene col 13253: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 13253); `tables/drug_effects.parquet` (18 rows, flagged included); `relations/gene_relations.parquet` (col_a == 13253, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 13253]; `tensor/DDL_lfc|DDL_z.npy` [13253]; `embed/gene_vectors.npy` [13253]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 13253 or target_col == 13253). Every well: [[UBE2QL1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/UBE2QL1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
