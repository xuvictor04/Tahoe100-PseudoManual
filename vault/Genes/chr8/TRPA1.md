---
symbol: "TRPA1"
type: "gene"
col: 2439
ensembl_id: "ENSG00000104321"
name: "transient receptor potential cation channel subfamily A member 1"
location: "8q21.11"
module: 19
arm: "+"
pooled_cpm: 7.81
n_lines_expressing: 19
n_dd_up: 8
n_dd_down: 3
n_dd_up_clean: 3
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 12
direction_downstream: 33
tags: ["gene", "module/019"]
generated_by: "tahoemap"
---

# TRPA1

*transient receptor potential cation channel subfamily A member 1* — 8q21.11

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 8 drug-doses (5 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 3.42× (z +12.4, q 2e-32, up in 5 of 11 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Tucidinostat (drug)]] 5 µM: 1.42× (z +4.9, q 8e-05, up in 5 of 17 measured lines).
> Pooled over the cell lines (median), lowered significantly by 3 drug-doses (1 with an alert ⚠); the strongest is [[Digitoxin (drug)]] 0.5 µM: 0.644× (z -4.4, q 0.005, down in 10 of 16 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 8 here, 4 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 3 lines (SHP-77 0.0689×, CHP-212 0.176×, A549 0.197×; ⚠ cell-cycle shift, explains ~0% of this change); [[Panobinostat (drug)]] 0.5 µM in 3 lines (HOP62 0.0878×, CHP-212 0.113×, NCI-H1792 0.190×); [[Homoharringtonine (drug)]] 0.5 µM in 3 lines (NCI-H1573 0.0808×, NCI-H1792 0.164×, CHP-212 0.132×); [[Panobinostat (drug)]] 5 µM in 2 lines (HOP62 0.0977×, SHP-77 0.133×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[EDIL3]] (+0.68, fdr 1e-05), [[NCKAP5]] (+0.64, fdr 1e-05), [[NOVA1]] (+0.64, fdr 1e-05).
> It is in [[Module 019]], a single-armed module (Neuronal System).
> Probable direction (from the cell lines, not proof of direct regulation): 12 arrows point to it, the strongest [[RARB]] → it (grade C ⚠); 33 go from it, the strongest it → [[HECW2]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 5 with an alert ⚠. 8 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2439.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **3.42×** | +12.4 | 2e-32 | 5/11 (PANC-1, HOP62, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.87×** | +10.2 | 4e-22 | 3/7 (PANC-1, HOP62, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.81×** | +9.7 | 9e-20 | 1/9 (NCI-H1573) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.85×** | +6.2 | 7e-08 | 1/9 (NCI-H1573) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~1% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.42×** | +4.9 | 8e-05 | 5/17 (NCI-H460, PANC-1, …) | inconsistent across doses |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.66×** | +4.9 | 8e-05 | 1/10 (NCI-H1792) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Oxaprozin (drug)]] 0.5 µM |  | **1.47×** | +3.9 | 0.009 | 1/16 (NCI-H460) | inconsistent across doses |  |
| [[Methylprednisolone succinate (drug)]] 0.5 µM |  | **1.59×** | +3.3 | 0.060 | 0/17 | inconsistent across doses | low cells (technical?); noisy plate (z scaled) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | 1.37× | +3.1 | 0.13 | 6/16 (HOP62, hTERT-HPNE, …) | top dose only |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | 1.37× | +3.0 | 0.13 | 0/12 | top dose only | cell-cycle shift (explains ~0% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 1 with an alert ⚠. 3 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 2439.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 8 here, 4 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 3 lines (SHP-77 0.0689×, CHP-212 0.176×, A549 0.197×; ⚠ cell-cycle shift, explains ~0% of this change); [[Panobinostat (drug)]] 0.5 µM in 3 lines (HOP62 0.0878×, CHP-212 0.113×, NCI-H1792 0.190×); [[Homoharringtonine (drug)]] 0.5 µM in 3 lines (NCI-H1573 0.0808×, NCI-H1792 0.164×, CHP-212 0.132×); [[Panobinostat (drug)]] 5 µM in 2 lines (HOP62 0.0977×, SHP-77 0.133×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 0.5 µM |  | **0.644×** | -4.4 | 0.005 | 10/16 (SHP-77, NCI-H1792, …) | inconsistent across doses | cell-cycle shift (explains ~3% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.674×** | -4.0 | 0.018 | 7/16 (HOP62, CHP-212, …) | inconsistent across doses |  |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.680×** | -3.9 | 0.018 | 12/17 (HOP62, CHP-212, …) | two highest doses | cell-cycle shift (explains ~10% here) |
| [[Digitoxin (drug)]] 0.05 µM |  | 0.672× | -3.4 | 0.11 | 4/14 (NCI-H460, C32, …) | inconsistent across doses | cell-cycle shift (explains ~1% here) |
| [[Panobinostat (drug)]] 5 µM |  | 0.666× | -3.3 | 0.12 | 10/17 (HOP62, SHP-77, …) | two highest doses | cell-cycle shift (explains ~10% here); noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | 0.732× | -3.2 | 0.15 | 7/16 (HOP62, NCI-H1792, …) | inconsistent across doses |  |
| [[TAK-733 (drug)]] 0.05 µM |  | 0.728× | -3.0 | 0.19 | 1/17 (NCI-H1792) | inconsistent across doses |  |
| [[(S)-Crizotinib (drug)]] 0.05 µM |  | 0.726× | -3.0 | 0.19 | 2/16 (HS-578T, LOX-IMVI) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.11 per unit of S-phase module lfc, +0.05 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2439. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[CHP-212 (line)]] | wt | 146 | 0 | 4 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.176× (z -10.7) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.113× (z -9.5) |
| [[NCI-H1792 (line)]] | alt | 22.9 | 0 | 4 (2 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.123× (z -10.6) ⚠ toxic · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.164× (z -9.5) |
| [[SHP-77 (line)]] | alt | 74.7 | 0 | 4 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0689× (z -20.2) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.133× (z -8.6) |
| [[HOP62 (line)]] | alt | 78.0 | 0 | 3 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.0878× (z -12.1) |
| [[NCI-H1573 (line)]] | alt | 7.23 | 0 | 2 | — | [[Crizotinib (hydrochloride) (drug)]] 0.5 µM 0.0561× (z -12.5) |
| [[A549 (line)]] | wt | 12.7 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.197× (z -9.4) ⚠ cell-cycle shift, explains ~0% of this change |
| [[NCI-H460 (line)]] | wt | 4.31 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.282× (z -8.6) ⚠ cell-cycle shift, explains ~0% of this change |
| [[A-172 (line)]] | wt | 1.22 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 0.790 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 23.5 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 1.82 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 1.12 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 1.71 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 1.11 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 2.06 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 1.42 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 1.00 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 1.91 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 1.12 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 1.01 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 1.13 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 0.935 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 3.20 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 1.16 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 2.97 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 1.14 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 1.01 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 1.34 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 2.03 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 1.91 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.849 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 1.55 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 8.74 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 1.37 n.m. | — | — | — | — |
| [[NCI-H2347 (line)]] | alt | 0.849 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 9.69 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 1.19 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 0.889 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 4.35 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 1.07 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 4.66 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 1.52 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 1.04 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 2.05 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 18.0 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 1.24 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 3.07 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 0.939 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 1.16 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 0.953 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2439), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[EDIL3]] | +0.68 | +0.55 / +0.73 | both halves | 1e-05 | **novel candidate** |
| [[NCKAP5]] | +0.64 | +0.58 / +0.54 | both halves | 1e-05 | **novel candidate** |
| [[NOVA1]] | +0.64 | +0.54 / +0.65 | both halves | 1e-05 |  |
| [[MSC-AS1]] | +0.64 | +0.65 / +0.56 | both halves | 1e-05 | ⚠ same locus (0.0 kb: neighbours can correlate without regulation) |
| [[CASC15]] | +0.63 | +0.68 / +0.47 | both halves | 2e-05 | **novel candidate** |
| [[PDE7B]] | +0.62 | +0.61 / +0.57 | both halves | 1e-05 |  |
| [[EYA2]] | +0.62 | +0.53 / +0.57 | both halves | 1e-05 | **novel candidate** |
| [[GPC6]] | +0.62 | +0.65 / +0.54 | both halves | 1e-05 | **novel candidate** |
| [[LINC00648]] | +0.61 | +0.55 / +0.56 | both halves | 1e-05 | **novel candidate** |
| [[COL8A1]] | +0.60 | +0.48 / +0.59 | both halves | 2e-05 | **novel candidate** |
| [[TEX41]] | +0.60 | +0.54 / +0.55 | both halves | 1e-05 |  |
| [[GPRIN3]] | +0.60 | +0.55 / +0.58 | both halves | 1e-05 |  |
| [[PEX5L]] | +0.59 | +0.54 / +0.56 | both halves | 1e-05 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*12 arrows, 12 of them with an alert ⚠; grade A 0, B 0, C 12.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[RARB]] | C | RARB activity raises TRPA1's level | lines that do not express RARB (28) vs lines expressing it (22) | 3.31× lower at baseline in the lines without RARB | 0.013 | ⚠ within organs, on part of the lines; also absent: MSC-AS1, NEFM, PAPPA; co-absent with the target |
| [[SGIP1]] | C | SGIP1 activity raises TRPA1's level | lines that do not express SGIP1 (31) vs lines expressing it (19) | 3.07× lower at baseline in the lines without SGIP1 | 0.016 | ⚠ within organs, on part of the lines; also absent: MEG3, HGF, MIR493HG; co-absent with the target |
| [[CD38]] | C | CD38 activity raises TRPA1's level | lines that do not express CD38 (35) vs lines expressing it (15) | 2.82× lower at baseline in the lines without CD38 | 0.029 | ⚠ within organs, on part of the lines; also absent: MAGEA10, RNF17, GRIA2; maybe low, not absent; co-absent with the target |
| [[PEX5L]] | C | PEX5L activity raises TRPA1's level | lines that do not express PEX5L (32) vs lines expressing it (18) | 2.10× lower at baseline in the lines without PEX5L | 0.031 | ⚠ within organs, on part of the lines; also absent: ENSG00000253363, APCDD1L, UBBP4-1; maybe low, not absent; co-absent with the target |
| [[MSC-AS1]] | C | MSC-AS1 activity raises TRPA1's level | lines that do not express MSC-AS1 (27) vs lines expressing it (23) | 3.46× lower at baseline in the lines without MSC-AS1 | 0.037 | ⚠ within organs, on part of the lines; also absent: ADAM12, CNRIP1, FMN2; co-absent with the target |
| [[FRMPD4]] | C | FRMPD4 activity raises TRPA1's level | lines that do not express FRMPD4 (24) vs lines expressing it (26) | 2.77× lower at baseline in the lines without FRMPD4 | 0.048 | ⚠ within organs, on part of the lines; also absent: COL4A1, BICC1, NTF3; co-absent with the target |
| [[TEX41]] | C | TEX41 activity raises TRPA1's level | lines that do not express TEX41 (29) vs lines expressing it (21) | 2.45× lower at baseline in the lines without TEX41 | 0.072 | ⚠ within organs, on part of the lines; also absent: SPOCK1, ENSG00000280241, ADAM12; co-absent with the target |
| [[PDE3A]] | C | PDE3A activity raises TRPA1's level | lines that do not express PDE3A (34) vs lines expressing it (16) | 3.06× lower at baseline in the lines without PDE3A | 0.076 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: PGR, SNTG1, COL19A1; co-absent with the target |
| [[GLIS3]] | C | GLIS3 activity raises TRPA1's level | lines that do not express GLIS3 (21) vs lines expressing it (29) | 1.81× lower at baseline in the lines without GLIS3 | 0.086 | ⚠ within organs, on part of the lines; also absent: ENSG00000232949, STEAP1B-AS1, SYNPO; co-absent with the target |
| [[TCF4]] | C | TCF4 activity raises TRPA1's level | lines that do not express TCF4 (25) vs lines expressing it (25) | 2.56× lower at baseline in the lines without TCF4 | 0.088 | ⚠ within organs, on part of the lines; also absent: KCNT2, APCDD1L, MSC-AS1; co-absent with the target |
| [[NCKAP5-AS2]] | C | NCKAP5-AS2 activity raises TRPA1's level | lines that do not express NCKAP5-AS2 (31) vs lines expressing it (19) | 2.42× lower at baseline in the lines without NCKAP5-AS2 | 0.088 | ⚠ within organs, on part of the lines; also absent: MEG3, PDGFRB, UNC5D; co-absent with the target |
| [[ANGPTL2]] | C | ANGPTL2 activity raises TRPA1's level | lines that do not express ANGPTL2 (29) vs lines expressing it (21) | 2.27× lower at baseline in the lines without ANGPTL2 | 0.098 | ⚠ within organs, on part of the lines; also absent: LINC01611, ENSG00000189229, CDH13; maybe low, not absent; co-absent with the target |

### Downstream of this gene

*33 arrows, 33 of them with an alert ⚠; grade A 0, B 3, C 30. Shown: the 12 strongest; 21 more arrows (21 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HECW2]] | B | TRPA1 activity strengthens HECW2's drug response | lines that do not express TRPA1 (12) vs lines expressing it (15) | the lines without TRPA1 respond 0.86× as strongly (z diff +0.13); strongest at Belinostat 5 µM: 0.75x vs 0.40x (z diff +3.6) | 0.036 | ⚠ within organs, on part of the lines; also absent: ITGA4, DOCK10, INSYN2B; target measured in part of the lines; both ways; artifact flags |
| cells under [[Epirubicin (hydrochloride) (drug)]] 5 µM | B | TRPA1 activity raises the cells' numbers under Epirubicin (hydrochloride) 5 µM (protects the cells) | lines that do not express TRPA1 (31) vs lines expressing it (17) | the lines without TRPA1: 0.59× the cells of the other lines | 0.050 | ⚠ within organs, on part of the lines; also absent: ITGA4, DOCK10, INSYN2B |
| [[P4HA3]] | B | TRPA1 activity raises P4HA3's level | lines that do not express TRPA1 (31) vs lines expressing it (19) | 1.79× lower at baseline in the lines without TRPA1 | 0.067 | ⚠ within organs, on part of the lines; also absent: ITGA4, DOCK10, INSYN2B |
| [[RARB]] | C | TRPA1 activity raises RARB's level | lines that do not express TRPA1 (31) vs lines expressing it (19) | 6.32× lower at baseline in the lines without TRPA1 | 7e-04 | ⚠ within organs, on part of the lines; also absent: ITGA4, DOCK10, INSYN2B; co-absent with the target |
| [[ADAM12]] | C | TRPA1 activity raises ADAM12's level | lines that do not express TRPA1 (31) vs lines expressing it (19) | 8.05× lower at baseline in the lines without TRPA1 | 0.001 | ⚠ within organs, on part of the lines; also absent: ITGA4, DOCK10, INSYN2B; co-absent with the target |
| [[GLIS3]] | C | TRPA1 activity raises GLIS3's level | lines that do not express TRPA1 (31) vs lines expressing it (19) | 4.14× lower at baseline in the lines without TRPA1 | 0.005 | ⚠ within organs, on part of the lines; also absent: ITGA4, DOCK10, INSYN2B; co-absent with the target |
| [[TREM1]] | C | TRPA1 activity raises TREM1's level | lines that do not express TRPA1 (31) vs lines expressing it (19) | 2.92× lower at baseline in the lines without TRPA1 | 0.006 | ⚠ within organs, on part of the lines; also absent: ITGA4, DOCK10, INSYN2B; co-absent with the target |
| [[PAPPA]] | C | TRPA1 activity raises PAPPA's level | lines that do not express TRPA1 (31) vs lines expressing it (19) | 6.52× lower at baseline in the lines without TRPA1 | 0.006 | ⚠ within organs, on part of the lines; also absent: ITGA4, DOCK10, INSYN2B; co-absent with the target |
| [[ARHGEF6]] | C | TRPA1 activity raises ARHGEF6's level | lines that do not express TRPA1 (31) vs lines expressing it (19) | 3.51× lower at baseline in the lines without TRPA1 | 0.006 | ⚠ within organs, on part of the lines; also absent: ITGA4, DOCK10, INSYN2B; co-absent with the target |
| [[SGIP1]] | C | TRPA1 activity raises SGIP1's level | lines that do not express TRPA1 (31) vs lines expressing it (19) | 5.01× lower at baseline in the lines without TRPA1 | 0.006 | ⚠ within organs, on part of the lines; also absent: ITGA4, DOCK10, INSYN2B; co-absent with the target |
| [[HECW2]] | C | TRPA1 activity raises HECW2's level | lines that do not express TRPA1 (31) vs lines expressing it (19) | 4.78× lower at baseline in the lines without TRPA1 | 0.007 | ⚠ within organs, on part of the lines; also absent: ITGA4, DOCK10, INSYN2B; co-absent with the target |
| [[KCNE4]] | C | TRPA1 activity raises KCNE4's level | lines that do not express TRPA1 (31) vs lines expressing it (19) | 4.08× lower at baseline in the lines without TRPA1 | 0.007 | ⚠ within organs, on part of the lines; also absent: ITGA4, DOCK10, INSYN2B; co-absent with the target |

## Where it sits

- **Module**: [[Module 019]] — Neuronal System; 196 genes; every member is in the + arm (projection on the module's main direction 0.606). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.17; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (45.2, 32.6); signed map (38.7, 44.4). **Vector** length 43.8, 11.4% of its response variance represented; |z| ≥ 3 in 430 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +6.4 | +12.4 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +6.2 | +10.2 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +6.0 | +9.7 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | +5.1 | +2.0 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +3.9 | +4.9 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +1.9 | +2.8 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +1.5 | +2.8 |
|  | [[Auranofin (drug)]] 5 µM |  | +1.4 | +1.9 |
|  | [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | +1.4 | +0.0 |
| fall | [[Dexamethasone (drug)]] 0.5 µM |  | -1.6 | -1.3 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -1.5 | -1.1 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -1.4 | -1.3 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | -1.4 | -4.4 |
|  | [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | -1.4 | -2.8 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -1.3 | -2.8 |
|  | [[Mebendazole (drug)]] 5 µM |  | -1.3 | -1.4 |

## What is on record

|  |  |
|---|---|
| Name | transient receptor potential cation channel subfamily A member 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 8q21.11 — chr8:72,019,917-72,075,584 (-) |
| Ensembl biotype | protein_coding |
| Also known as | ; previously ANKTM1 |
| Gene groups (HGNC) | Ankyrin repeat domain containing; Transient receptor potential cation channel subfamily A |
| Reactome | 4 pathways, smallest: TRP channels; Stimuli-sensing channels; Ion channel transport |
| Matched by | ensembl_id |

**Function**, from UniProt [O75762](https://www.uniprot.org/uniprotkb/O75762) (Transient receptor potential cation channel subfamily A member 1):

> Ligand-activated Ca(2+)-permeable, nonselective cation channel involved in pain detection and possibly also in cold perception, oxygen concentration perception, cough, itch, and inner ear function. Has a relatively high Ca(2+) selectivity, with a preference for divalent over monovalent cations (Ca(2+) > Ba(2+) > Mg(2+) > NH4(+) > Li(+) > K(+)), the influx of cation into the cytoplasm leads to membrane depolarization. Has a central role in the pain response to endogenous inflammatory mediators, …

**Summary**, from NCBI Gene [8989](https://www.ncbi.nlm.nih.gov/gene/8989):

> The structure of the protein encoded by this gene is highly related to both the protein ankyrin and transmembrane proteins. The specific function of this protein has not yet been determined; however, studies indicate the function may involve a role in signal transduction and growth control. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:497](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:497) · Entrez [8989](https://www.ncbi.nlm.nih.gov/gene/8989) · UniProt [O75762](https://www.uniprot.org/uniprotkb/O75762) · Ensembl [ENSG00000104321](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000104321)

## Data

Gene col 2439: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2439); `tables/drug_effects.parquet` (18 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2439, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2439]; `tensor/DDL_lfc|DDL_z.npy` [2439]; `embed/gene_vectors.npy` [2439]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2439 or target_col == 2439). Every well: [[TRPA1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TRPA1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
