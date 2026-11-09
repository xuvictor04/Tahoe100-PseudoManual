---
symbol: "TSPAN8"
type: "gene"
col: 4799
ensembl_id: "ENSG00000127324"
name: "tetraspanin 8"
location: "12q21.1"
module: 44
arm: "+"
pooled_cpm: 31.96
n_lines_expressing: 16
n_dd_up: 25
n_dd_down: 8
n_dd_up_clean: 17
n_dd_down_clean: 5
in_vector_space: true
direction_upstream: 98
direction_downstream: 79
tags: ["gene", "module/044"]
generated_by: "tahoemap"
---

# TSPAN8

*tetraspanin 8* — 12q21.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 25 drug-doses (8 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 3.92× (z +19.9, q 0e+00, up in 6 of 14 measured lines).
> Pooled over the cell lines (median), lowered significantly by 8 drug-doses (3 with an alert ⚠); the strongest is [[Belinostat (drug)]] 5 µM: 0.663× (z -4.2, q 0.014, down in 12 of 14 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CFTR]] (+0.82, fdr 7e-06), [[ST6GALNAC1]] (+0.81, fdr 7e-06), [[CDH17]] (+0.81, fdr 7e-06).
> It is in [[Module 044]], a single-armed module (Defective GALNT12 causes CRCS1).
> Probable direction (from the cell lines, not proof of direct regulation): 98 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); 79 go from it, the strongest it → [[SLC37A1]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 25 in all, 8 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 25 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4799.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **3.92×** | +19.9 | 0e+00 | 6/14 (AsPC-1, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **6.00×** | +18.4 | 0e+00 | 9/13 (NCI-H460, AsPC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM |  | **2.84×** | +15.2 | 0e+00 | 3/14 (NCI-H1792, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~19% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **4.13×** | +14.1 | 1e-42 | 8/10 (NCI-H460, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.75×** | +9.6 | 6e-20 | 8/11 (NCI-H460, Hs 766T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.58×** | +6.7 | 2e-09 | 3/14 (SW48, SW1417, …) | top dose only |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.81×** | +5.9 | 4e-07 | 0/14 | top dose only | cell-cycle shift (explains ~0% here) |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.72×** | +5.6 | 1e-06 | 2/14 (NCI-H1792, SW48) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.69×** | +5.2 | 1e-05 | 0/14 | top dose only | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.55×** | +4.5 | 3e-04 | 4/14 (KATO III, NCI-H460, …) | top dose only | cell-cycle shift (explains ~10% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.52×** | +4.3 | 7e-04 | 0/14 | top dose only |  |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.75×** | +4.1 | 0.002 | 0/14 | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **2.09×** | +4.0 | 0.003 | 4/9 (AsPC-1, HT-29, …) | top dose only | noisy plate (z scaled) |
| [[Bimiralisib (drug)]] 0.5 µM |  | **1.61×** | +3.5 | 0.018 | 1/14 (AsPC-1) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Cobimetinib (drug)]] 5 µM |  | **1.42×** | +3.5 | 0.018 | 8/14 (LS 180, COLO 205, …) | inconsistent across doses |  |
| [[Methylprednisolone succinate (drug)]] 0.5 µM |  | **1.55×** | +3.2 | 0.036 | 0/14 | inconsistent across doses | low cells (technical?); noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.23×** | +3.1 | 0.057 | 2/14 (NCI-H1792, SHP-77) | top dose only |  |
| [[9-ING-41 (drug)]] 0.5 µM |  | **1.52×** | +3.1 | 0.057 | 0/14 | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Verteporfin (drug)]] 0.5 µM |  | **1.33×** | +2.9 | 0.083 | 0/14 | inconsistent across doses | position effect removed |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **1.34×** | +2.9 | 0.085 | 6/14 (COLO 205, LS 180, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 4 with an alert ⚠. 8 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 4799.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Belinostat (drug)]] 5 µM |  | **0.663×** | -4.2 | 0.014 | 12/14 (LoVo, LS 180, …) | top dose only | cell-cycle shift (explains ~21% here); position effect removed |
| [[5-Azacytidine (drug)]] 5 µM |  | **0.690×** | -3.8 | 0.032 | 7/14 (KATO III, NCI-H460, …) | top dose only |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.693×** | -3.8 | 0.032 | 9/14 (LoVo, KATO III, …) | inconsistent across doses |  |
| [[Budesonide (drug)]] 5 µM |  | **0.719×** | -3.4 | 0.086 | 6/14 (Hs 766T, LoVo, …) | top dose only |  |
| [[Erlotinib (drug)]] 0.05 µM |  | **0.706×** | -3.3 | 0.086 | 0/14 | inconsistent across doses |  |
| [[Dihydroartemisinin (drug)]] 5 µM |  | **0.727×** | -3.3 | 0.086 | 6/14 (HT-29, COLO 205, …) | top dose only | position effect removed |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~38% of this change | **0.727×** | -3.3 | 0.086 | 12/14 (LoVo, LS 180, …) | all doses, stronger at high dose |  |
| [[Abemaciclib (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.730×** | -3.2 | 0.086 | 2/14 (LoVo, SW48) | inconsistent across doses |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~33% of this change | 0.737× | -3.1 | 0.11 | 13/14 (LoVo, LS 180, …) | all doses, stronger at high dose |  |
| [[Neratinib (maleate) (drug)]] 5 µM |  | 0.811× | -3.0 | 0.14 | 7/14 (LoVo, NCI-H460, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.27 per unit of S-phase module lfc, +0.35 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4799. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[KATO III (line)]] | alt | 164 | 1 (1 ⚠) | 7 (4 ⚠) | [[Dinaciclib (drug)]] 5 µM 3.45× (z +8.8) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.192× (z -17.2) |
| [[COLO 205 (line)]] | alt | 75.6 | 0 | 6 (4 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.0729× (z -13.4) ⚠ cell-cycle shift, explains ~38% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.226× (z -10.7) |
| [[LoVo (line)]] | wt | 475 | 0 | 5 (3 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.0866× (z -19.7) ⚠ cell-cycle shift, explains ~38% of this change · without an alert: [[Belinostat (drug)]] 5 µM 0.0994× (z -18.6) |
| [[LS 180 (line)]] | wt | 149 | 0 | 5 (4 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.0913× (z -18.4) ⚠ cell-cycle shift, explains ~38% of this change · without an alert: [[Belinostat (drug)]] 5 µM 0.146× (z -14.7) |
| [[NCI-H460 (line)]] | wt | 8.80 | 3 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 5.96× (z +9.3) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 3.05× (z +8.5) | — |
| [[AsPC-1 (line)]] | alt | 45.9 | 2 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.86× (z +9.1) | — |
| [[HT-29 (line)]] | alt | 62.2 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.235× (z -11.5) |
| [[Hs 766T (line)]] | wt | 42.4 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.271× (z -9.3) |
| [[NCI-H1792 (line)]] | alt | 12.9 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 13.3× (z +15.1) | — |
| [[A-172 (line)]] | wt | 3.67 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 2.76 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 2.75 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 2.82 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 5.95 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 3.67 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 4.42 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 3.65 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 11.1 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 6.49 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 3.36 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 5.12 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 4.12 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 6.29 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 3.60 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 3.33 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 4.48 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 3.37 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 4.48 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 2.55 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 13.8 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 3.19 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 22.8 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 3.15 n.m. | — | — | — | — |
| [[NCI-H2347 (line)]] | alt | 3.36 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 33.9 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 4.17 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 3.98 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 2.66 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 3.48 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 3.35 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 11.6 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 3.23 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 3.67 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 3.73 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 5.98 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 3.82 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 7.61 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 20.1 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 11.3 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 4.61 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4799), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CFTR]] | +0.82 | +0.78 / +0.73 | both halves | 7e-06 | **novel candidate** |
| [[ST6GALNAC1]] | +0.81 | +0.82 / +0.73 | both halves | 7e-06 | **novel candidate** |
| [[CDH17]] | +0.81 | +0.75 / +0.81 | both halves | 7e-06 | **novel candidate** |
| [[FXYD3]] | +0.80 | +0.79 / +0.76 | both halves | 7e-06 | **novel candidate** |
| [[UGT1A1]] | +0.79 | +0.79 / +0.72 | both halves | 7e-06 | **novel candidate** |
| [[GPA33]] | +0.79 | +0.76 / +0.75 | both halves | 7e-06 | **novel candidate** |
| [[TM4SF4]] | +0.77 | +0.66 / +0.77 | both halves | 7e-06 | STRING 433 |
| [[PRR15]] | +0.76 | +0.71 / +0.75 | both halves | 7e-06 | **novel candidate** |
| [[MUC13]] | +0.75 | +0.79 / +0.69 | both halves | 7e-06 | STRING 570 |
| [[POF1B]] | +0.75 | +0.77 / +0.71 | both halves | 7e-06 |  |
| [[LGALS4]] | +0.75 | +0.74 / +0.73 | both halves | 7e-06 |  |
| [[HNF1A-AS1]] | +0.74 | +0.68 / +0.62 | both halves | 7e-06 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*98 arrows, 98 of them with an alert ⚠; grade A 0, B 7, C 91. Shown: the 12 strongest; 86 more arrows (86 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers TSPAN8's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 6.2% of all compounds | 0.047 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[HNMT]] | B | HNMT activity raises TSPAN8's level | lines that do not express HNMT (17) vs lines expressing it (33) | 2.17× lower at baseline in the lines without HNMT | 0.059 | ⚠ within organs, on part of the lines; also absent: PLAAT4, TNFSF10, VSIR |
| [[SLC44A5]] | B | SLC44A5 activity raises TSPAN8's level | lines that do not express SLC44A5 (17) vs lines expressing it (33) | 2.25× lower at baseline in the lines without SLC44A5 | 0.063 | ⚠ within organs, on part of the lines; also absent: ENSG00000289609; maybe low, not absent |
| [[SHROOM3]] | B | SHROOM3 activity raises TSPAN8's level | lines that do not express SHROOM3 (19) vs lines expressing it (31) | 2.70× lower at baseline in the lines without SHROOM3 | 0.079 | ⚠ within organs, on part of the lines; co-occurs with TERT; also absent: RHOV, ELF3, PLUT |
| [[HTR1D]] | B | HTR1D activity raises TSPAN8's level | lines that do not express HTR1D (15) vs lines expressing it (35) | 2.06× lower at baseline in the lines without HTR1D | 0.082 | ⚠ within organs, on part of the lines; also absent: A4GALT, ZNF185, PAPSS2; maybe low, not absent |
| [[GNA14]] | B | GNA14 activity raises TSPAN8's level | lines that do not express GNA14 (5) vs lines expressing it (45) | 2.45× lower at baseline in the lines without GNA14 | 0.083 | ⚠ within organs, on part of the lines; also absent: SSUH2, EXT1, SAMSN1; maybe low, not absent |
| [[IKZF2]] | B | IKZF2 activity raises TSPAN8's level | lines that do not express IKZF2 (13) vs lines expressing it (37) | 1.83× lower at baseline in the lines without IKZF2 | 0.097 | ⚠ within organs, on part of the lines; also absent: ENSG00000273118, MECOM, SEMA3C; maybe low, not absent |
| [[CDH17]] | C | CDH17 activity raises TSPAN8's level | lines that do not express CDH17 (40) vs lines expressing it (10) | 10.51× lower at baseline in the lines without CDH17 | 2e-04 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: NPSR1, MUC13, CLRN3; co-absent with the target |
| [[NPSR1]] | C | NPSR1 activity raises TSPAN8's level | lines that do not express NPSR1 (42) vs lines expressing it (8) | 13.57× lower at baseline in the lines without NPSR1 | 3e-04 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: REG4, MUC17, CDH17; co-absent with the target |
| [[PTPRR]] | C | PTPRR activity raises TSPAN8's level | lines that do not express PTPRR (32) vs lines expressing it (18) | 4.00× lower at baseline in the lines without PTPRR | 4e-04 | ⚠ within organs, on part of the lines; also absent: DHRS9, LINC01133, TFF2; co-absent with the target |
| [[CEACAM5]] | C | CEACAM5 activity raises TSPAN8's level | lines that do not express CEACAM5 (39) vs lines expressing it (11) | 7.79× lower at baseline in the lines without CEACAM5 | 4e-04 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: NPSR1, CDH17, ENSG00000267881; co-absent with the target |
| [[UGT1A1]] | C | UGT1A1 activity raises TSPAN8's level | lines that do not express UGT1A1 (36) vs lines expressing it (14) | 5.47× lower at baseline in the lines without UGT1A1 | 7e-04 | ⚠ within organs, on part of the lines; also absent: UGT1A6, UGT1A9, NPSR1; co-absent with the target |

### Downstream of this gene

*79 arrows, 79 of them with an alert ⚠; grade A 0, B 11, C 68. Shown: the 12 strongest; 67 more arrows (67 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SLC37A1]] | B | TSPAN8 activity raises SLC37A1's level | lines that do not express TSPAN8 (34) vs lines expressing it (16) | 3.35× lower at baseline in the lines without TSPAN8 | 0.002 | ⚠ within organs, on part of the lines; also absent: ENSG00000267881, SERPINB5, CDH17 |
| [[BAG1]] | B | TSPAN8 activity raises BAG1's level | lines that do not express TSPAN8 (34) vs lines expressing it (16) | 1.93× lower at baseline in the lines without TSPAN8 | 0.004 | ⚠ within organs, on part of the lines; also absent: ENSG00000267881, SERPINB5, CDH17 |
| [[MGST2]] | B | TSPAN8 activity raises MGST2's level | lines that do not express TSPAN8 (34) vs lines expressing it (16) | 2.81× lower at baseline in the lines without TSPAN8 | 0.010 | ⚠ within organs, on part of the lines; also absent: ENSG00000267881, SERPINB5, CDH17 |
| [[RSPH1]] | B | TSPAN8 activity raises RSPH1's level | lines that do not express TSPAN8 (34) vs lines expressing it (16) | 2.37× lower at baseline in the lines without TSPAN8 | 0.022 | ⚠ within organs, on part of the lines; also absent: ENSG00000267881, SERPINB5, CDH17 |
| [[SLC12A2]] | B | TSPAN8 activity raises SLC12A2's level | lines that do not express TSPAN8 (34) vs lines expressing it (16) | 2.46× lower at baseline in the lines without TSPAN8 | 0.026 | ⚠ within organs, on part of the lines; also absent: ENSG00000267881, SERPINB5, CDH17 |
| [[MFSD6]] | B | TSPAN8 activity raises MFSD6's level | lines that do not express TSPAN8 (34) vs lines expressing it (16) | 2.20× lower at baseline in the lines without TSPAN8 | 0.027 | ⚠ within organs, on part of the lines; also absent: ENSG00000267881, SERPINB5, CDH17 |
| [[ATP8B1]] | B | TSPAN8 activity raises ATP8B1's level | lines that do not express TSPAN8 (34) vs lines expressing it (16) | 3.04× lower at baseline in the lines without TSPAN8 | 0.037 | ⚠ within organs, on part of the lines; also absent: ENSG00000267881, SERPINB5, CDH17 |
| [[SLC44A5]] | B | TSPAN8 activity raises SLC44A5's level | lines that do not express TSPAN8 (34) vs lines expressing it (16) | 2.36× lower at baseline in the lines without TSPAN8 | 0.060 | ⚠ within organs, on part of the lines; also absent: ENSG00000267881, SERPINB5, CDH17 |
| [[PLA2R1]] | B | TSPAN8 activity raises PLA2R1's level | lines that do not express TSPAN8 (34) vs lines expressing it (16) | 2.70× lower at baseline in the lines without TSPAN8 | 0.064 | ⚠ within organs, on part of the lines; also absent: ENSG00000267881, SERPINB5, CDH17 |
| [[TRIM2]] | B | TSPAN8 activity raises TRIM2's level | lines that do not express TSPAN8 (34) vs lines expressing it (16) | 2.59× lower at baseline in the lines without TSPAN8 | 0.073 | ⚠ within organs, on part of the lines; also absent: ENSG00000267881, SERPINB5, CDH17 |
| [[EPB41L1]] | B | TSPAN8 activity raises EPB41L1's level | lines that do not express TSPAN8 (34) vs lines expressing it (16) | 2.29× lower at baseline in the lines without TSPAN8 | 0.083 | ⚠ within organs, on part of the lines; also absent: ENSG00000267881, SERPINB5, CDH17 |
| [[PTPRR]] | C | TSPAN8 activity raises PTPRR's level | lines that do not express TSPAN8 (34) vs lines expressing it (16) | 5.64× lower at baseline in the lines without TSPAN8 | 0.002 | ⚠ within organs, on part of the lines; also absent: ENSG00000267881, SERPINB5, CDH17; co-absent with the target |

## Where it sits

- **Module**: [[Module 044]] — Defective GALNT12 causes CRCS1; 102 genes; every member is in the + arm (projection on the module's main direction 0.864). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.29; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (22.8, 51.3); signed map (63.8, 5.0). **Vector** length 67.7, 28.2% of its response variance represented; |z| ≥ 3 in 394 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *Defective GALNT12 causes CRCS1* (reactome, mean cos +0.62 to 5); *Defective GALNT3 causes HFTC* (reactome, mean cos +0.62 to 5); *Defective C1GALT1C1 causes TNPS* (reactome, mean cos +0.62 to 5).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +7.1 | +14.1 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +7.0 | +18.4 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +6.6 | +9.6 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +5.0 | +19.9 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +4.5 | +15.2 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +3.6 | +6.7 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.8 | +3.1 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.8 | +4.1 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +1.8 | +2.7 |
|  | [[Ponatinib (drug)]] 0.5 µM |  | +1.6 | +2.1 |
| fall | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -3.2 | -3.8 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -2.2 | -3.8 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -2.1 | -1.4 |
|  | [[Mebendazole (drug)]] 5 µM |  | -1.8 | -2.1 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -1.7 | -2.7 |
|  | [[Abemaciclib (drug)]] 0.5 µM |  | -1.5 | -1.9 |

## What is on record

|  |  |
|---|---|
| Name | tetraspanin 8 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 12q21.1 — chr12:71,125,085-71,441,898 (-) |
| Ensembl biotype | protein_coding |
| Also known as | CO-029; previously TM4SF3 |
| Gene groups (HGNC) | Tetraspanin family |
| Hallmark sets | PROTEIN_SECRETION |
| Matched by | ensembl_id |

**Function**, from UniProt [P19075](https://www.uniprot.org/uniprotkb/P19075) (Tetraspanin-8):

> Structural component of specialized membrane microdomains known as tetraspanin-enriched microdomains (TERMs), which act as platforms for receptor clustering and signaling. Participates thereby in diverse biological functions such as cell signal transduction, migration and protein trafficking. Promotes ADAM17-mediated TNF processing through recruitment of ADAM17 to tetraspanin-enriched micro-domains (TEMs). Forms a complex with RICTOR and integrin alpha3/ITGA3 to mediate mTORC2 activation and …

**Summary**, from NCBI Gene [7103](https://www.ncbi.nlm.nih.gov/gene/7103):

> The protein encoded by this gene is a member of the transmembrane 4 superfamily, also known as the tetraspanin family. Most of these members are cell-surface proteins that are characterized by the presence of four hydrophobic domains. The proteins mediate signal transduction events that play a role in the regulation of cell development, activation, growth and motility. This encoded protein is a cell surface glycoprotein that is known to complex with integrins. This gene is expressed in …

**Accessions** — [HGNC:11855](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:11855) · Entrez [7103](https://www.ncbi.nlm.nih.gov/gene/7103) · UniProt [P19075](https://www.uniprot.org/uniprotkb/P19075) · Ensembl [ENSG00000127324](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000127324)

## Data

Gene col 4799: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4799); `tables/drug_effects.parquet` (35 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4799, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4799]; `tensor/DDL_lfc|DDL_z.npy` [4799]; `embed/gene_vectors.npy` [4799]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4799 or target_col == 4799). Every well: [[TSPAN8 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TSPAN8.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
