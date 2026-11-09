---
symbol: "CHDH"
type: "gene"
col: 298
ensembl_id: "ENSG00000016391"
name: "choline dehydrogenase"
location: "3p21.1"
module: 27
arm: "+"
pooled_cpm: 4.3
n_lines_expressing: 28
n_dd_up: 17
n_dd_down: 9
n_dd_up_clean: 9
n_dd_down_clean: 9
in_vector_space: true
direction_upstream: 19
direction_downstream: 12
tags: ["gene", "module/027"]
generated_by: "tahoemap"
---

# CHDH

*choline dehydrogenase* — 3p21.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 17 drug-doses (8 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 4.36× (z +15.6, q 0e+00, up in 3 of 6 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Homoharringtonine (drug)]] 5 µM: 1.66× (z +7.9, q 3e-13, up in 4 of 19 measured lines).
> Pooled over the cell lines (median), lowered significantly by 9 drug-doses (none with an alert); the strongest is [[Artesunate (drug)]] 5 µM: 0.729× (z -5.0, q 3e-04, down in 10 of 24 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[B3GAT1-DT]] (+0.79, fdr 7e-06), [[MYB]] (+0.77, fdr 7e-06), [[KCNE3]] (+0.75, fdr 7e-06); moves opposite to [[SH3BGRL3]] (-0.52, fdr 3e-05).
> It is in [[Module 027]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 19 arrows point to it, the strongest [[APCDD1]] → it (grade B ⚠); 12 go from it, the strongest it → [[FAAH]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 18 in all, 9 with an alert ⚠. 17 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 298.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **4.36×** | +15.6 | 0e+00 | 3/6 (HT-29, HepG2/C3A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **3.12×** | +11.6 | 1e-28 | 6/9 (LS 180, SW1417, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.81×** | +11.4 | 9e-28 | 7/13 (NCI-H2347, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.66×** | +7.9 | 3e-13 | 4/19 (BT-474, NCI-H460, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.71×** | +5.9 | 4e-07 | 5/14 (SW1417, PANC-1, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.69×** | +5.6 | 2e-06 | 3/15 (A-427, SW1417, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.35×** | +4.7 | 2e-04 | 3/20 (BT-474, NCI-H2347, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.51×** | +4.5 | 5e-04 | 2/22 (HT-29, BT-474) | top dose only |  |
| [[Simotinib (drug)]] 5 µM | ⚠ toxic | **1.50×** | +4.3 | 0.001 | 0/19 | top dose only |  |
| [[Radotinib (drug)]] 0.5 µM |  | **1.44×** | +4.0 | 0.004 | 1/21 (KATO III) | inconsistent across doses |  |
| [[Selinexor (drug)]] 5 µM |  | **1.28×** | +3.8 | 0.006 | 4/24 (KATO III, RKO, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.10× | +3.8 | 0.007 | 6/25 (PANC-1, NCI-H23, …) | inconsistent across doses |  |
| [[Entrectinib (drug)]] 5 µM |  | **1.40×** | +3.7 | 0.009 | 2/23 (LS 180, KATO III) | top dose only |  |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **1.88×** | +3.6 | 0.012 | 0/6 | top dose only | noisy plate (z scaled) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.38×** | +3.4 | 0.024 | 3/19 (CFPAC-1, HT-29, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Sulfatinib (drug)]] 5 µM |  | **1.34×** | +3.1 | 0.073 | 2/23 (KATO III, NCI-H2030) | top dose only |  |
| [[NG25 (drug)]] 5 µM |  | **1.68×** | +3.0 | 0.089 | 4/19 (COLO 205, SW480, …) | top dose only | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Omeprazole (drug)]] 0.5 µM |  | **1.31×** | +3.0 | 0.096 | 2/22 (HEC-1-A, SW1417) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, none with an alert. 9 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 298.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Artesunate (drug)]] 5 µM |  | **0.729×** | -5.0 | 3e-04 | 10/24 (SW480, LS 180, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Artesunate (drug)]] 0.5 µM |  | **0.648×** | -4.8 | 3e-04 | 5/24 (NCI-H23, KATO III, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.649×** | -4.8 | 3e-04 | 14/22 (SW480, LS 180, …) | two highest doses | cell-cycle shift (explains ~1% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.652×** | -4.7 | 3e-04 | 12/23 (SW480, HepG2/C3A, …) | inconsistent across doses | cell-cycle shift (explains ~1% here); position effect removed |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.673×** | -4.4 | 0.001 | 7/22 (CFPAC-1, SW480, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); position effect removed |
| [[Belinostat (drug)]] 5 µM |  | **0.729×** | -3.5 | 0.043 | 12/23 (SW480, COLO 205, …) | top dose only | cell-cycle shift (explains ~1% here) |
| [[Naproxen (drug)]] 5 µM |  | **0.726×** | -3.4 | 0.049 | 4/23 (HCT15, SW1417, …) | rises with dose | position effect removed |
| [[Dihydroartemisinin (drug)]] 0.5 µM |  | **0.746×** | -3.2 | 0.081 | 4/23 (SW48, KATO III, …) | two highest doses |  |
| [[Pravastatin (sodium) (drug)]] 5 µM |  | **0.740×** | -3.2 | 0.081 | 2/23 (RKO, NCI-H460) | rises with dose | plate-row cell shift |
| [[Hydroxyurea (drug)]] 5 µM |  | 0.754× | -3.0 | 0.14 | 5/23 (NCI-H2030, SW480, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.04 per unit of S-phase module lfc, +0.01 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 298. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 17.5 | 0 | 8 (3 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0556× (z -19.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~6% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.0610× (z -18.7) |
| [[COLO 205 (line)]] | alt | 12.0 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0419× (z -11.9) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.114× (z -11.6) |
| [[HepG2_C3A (line)]] | wt | 25.9 | 0 | 2 | — | [[Auranofin (drug)]] 5 µM 0.145× (z -9.6) |
| [[PANC-1 (line)]] | alt | 8.48 | 0 | 2 (2 ⚠) | — | [[Bortezomib (drug)]] 0.05 µM 0.138× (z -12.0) ⚠ cell-cycle shift, explains ~0% of this change |
| [[A-427 (line)]] | wt | 8.17 | 0 | 1 | — | [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM 0.0937× (z -10.9) |
| [[HT-29 (line)]] | alt | 7.05 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0550× (z -12.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~6% of this change |
| [[LS 180 (line)]] | wt | 11.0 | 0 | 1 | — | [[Panobinostat (drug)]] 0.5 µM 0.115× (z -9.3) |
| [[A-172 (line)]] | wt | 0.669 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 0.386 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 1.07 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 1.76 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 0.525 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 8.27 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 0.939 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 0.593 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 1.89 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 1.51 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 0.507 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 5.16 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 5.98 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 0.496 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 0.383 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 0.458 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 0.627 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 0.566 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 8.71 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 9.00 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 0.555 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 3.53 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 0.822 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 1.14 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 1.46 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 3.70 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 1.99 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 1.92 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 1.38 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 5.15 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 1.32 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 1.69 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 4.52 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 0.528 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 1.01 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 0.740 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 0.677 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 0.802 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 0.961 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 0.540 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 0.657 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 8.24 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 7.35 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 298), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*99 of its nearest partners move with it, 2 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[B3GAT1-DT]] | +0.79 | +0.77 / +0.65 | both halves | 7e-06 | **novel candidate** |
| [[MYB]] | +0.77 | +0.77 / +0.73 | both halves | 7e-06 | **novel candidate** |
| [[KCNE3]] | +0.75 | +0.77 / +0.64 | both halves | 7e-06 |  |
| [[LINC02058]] | +0.72 | +0.69 / +0.62 | both halves | 7e-06 |  |
| [[LINC01622]] | +0.72 | +0.76 / +0.60 | both halves | 7e-06 | **novel candidate** |
| [[SMOC2]] | +0.71 | +0.64 / +0.68 | both halves | 7e-06 | **novel candidate** |
| [[AXIN2]] | +0.70 | +0.76 / +0.54 | both halves | 1e-05 |  |
| [[IL17RB]] | +0.70 | +0.64 / +0.69 | both halves | 7e-06 | STRING 853; ⚠ same locus (0.1 kb: neighbours can correlate without regulation) |
| [[CLRN3]] | +0.69 | +0.72 / +0.56 | both halves | 1e-05 |  |
| [[VSNL1]] | +0.69 | +0.71 / +0.57 | both halves | 1e-05 |  |
| [[APCDD1]] | +0.68 | +0.70 / +0.54 | both halves | 1e-05 |  |
| [[VIL1]] | +0.67 | +0.66 / +0.57 | both halves | 9e-06 |  |
| [[NOTUM]] | +0.67 | +0.67 / +0.59 | both halves | 7e-06 |  |

## Genes that move opposite

*1 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SH3BGRL3]] | -0.52 | -0.51 / -0.45 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*19 arrows, 19 of them with an alert ⚠; grade A 0, B 7, C 12. Shown: the 12 strongest; 7 more arrows (7 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[APCDD1]] | B | APCDD1 activity raises CHDH's level | lines that do not express APCDD1 (40) vs lines expressing it (10) | 2.66× lower at baseline in the lines without APCDD1 | 0.040 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: APOB, MUC6, ENSG00000285751 |
| [[LINC01748]] | B | LINC01748 activity raises CHDH's level | lines that do not express LINC01748 (34) vs lines expressing it (16) | 1.99× lower at baseline in the lines without LINC01748 | 0.046 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: CALB1, ATP10B, CLRN3 |
| [[MYB]] | B | MYB activity raises CHDH's level | lines that do not express MYB (24) vs lines expressing it (26) | 2.16× lower at baseline in the lines without MYB | 0.069 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: NOS3, CKMT1B, LINC01748 |
| [[BANK1]] | B | BANK1 activity raises CHDH's level | lines that do not express BANK1 (12) vs lines expressing it (38) | 1.74× lower at baseline in the lines without BANK1 | 0.083 | ⚠ within organs, on part of the lines; maybe low, not absent |
| [[IGFL4]] | B | IGFL4 activity raises CHDH's level | lines that do not express IGFL4 (25) vs lines expressing it (25) | 2.18× lower at baseline in the lines without IGFL4 | 0.089 | ⚠ within organs, on part of the lines; also absent: YBX2, FGF9, KLRK1; maybe low, not absent |
| [[HDAC6]] | B | HDAC6 activity raises CHDH's level | compounds that target HDAC6: 2 of 2 lower it (Belinostat, Panobinostat) | 100% of the class's compounds vs 2.0% of all compounds | 0.095 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[TFF3]] | B | TFF3 activity raises CHDH's level | lines that do not express TFF3 (38) vs lines expressing it (12) | 2.58× lower at baseline in the lines without TFF3 | 0.098 | ⚠ within organs, on part of the lines; also absent: CEACAM5, MUC17, AGR3 |
| [[IL17RB]] | C | IL17RB activity raises CHDH's level | lines that do not express IL17RB (22) vs lines expressing it (28) | 3.42× lower at baseline in the lines without IL17RB | 0.002 | ⚠ within organs, on part of the lines; also absent: CHDH, ESRP2, PRSS22; maybe low, not absent; co-absent with the target |
| [[YBX2]] | C | YBX2 activity raises CHDH's level | lines that do not express YBX2 (28) vs lines expressing it (22) | 2.38× lower at baseline in the lines without YBX2 | 0.011 | ⚠ within organs, on part of the lines; also absent: CKMT1A, PRR15L, FGF9; co-absent with the target |
| [[ESRP2]] | C | ESRP2 activity raises CHDH's level | lines that do not express ESRP2 (26) vs lines expressing it (24) | 3.38× lower at baseline in the lines without ESRP2 | 0.020 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: PRSS22, MARVELD3, CRB3; co-absent with the target |
| [[LINC02331]] | C | LINC02331 activity raises CHDH's level | lines that do not express LINC02331 (30) vs lines expressing it (20) | 3.09× lower at baseline in the lines without LINC02331 | 0.037 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: KDF1, EPS8L3, LCN2; co-absent with the target |
| [[FGF20]] | C | FGF20 activity raises CHDH's level | lines that do not express FGF20 (41) vs lines expressing it (9) | 2.23× lower at baseline in the lines without FGF20 | 0.050 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: GPR15, HEPHL1, GCG; co-absent with the target |

### Downstream of this gene

*12 arrows, 12 of them with an alert ⚠; grade A 0, B 2, C 10.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[FAAH]] | B | CHDH activity raises FAAH's level | lines that do not express CHDH (22) vs lines expressing it (28) | 1.80× lower at baseline in the lines without CHDH | 0.036 | ⚠ within organs, on part of the lines; also absent: IL17RB, ESRP2, PRSS22 |
| [[ZNRF3]] | B | CHDH activity raises ZNRF3's level | lines that do not express CHDH (22) vs lines expressing it (28) | 2.16× lower at baseline in the lines without CHDH | 0.097 | ⚠ within organs, on part of the lines; also absent: IL17RB, ESRP2, PRSS22 |
| [[IL17RB]] | C | CHDH activity raises IL17RB's level | lines that do not express CHDH (22) vs lines expressing it (28) | 3.58× lower at baseline in the lines without CHDH | 0.004 | ⚠ within organs, on part of the lines; also absent: IL17RB, ESRP2, PRSS22; co-absent with the target |
| [[HSD11B2]] | C | CHDH activity raises HSD11B2's level | lines that do not express CHDH (22) vs lines expressing it (28) | 2.95× lower at baseline in the lines without CHDH | 0.032 | ⚠ within organs, on part of the lines; also absent: IL17RB, ESRP2, PRSS22; co-absent with the target |
| [[ESRP2]] | C | CHDH activity raises ESRP2's level | lines that do not express CHDH (22) vs lines expressing it (28) | 3.76× lower at baseline in the lines without CHDH | 0.035 | ⚠ within organs, on part of the lines; also absent: IL17RB, ESRP2, PRSS22; co-absent with the target |
| [[SMPDL3B]] | C | CHDH activity raises SMPDL3B's level | lines that do not express CHDH (22) vs lines expressing it (28) | 2.72× lower at baseline in the lines without CHDH | 0.038 | ⚠ within organs, on part of the lines; also absent: IL17RB, ESRP2, PRSS22; co-absent with the target |
| [[FGD3]] | C | CHDH activity raises FGD3's level | lines that do not express CHDH (22) vs lines expressing it (28) | 2.18× lower at baseline in the lines without CHDH | 0.056 | ⚠ within organs, on part of the lines; also absent: IL17RB, ESRP2, PRSS22; co-absent with the target |
| [[KLK6]] | C | CHDH activity raises KLK6's level | lines that do not express CHDH (22) vs lines expressing it (28) | 3.61× lower at baseline in the lines without CHDH | 0.060 | ⚠ within organs, on part of the lines; also absent: IL17RB, ESRP2, PRSS22; co-absent with the target |
| [[YBX2]] | C | CHDH activity raises YBX2's level | lines that do not express CHDH (22) vs lines expressing it (28) | 2.27× lower at baseline in the lines without CHDH | 0.064 | ⚠ within organs, on part of the lines; also absent: IL17RB, ESRP2, PRSS22; co-absent with the target |
| [[NMNAT3]] | C | CHDH activity raises NMNAT3's level | lines that do not express CHDH (22) vs lines expressing it (28) | 2.66× lower at baseline in the lines without CHDH | 0.089 | ⚠ within organs, on part of the lines; also absent: IL17RB, ESRP2, PRSS22; co-absent with the target |
| [[LINC02331]] | C | CHDH activity raises LINC02331's level | lines that do not express CHDH (22) vs lines expressing it (28) | 2.25× lower at baseline in the lines without CHDH | 0.094 | ⚠ within organs, on part of the lines; also absent: IL17RB, ESRP2, PRSS22; co-absent with the target |
| [[RNF43]] | C | CHDH activity raises RNF43's level | lines that do not express CHDH (22) vs lines expressing it (28) | 4.21× lower at baseline in the lines without CHDH | 0.097 | ⚠ within organs, on part of the lines; also absent: IL17RB, ESRP2, PRSS22; co-absent with the target |

## Where it sits

- **Module**: [[Module 027]]; 155 genes; every member is in the + arm (projection on the module's main direction 0.763). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.24; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (24.8, 45.6); signed map (62.2, 14.0). **Vector** length 58.1, 14.9% of its response variance represented; |z| ≥ 3 in 515 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +3.7 | +15.6 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +3.7 | +11.6 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +3.0 | +11.4 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | +2.6 | +3.4 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +2.3 | +7.9 |
|  | [[Ponatinib (drug)]] 5 µM |  | +1.7 | +2.7 |
|  | [[Ponatinib (drug)]] 0.5 µM |  | +1.4 | +2.5 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +1.2 | +2.8 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +1.2 | +2.8 |
|  | [[Radotinib (drug)]] 5 µM |  | +1.2 | +0.8 |
| fall | [[5-Azacytidine (drug)]] 5 µM |  | -1.6 | -1.1 |
|  | [[Artesunate (drug)]] 5 µM |  | -1.4 | -5.0 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | -1.2 | -4.7 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -1.1 | -4.8 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -0.9 | -0.4 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -0.9 | -2.7 |
|  | [[Dihydroartemisinin (drug)]] 5 µM |  | -0.8 | -2.2 |
|  | [[GSK1059615 (drug)]] 5 µM |  | -0.8 | -1.1 |

## What is on record

|  |  |
|---|---|
| Name | choline dehydrogenase |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 3p21.1 — chr3:53,812,335-53,846,419 (-) |
| Ensembl biotype | protein_coding |
| Gene groups (HGNC) | Flavoproteins; Oxidoreductases |
| Reactome | 2 pathways, smallest: Choline catabolism; Metabolism of amino acids and derivatives |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8NE62](https://www.uniprot.org/uniprotkb/Q8NE62) (Choline dehydrogenase, mitochondrial):

> Catalyzes the dehydrogenation of choline to betaine aldehyde in the mitochondria (By similarity). Involved in mitochondrial autophagy after mitochondrial damage.

**Summary**, from NCBI Gene [55349](https://www.ncbi.nlm.nih.gov/gene/55349):

> The protein encoded by this gene is a choline dehydrogenase that localizes to the mitochondrion. Variations in this gene can affect susceptibility to choline deficiency. A few transcript variants have been found for this gene, but the full-length nature of only one has been characterized to date. [provided by RefSeq, Dec 2010]

**Accessions** — [HGNC:24288](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:24288) · Entrez [55349](https://www.ncbi.nlm.nih.gov/gene/55349) · UniProt [Q8NE62](https://www.uniprot.org/uniprotkb/Q8NE62) · Ensembl [ENSG00000016391](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000016391)

## Data

Gene col 298: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 298); `tables/drug_effects.parquet` (28 rows, flagged included); `relations/gene_relations.parquet` (col_a == 298, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 298]; `tensor/DDL_lfc|DDL_z.npy` [298]; `embed/gene_vectors.npy` [298]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 298 or target_col == 298). Every well: [[CHDH — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CHDH.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
