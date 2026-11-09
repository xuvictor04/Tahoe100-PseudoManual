---
symbol: "GCNT3"
type: "gene"
col: 6386
ensembl_id: "ENSG00000140297"
name: "glucosaminyl (N-acetyl) transferase 3, mucin type"
location: "15q22.2"
module: 8
arm: "+"
pooled_cpm: 52.33
n_lines_expressing: 12
n_dd_up: 8
n_dd_down: 9
n_dd_up_clean: 4
n_dd_down_clean: 7
in_vector_space: true
direction_upstream: 138
direction_downstream: 186
tags: ["gene", "module/008"]
generated_by: "tahoemap"
---

# GCNT3

*glucosaminyl (N-acetyl) transferase 3, mucin type* — 15q22.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 8 drug-doses (4 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 2.14× (z +8.2, q 1e-13, up in 0 of 10 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Ixazomib citrate (drug)]] 0.5 µM: 1.52× (z +4.5, q 0.001, up in 4 of 10 measured lines).
> Pooled over the cell lines (median), lowered significantly by 9 drug-doses (2 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 0.5 µM: 0.591× (z -5.7, q 8e-06, down in 7 of 10 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[HEPH]] (+0.86, fdr 7e-06), [[NPSR1]] (+0.84, fdr 7e-06), [[MYO7B]] (+0.84, fdr 7e-06).
> It is in [[Module 008]], a single-armed module (Dectin-2 family).
> Probable direction (from the cell lines, not proof of direct regulation): 138 arrows point to it, the strongest [[LDLRAD4]] → it (grade B ⚠); 186 go from it, the strongest it → [[NOSTRIN]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 4 with an alert ⚠. 8 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6386.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.14×** | +8.2 | 1e-13 | 0/10 | all doses, flat | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.60×** | +4.9 | 3e-04 | 0/9 | all doses, flat | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.52×** | +4.5 | 0.001 | 4/10 (HepG2/C3A, A549, …) | two highest doses |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.56×** | +4.4 | 0.001 | 0/9 | all doses, flat | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.49×** | +4.0 | 0.005 | 2/10 (HepG2/C3A, A549) | inconsistent across doses | cell-cycle shift (explains ~13% here) |
| [[Budesonide (drug)]] 0.05 µM |  | **1.46×** | +4.0 | 0.005 | 0/10 | inconsistent across doses |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.41×** | +3.7 | 0.016 | 3/10 (HepG2/C3A, A549, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.38×** | +3.4 | 0.043 | 0/10 | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | 1.34× | +3.2 | 0.10 | 0/10 | inconsistent across doses |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | 1.35× | +3.1 | 0.11 | 0/10 | top dose only | cell-cycle shift (explains ~0% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 2 with an alert ⚠. 9 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 6386.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.591×** | -5.7 | 8e-06 | 7/10 (KATO III, AsPC-1, …) | two highest doses | cell-cycle shift (explains ~1% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.589×** | -5.5 | 1e-05 | 7/10 (AsPC-1, KATO III, …) | rises with dose | cell-cycle shift (explains ~12% here); composition shift |
| [[Panobinostat (drug)]] 5 µM |  | **0.629×** | -5.0 | 1e-04 | 9/10 (LoVo, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~25% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.638×** | -4.8 | 2e-04 | 7/10 (LoVo, HT-29, …) | rises with dose | cell-cycle shift (explains ~24% here); position effect removed |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.656×** | -4.5 | 7e-04 | 7/10 (LS 180, KATO III, …) | inconsistent across doses | cell-cycle shift (explains ~17% here) |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **0.674×** | -4.3 | 0.002 | 7/10 (LoVo, KATO III, …) | all doses, stronger at high dose |  |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **0.788×** | -3.6 | 0.024 | 7/10 (LoVo, KATO III, …) | two highest doses | composition shift |
| [[Brivudine (drug)]] 5 µM |  | **0.547×** | -3.4 | 0.048 | 7/10 (HT-29, LoVo, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Rutin (trihydrate) (drug)]] 0.05 µM |  | **0.728×** | -3.2 | 0.098 | 0/10 | inconsistent across doses |  |
| [[Anethole trithione (drug)]] 0.5 µM |  | 0.751× | -3.1 | 0.12 | 0/10 | inconsistent across doses |  |
| [[Artesunate (drug)]] 0.5 µM |  | 0.756× | -3.0 | 0.14 | 0/10 | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.19 per unit of S-phase module lfc, -0.06 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6386. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LoVo (line)]] | wt | 612 | 0 | 13 (9 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0859× (z -29.8) ⚠ cell-cycle shift, explains ~25% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.0510× (z -25.5) |
| [[KATO III (line)]] | alt | 161 | 0 | 12 (8 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0763× (z -29.1) ⚠ cell-cycle shift, explains ~25% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.0903× (z -19.2) |
| [[LS 180 (line)]] | wt | 121 | 0 | 11 (8 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.185× (z -19.2) ⚠ cell-cycle shift, explains ~25% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.0973× (z -18.8) |
| [[AsPC-1 (line)]] | alt | 190 | 0 | 10 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0537× (z -27.6) ⚠ cell-cycle shift, explains ~25% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.0648× (z -17.6) |
| [[HT-29 (line)]] | alt | 524 | 0 | 10 (7 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.0722× (z -23.6) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.0748× (z -16.5) |
| [[COLO 205 (line)]] | alt | 191 | 0 | 4 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.129× (z -12.7) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.196× (z -10.1) |
| [[SW1417 (line)]] | alt | 27.7 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.216× (z -12.1) ⚠ cell-cycle shift, explains ~25% of this change |
| [[CFPAC-1 (line)]] | alt | 32.6 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.288× (z -9.8) ⚠ cell-cycle shift, explains ~0% of this change |
| [[A-172 (line)]] | wt | 4.91 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 3.77 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 13.0 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 38.8 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 8.97 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 10.2 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 5.12 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 4.62 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 5.99 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 5.00 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 5.21 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 9.23 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 19.0 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 4.90 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 5.97 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 4.63 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 6.47 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 4.04 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 5.72 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 3.62 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 12.4 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 6.33 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 7.32 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 36.6 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 4.22 n.m. | — | — | — | — |
| [[NCI-H2347 (line)]] | alt | 6.82 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 4.88 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 50.2 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 5.75 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 4.94 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 3.71 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 4.89 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 4.80 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 4.68 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 4.55 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 5.10 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 5.72 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 9.29 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 5.59 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 5.60 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 6.10 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 4.33 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6386), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[HEPH]] | +0.86 | +0.86 / +0.81 | both halves | 7e-06 | **novel candidate** |
| [[NPSR1]] | +0.84 | +0.89 / +0.79 | both halves | 7e-06 | **novel candidate** |
| [[MYO7B]] | +0.84 | +0.80 / +0.82 | both halves | 7e-06 | **novel candidate** |
| [[CLIC5]] | +0.81 | +0.82 / +0.73 | both halves | 7e-06 | **novel candidate** |
| [[TPRXL]] | +0.80 | +0.82 / +0.68 | both halves | 7e-06 | **novel candidate** |
| [[SLC6A20]] | +0.80 | +0.82 / +0.71 | both halves | 7e-06 | **novel candidate** |
| [[TMPRSS2]] | +0.80 | +0.82 / +0.76 | both halves | 7e-06 | **novel candidate** |
| [[TC2N]] | +0.79 | +0.76 / +0.76 | both halves | 7e-06 | **novel candidate** |
| [[LGALS4]] | +0.78 | +0.84 / +0.69 | both halves | 7e-06 |  |
| [[LINC01559]] | +0.77 | +0.79 / +0.68 | both halves | 7e-06 | **novel candidate** |
| [[C6orf132]] | +0.77 | +0.76 / +0.74 | both halves | 7e-06 |  |
| [[MUC17]] | +0.77 | +0.74 / +0.77 | both halves | 7e-06 | pathway: O-linked glycosylation; STRING 571 |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*138 arrows, 138 of them with an alert ⚠; grade A 0, B 10, C 128. Shown: the 12 strongest; 126 more arrows (126 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[LDLRAD4]] | B | LDLRAD4 activity raises GCNT3's level | lines that do not express LDLRAD4 (23) vs lines expressing it (27) | 1.86× lower at baseline in the lines without LDLRAD4 | 0.056 | ⚠ within organs, on part of the lines; also absent: TTTY14, NLGN4X, ENSG00000260958 |
| [[HTR1D]] | B | HTR1D activity raises GCNT3's level | lines that do not express HTR1D (15) vs lines expressing it (35) | 2.48× lower at baseline in the lines without HTR1D | 0.057 | ⚠ within organs, on part of the lines; also absent: A4GALT, ZNF185, PAPSS2; maybe low, not absent |
| [[SHROOM3]] | B | SHROOM3 activity raises GCNT3's level | lines that do not express SHROOM3 (19) vs lines expressing it (31) | 3.14× lower at baseline in the lines without SHROOM3 | 0.057 | ⚠ within organs, on part of the lines; co-occurs with TERT; also absent: RHOV, ELF3, PLUT |
| [[NOSTRIN]] | B | NOSTRIN activity raises GCNT3's level | lines that do not express NOSTRIN (16) vs lines expressing it (34) | 2.54× lower at baseline in the lines without NOSTRIN | 0.067 | ⚠ within organs, on part of the lines; also absent: SLC9A2, SLPI, SULT2B1; maybe low, not absent |
| [[SPATA6L]] | B | SPATA6L activity raises GCNT3's level | lines that do not express SPATA6L (15) vs lines expressing it (35) | 2.73× lower at baseline in the lines without SPATA6L | 0.068 | ⚠ within organs, on part of the lines; also absent: RHOV, ANO9, ELF3; maybe low, not absent |
| [[PSMB5]] | B | PSMB5 activity lowers GCNT3's level | compounds that target PSMB5: 2 of 2 raise it (Bortezomib, Ixazomib / Ixazomib citrate) | 100% of the class's compounds vs 1.4% of all compounds | 0.071 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[EPS8L1]] | B | EPS8L1 activity raises GCNT3's level | lines that do not express EPS8L1 (14) vs lines expressing it (36) | 2.58× lower at baseline in the lines without EPS8L1 | 0.076 | ⚠ within organs, on part of the lines; also absent: KIAA0040, IL1RN, MBNL3; maybe low, not absent |
| [[FUT2]] | B | FUT2 activity raises GCNT3's level | lines that do not express FUT2 (12) vs lines expressing it (38) | 2.57× lower at baseline in the lines without FUT2 | 0.085 | ⚠ within organs, on part of the lines; also absent: EFNB2, SH3TC1, PTPRE; maybe low, not absent |
| [[HDAC6]] | B | HDAC6 activity raises GCNT3's level | compounds that target HDAC6: 2 of 2 lower it (Belinostat, Panobinostat) | 100% of the class's compounds vs 2.0% of all compounds | 0.095 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[SLC44A3-AS1]] | B | SLC44A3-AS1 activity raises GCNT3's level | lines that do not express SLC44A3-AS1 (13) vs lines expressing it (37) | 2.55× lower at baseline in the lines without SLC44A3-AS1 | 0.095 | ⚠ within organs, on part of the lines; also absent: SLC44A3, CRYBG2, ENSG00000287306; maybe low, not absent |
| [[TRIM31]] | C | TRIM31 activity raises GCNT3's level | lines that do not express TRIM31 (39) vs lines expressing it (11) | 15.17× lower at baseline in the lines without TRIM31 | 1e-05 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: MUC13, GCNT3, NPSR1; co-absent with the target |
| [[MUC13]] | C | MUC13 activity raises GCNT3's level | lines that do not express MUC13 (40) vs lines expressing it (10) | 16.35× lower at baseline in the lines without MUC13 | 2e-05 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: TRIM31, NPSR1, CDH17; co-absent with the target |

### Downstream of this gene

*186 arrows, 186 of them with an alert ⚠; grade A 0, B 43, C 143. Shown: the 12 strongest; 174 more arrows (174 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[NOSTRIN]] | B | GCNT3 activity raises NOSTRIN's level | lines that do not express GCNT3 (38) vs lines expressing it (12) | 4.28× lower at baseline in the lines without GCNT3 | 6e-04 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: TRIM31, LYZ, MUC13 |
| [[IL22RA1]] | B | GCNT3 activity raises IL22RA1's level | lines that do not express GCNT3 (38) vs lines expressing it (12) | 3.99× lower at baseline in the lines without GCNT3 | 0.002 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: TRIM31, LYZ, MUC13 |
| [[SLC37A1]] | B | GCNT3 activity raises SLC37A1's level | lines that do not express GCNT3 (38) vs lines expressing it (12) | 3.08× lower at baseline in the lines without GCNT3 | 0.003 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: TRIM31, LYZ, MUC13 |
| [[SDCBP2]] | B | GCNT3 activity raises SDCBP2's level | lines that do not express GCNT3 (38) vs lines expressing it (12) | 4.82× lower at baseline in the lines without GCNT3 | 0.003 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: TRIM31, LYZ, MUC13 |
| [[MUC12]] | B | GCNT3 activity raises MUC12's level | lines that do not express GCNT3 (38) vs lines expressing it (12) | 3.02× lower at baseline in the lines without GCNT3 | 0.003 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: TRIM31, LYZ, MUC13 |
| [[TNFRSF21]] | B | GCNT3 activity raises TNFRSF21's level | lines that do not express GCNT3 (38) vs lines expressing it (12) | 5.35× lower at baseline in the lines without GCNT3 | 0.003 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: TRIM31, LYZ, MUC13 |
| [[FUT2]] | B | GCNT3 activity raises FUT2's level | lines that do not express GCNT3 (38) vs lines expressing it (12) | 2.95× lower at baseline in the lines without GCNT3 | 0.004 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: TRIM31, LYZ, MUC13 |
| [[TOB1]] | B | GCNT3 activity raises TOB1's level | lines that do not express GCNT3 (38) vs lines expressing it (12) | 1.98× lower at baseline in the lines without GCNT3 | 0.005 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: TRIM31, LYZ, MUC13 |
| [[FAM83E]] | B | GCNT3 activity raises FAM83E's level | lines that do not express GCNT3 (38) vs lines expressing it (12) | 3.62× lower at baseline in the lines without GCNT3 | 0.007 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: TRIM31, LYZ, MUC13 |
| [[BCL2L15]] | B | GCNT3 activity raises BCL2L15's level | lines that do not express GCNT3 (38) vs lines expressing it (12) | 3.52× lower at baseline in the lines without GCNT3 | 0.008 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: TRIM31, LYZ, MUC13 |
| [[EPS8L1]] | B | GCNT3 activity raises EPS8L1's level | lines that do not express GCNT3 (38) vs lines expressing it (12) | 3.81× lower at baseline in the lines without GCNT3 | 0.008 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: TRIM31, LYZ, MUC13 |
| [[FZD5]] | B | GCNT3 activity raises FZD5's level | lines that do not express GCNT3 (38) vs lines expressing it (12) | 3.11× lower at baseline in the lines without GCNT3 | 0.008 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: TRIM31, LYZ, MUC13 |

## Where it sits

- **Module**: [[Module 008]] — Dectin-2 family; 228 genes; every member is in the + arm (projection on the module's main direction 0.748). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.23; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (20.5, 51.5); signed map (62.1, 6.2). **Vector** length 72.8, 37.5% of its response variance represented; |z| ≥ 3 in 373 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +2.8 | +8.2 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.6 | +0.7 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | +2.4 | +4.0 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +2.3 | +4.9 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +2.2 | +4.4 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +1.9 | +0.1 |
|  | [[Auranofin (drug)]] 5 µM |  | +1.8 | +1.8 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.2 | +1.9 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +1.2 | +4.5 |
| fall | [[BAY1125976 (drug)]] 5 µM |  | -1.5 | -2.2 |
|  | [[Sapanisertib (drug)]] 5 µM |  | -1.2 | -2.0 |
|  | [[Rutin (trihydrate) (drug)]] 0.05 µM |  | -1.2 | -3.2 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -1.1 | -1.9 |
|  | [[4EGI-1 (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.1 | -1.4 |
|  | [[Mebendazole (drug)]] 5 µM |  | -1.0 | -2.2 |

## What is on record

|  |  |
|---|---|
| Name | glucosaminyl (N-acetyl) transferase 3, mucin type |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 15q22.2 — chr15:59,594,875-59,640,239 (+) |
| Ensembl biotype | protein_coding |
| Also known as | C2GnT-M, C2/4GnT, C2GnT2 |
| Gene groups (HGNC) | Glucosaminyl (N-acetyl) transferases/xylosyltransferases |
| Reactome | 2 pathways, smallest: O-linked glycosylation of mucins; O-linked glycosylation |
| Matched by | ensembl_id |

**Function**, from UniProt [O95395](https://www.uniprot.org/uniprotkb/O95395) (Beta-1,3-galactosyl-O-glycosyl-glycoprotein beta-1,6-N-acetylglucosaminyltransferase 3):

> Glycosyltransferase that can synthesize all known mucin beta 6 N-acetylglucosaminides. Mediates core 2 and core 4 O-glycan branching, 2 important steps in mucin-type biosynthesis. Also has I-branching enzyme activity by converting linear into branched poly-N-acetyllactosaminoglycans, leading to introduce the blood group I antigen during embryonic development.

**Summary**, from NCBI Gene [9245](https://www.ncbi.nlm.nih.gov/gene/9245):

> This gene encodes a member of the N-acetylglucosaminyltransferase family. The encoded protein is a beta-6-N-acetylglucosamine-transferase that catalyzes the formation of core 2 and core 4 O-glycans on mucin-type glycoproteins.[provided by RefSeq, Apr 2009]

**Accessions** — [HGNC:4205](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:4205) · Entrez [9245](https://www.ncbi.nlm.nih.gov/gene/9245) · UniProt [O95395](https://www.uniprot.org/uniprotkb/O95395) · Ensembl [ENSG00000140297](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000140297)

## Data

Gene col 6386: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6386); `tables/drug_effects.parquet` (21 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6386, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6386]; `tensor/DDL_lfc|DDL_z.npy` [6386]; `embed/gene_vectors.npy` [6386]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6386 or target_col == 6386). Every well: [[GCNT3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/GCNT3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
