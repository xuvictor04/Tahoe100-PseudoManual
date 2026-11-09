---
symbol: "MSC"
type: "gene"
col: 10966
ensembl_id: "ENSG00000178860"
name: "musculin"
location: "8q13.3"
module: 14
arm: "+"
pooled_cpm: 3.16
n_lines_expressing: 16
n_dd_up: 19
n_dd_down: 0
n_dd_up_clean: 7
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 19
direction_downstream: 33
tags: ["gene", "module/014"]
generated_by: "tahoemap"
---

# MSC

*musculin* — 8q13.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 19 drug-doses (12 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 6.35× (z +9.9, q 2e-20, up in 0 of 5 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Selinexor (drug)]] 5 µM: 1.75× (z +4.4, q 7e-04, up in 2 of 13 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 7 here, 6 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Panobinostat (drug)]] 0.5 µM in 5 lines (A498 0.0779×, A549 0.0259×, HS-578T 0.0607×, NCI-H1792 0.0789×, …; ⚠ cell-cycle shift, explains ~43% of this change); [[Panobinostat (drug)]] 5 µM in 4 lines (A498 0.0874×, HS-578T 0.0654×, SNU-423 0.0502×, H4 0.0434×; ⚠ cell-cycle shift, explains ~40% of this change); [[Dinaciclib (drug)]] 5 µM in 1 line (A498 0.153×; ⚠ toxic; transcription drop); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (A498 0.296×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[MSC-AS1]] (+0.73, fdr 7e-06, ⚠ same locus), [[NR3C1]] (+0.71, fdr 7e-06), [[GBP5]] (+0.69, fdr 7e-06), [[IL6]] (+0.68, fdr 7e-06).
> It is in [[Module 014]], a single-armed module (TNF-alpha signaling via NF-kB).
> Probable direction (from the cell lines, not proof of direct regulation): 19 arrows point to it, the strongest [[GPR158]] → it (grade B ⚠); 33 go from it, the strongest it → [[CPEB2]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 19 in all, 12 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 19 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 12 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10966.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **6.35×** | +9.9 | 2e-20 | 0/5 | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **4.69×** | +8.6 | 2e-15 | 0/7 | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **4.11×** | +7.3 | 6e-11 | 0/5 | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **3.33×** | +6.7 | 3e-09 | 3/7 (SK-MEL-2, HS-578T, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~7% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **3.42×** | +6.6 | 5e-09 | 8/9 (SNU-423, A549, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[AZD2858 (drug)]] 0.5 µM | ⚠ toxic | **4.60×** | +5.2 | 2e-05 | 0/5 | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **2.51×** | +4.9 | 7e-05 | 1/9 (RPMI-7951) | inconsistent across doses | cell-cycle shift (explains ~0% here); position effect removed |
| [[Imiquimod (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **2.40×** | +4.8 | 9e-05 | 0/10 | top dose only |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.22×** | +4.4 | 6e-04 | 0/11 | top dose only | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 5 µM |  | **1.75×** | +4.4 | 7e-04 | 2/13 (HS-578T, RPMI-7951) | top dose only | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Nimesulide (drug)]] 5 µM | ⚠ toxic; unreliable plate only | **2.07×** | +4.0 | 0.003 | 0/10 | top dose only |  |
| [[Bendamustine (drug)]] 5 µM |  | **1.94×** | +3.5 | 0.019 | 2/10 (SNU-423, H4) | top dose only |  |
| [[Saquinavir (drug)]] 5 µM |  | **1.57×** | +3.5 | 0.019 | 2/13 (hTERT-HPNE, NCI-H1573) | inconsistent across doses |  |
| [[Fingolimod (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.84×** | +3.4 | 0.030 | 0/13 | top dose only | position effect removed |
| [[TAK-901 (drug)]] 5 µM |  | **3.10×** | +3.3 | 0.037 | 12/13 (RPMI-7951, HS-578T, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~1% here); composition shift; noisy plate (z scaled) |
| [[XRK3F2 (drug)]] 0.5 µM |  | **2.48×** | +3.1 | 0.069 | 0/8 | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.71×** | +3.0 | 0.094 | 8/13 (A498, A549, …) | rises with dose | cell-cycle shift (explains ~24% here) |
| [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM |  | **1.71×** | +3.0 | 0.094 | 0/10 | inconsistent across doses | low cells (technical?) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 4 in all, 1 with an alert ⚠. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 10966.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 7 here, 6 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Panobinostat (drug)]] 0.5 µM in 5 lines (A498 0.0779×, A549 0.0259×, HS-578T 0.0607×, NCI-H1792 0.0789×, …; ⚠ cell-cycle shift, explains ~43% of this change); [[Panobinostat (drug)]] 5 µM in 4 lines (A498 0.0874×, HS-578T 0.0654×, SNU-423 0.0502×, H4 0.0434×; ⚠ cell-cycle shift, explains ~40% of this change); [[Dinaciclib (drug)]] 5 µM in 1 line (A498 0.153×; ⚠ toxic; transcription drop); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (A498 0.296×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~40% of this change | 0.547× | -3.4 | 0.19 | 13/14 (A498, HS-578T, …) | all doses, flat |  |
| [[Panobinostat (drug)]] 0.05 µM |  | 0.565× | -3.3 | 0.19 | 10/14 (A-172, A498, …) | all doses, flat | cell-cycle shift (explains ~10% here) |
| [[Dexamethasone (drug)]] 0.5 µM |  | 0.566× | -3.3 | 0.19 | 5/13 (A498, NCI-H1792, …) | two highest doses |  |
| [[Pexidartinib (hydrochloride) (drug)]] 0.05 µM |  | 0.544× | -3.2 | 0.19 | 0/13 | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.47 per unit of S-phase module lfc, +0.33 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10966. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A498 (line)]] | wt | 42.2 | 0 | 6 (5 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.0779× (z -13.3) ⚠ cell-cycle shift, explains ~43% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.296× (z -9.1) |
| [[HS-578T (line)]] | alt | 8.37 | 0 | 2 (2 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.0607× (z -9.9) ⚠ cell-cycle shift, explains ~43% of this change |
| [[SNU-423 (line)]] | alt | 5.31 | 0 | 2 (2 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.0502× (z -9.2) ⚠ cell-cycle shift, explains ~40% of this change |
| [[A549 (line)]] | wt | 3.87 | 0 | 1 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.0259× (z -11.0) ⚠ cell-cycle shift, explains ~43% of this change |
| [[H4 (line)]] | wt | 10.1 | 0 | 1 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.0434× (z -8.6) ⚠ cell-cycle shift, explains ~40% of this change |
| [[NCI-H1792 (line)]] | alt | 16.5 | 0 | 1 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.0789× (z -9.8) ⚠ cell-cycle shift, explains ~43% of this change |
| [[SK-MEL-2 (line)]] | alt | 4.92 | 0 | 1 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.0550× (z -8.6) ⚠ cell-cycle shift, explains ~43% of this change |
| [[A-172 (line)]] | wt | 1.46 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 0.119 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 0.336 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 0.177 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 0.148 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 0.177 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 2.46 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 0.232 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 2.30 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 0.152 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 0.176 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 0.160 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 0.158 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 0.186 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 0.152 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 0.195 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 3.45 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 0.198 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 0.152 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 0.145 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 3.68 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 0.158 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.142 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 1.52 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 0.161 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 1.45 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 0.383 n.m. | — | — | — | — |
| [[NCI-H2347 (line)]] | alt | 0.130 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 0.155 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 1.38 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 0.192 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 0.165 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 0.165 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 0.166 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 12.1 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 0.137 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 0.178 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 0.332 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 0.176 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 0.178 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 0.148 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 0.186 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 0.144 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10966), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MSC-AS1]] | +0.73 | +0.72 / +0.68 | both halves | 7e-06 | ⚠ same locus (0.0 kb: neighbours can correlate without regulation) |
| [[NR3C1]] | +0.71 | +0.63 / +0.69 | both halves | 7e-06 |  |
| [[GBP5]] | +0.69 | +0.63 / +0.68 | both halves | 7e-06 |  |
| [[IL6]] | +0.68 | +0.65 / +0.64 | both halves | 7e-06 | pathway: HALLMARK_TNFA_SIGNALING_VIA_NFKB |
| [[SLC2A6]] | +0.65 | +0.53 / +0.62 | both halves | 1e-05 | pathway: HALLMARK_TNFA_SIGNALING_VIA_NFKB |
| [[IDO1]] | +0.65 | +0.56 / +0.64 | both halves | 1e-05 |  |
| [[ZEB2]] | +0.65 | +0.67 / +0.60 | both halves | 7e-06 |  |
| [[KYNU]] | +0.64 | +0.55 / +0.62 | both halves | 1e-05 | pathway: HALLMARK_TNFA_SIGNALING_VIA_NFKB |
| [[CCL2]] | +0.64 | +0.55 / +0.63 | both halves | 1e-05 | pathway: HALLMARK_TNFA_SIGNALING_VIA_NFKB |
| [[SHISAL1]] | +0.64 | +0.60 / +0.62 | both halves | 7e-06 |  |
| [[MARCKS]] | +0.63 | +0.52 / +0.72 | both halves | 1e-05 | pathway: HALLMARK_TNFA_SIGNALING_VIA_NFKB |
| [[SYNPO]] | +0.62 | +0.58 / +0.54 | both halves | 1e-05 |  |
| [[C1QTNF1]] | +0.62 | +0.65 / +0.49 | both halves | 1e-05 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*19 arrows, 19 of them with an alert ⚠; grade A 0, B 1, C 18. Shown: the 12 strongest; 7 more arrows (7 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[GPR158]] | B | GPR158 activity raises MSC's level | lines that do not express GPR158 (20) vs lines expressing it (30) | 1.42× lower at baseline in the lines without GPR158 | 0.065 | ⚠ within organs, on part of the lines; also absent: ENSG00000259929, P2RX7, LINC02968 |
| [[APBB1IP]] | C | APBB1IP activity raises MSC's level | lines that do not express APBB1IP (40) vs lines expressing it (10) | 3.59× lower at baseline in the lines without APBB1IP | 0.015 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: ENSG00000254337, TMPRSS15, ENSG00000235749; co-absent with the target |
| [[ABI3BP]] | C | ABI3BP activity raises MSC's level | lines that do not express ABI3BP (32) vs lines expressing it (18) | 2.00× lower at baseline in the lines without ABI3BP | 0.020 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000280241, FLI1, DKK3; maybe low, not absent; co-absent with the target |
| [[C1QTNF1-AS1]] | C | C1QTNF1-AS1 activity raises MSC's level | lines that do not express C1QTNF1-AS1 (24) vs lines expressing it (26) | 1.83× lower at baseline in the lines without C1QTNF1-AS1 | 0.028 | ⚠ within organs, on part of the lines; also absent: ADAMTS12, ENSG00000287335, FBLN2; maybe low, not absent; co-absent with the target |
| [[GBP5]] | C | GBP5 activity raises MSC's level | lines that do not express GBP5 (24) vs lines expressing it (26) | 2.45× lower at baseline in the lines without GBP5 | 0.030 | ⚠ within organs, on part of the lines; also absent: ADAMTS16, EDNRA, CHSY3; co-absent with the target |
| [[EBF1]] | C | EBF1 activity raises MSC's level | lines that do not express EBF1 (30) vs lines expressing it (20) | 2.94× lower at baseline in the lines without EBF1 | 0.039 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ADAM12, MSC, ITGA4; co-absent with the target |
| [[SIRLNT]] | C | SIRLNT activity raises MSC's level | lines that do not express SIRLNT (32) vs lines expressing it (18) | 2.48× lower at baseline in the lines without SIRLNT | 0.042 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: SRGN, LINC01411, KCNMA1; co-absent with the target |
| [[MIR3171HG]] | C | MIR3171HG activity raises MSC's level | lines that do not express MIR3171HG (33) vs lines expressing it (17) | 2.98× lower at baseline in the lines without MIR3171HG | 0.050 | ⚠ within organs, on part of the lines; also absent: LINC02616, IL13RA2, MSC; co-absent with the target |
| [[LINC01687]] | C | LINC01687 activity raises MSC's level | lines that do not express LINC01687 (31) vs lines expressing it (19) | 2.29× lower at baseline in the lines without LINC01687 | 0.055 | ⚠ within organs, on part of the lines; also absent: ENSG00000226043, LINC02616, TPTE; co-absent with the target |
| [[MSC-AS1]] | C | MSC-AS1 activity raises MSC's level | lines that do not express MSC-AS1 (27) vs lines expressing it (23) | 3.08× lower at baseline in the lines without MSC-AS1 | 0.055 | ⚠ within organs, on part of the lines; also absent: ADAM12, CNRIP1, FMN2; co-absent with the target |
| [[PAPPA]] | C | PAPPA activity raises MSC's level | lines that do not express PAPPA (33) vs lines expressing it (17) | 2.29× lower at baseline in the lines without PAPPA | 0.056 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: HTRA3, MSC-AS1, PDGFRB; co-absent with the target |
| [[IGFN1]] | C | IGFN1 activity raises MSC's level | lines that do not express IGFN1 (36) vs lines expressing it (14) | 2.89× lower at baseline in the lines without IGFN1 | 0.056 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: GLYATL2, LINC01411, PSG9; co-absent with the target |

### Downstream of this gene

*33 arrows, 33 of them with an alert ⚠; grade A 0, B 2, C 31. Shown: the 12 strongest; 21 more arrows (21 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CPEB2]] | B | MSC activity raises CPEB2's level | lines that do not express MSC (34) vs lines expressing it (16) | 2.26× lower at baseline in the lines without MSC | 0.036 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: ITGA4, MMP2, SPARC |
| [[SAMD9L]] | B | MSC activity raises SAMD9L's level | lines that do not express MSC (34) vs lines expressing it (16) | 3.51× lower at baseline in the lines without MSC | 0.083 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: ITGA4, MMP2, SPARC |
| [[MSC-AS1]] | C | MSC activity raises MSC-AS1's level | lines that do not express MSC (34) vs lines expressing it (16) | 15.51× lower at baseline in the lines without MSC | 7e-04 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: ITGA4, MMP2, SPARC; co-absent with the target |
| [[EBF1]] | C | MSC activity raises EBF1's level | lines that do not express MSC (34) vs lines expressing it (16) | 7.95× lower at baseline in the lines without MSC | 0.003 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: ITGA4, MMP2, SPARC; co-absent with the target |
| [[LINC01828]] | C | MSC activity raises LINC01828's level | lines that do not express MSC (34) vs lines expressing it (16) | 3.25× lower at baseline in the lines without MSC | 0.004 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: ITGA4, MMP2, SPARC; co-absent with the target |
| [[OR9Q1]] | C | MSC activity raises OR9Q1's level | lines that do not express MSC (34) vs lines expressing it (16) | 4.35× lower at baseline in the lines without MSC | 0.007 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: ITGA4, MMP2, SPARC; co-absent with the target |
| [[PAPPA]] | C | MSC activity raises PAPPA's level | lines that do not express MSC (34) vs lines expressing it (16) | 5.73× lower at baseline in the lines without MSC | 0.008 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: ITGA4, MMP2, SPARC; co-absent with the target |
| [[APBB1IP]] | C | MSC activity raises APBB1IP's level | lines that do not express MSC (34) vs lines expressing it (16) | 3.61× lower at baseline in the lines without MSC | 0.008 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: ITGA4, MMP2, SPARC; co-absent with the target |
| [[LINC00536]] | C | MSC activity raises LINC00536's level | lines that do not express MSC (34) vs lines expressing it (16) | 3.61× lower at baseline in the lines without MSC | 0.018 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: ITGA4, MMP2, SPARC; co-absent with the target |
| [[MIR548XHG]] | C | MSC activity raises MIR548XHG's level | lines that do not express MSC (34) vs lines expressing it (16) | 4.69× lower at baseline in the lines without MSC | 0.019 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: ITGA4, MMP2, SPARC; co-absent with the target |
| [[LINC00383]] | C | MSC activity raises LINC00383's level | lines that do not express MSC (34) vs lines expressing it (16) | 1.78× lower at baseline in the lines without MSC | 0.021 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: ITGA4, MMP2, SPARC; co-absent with the target |
| [[DOCK10]] | C | MSC activity raises DOCK10's level | lines that do not express MSC (34) vs lines expressing it (16) | 7.28× lower at baseline in the lines without MSC | 0.023 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: ITGA4, MMP2, SPARC; co-absent with the target |

## Where it sits

- **Module**: [[Module 014]] — TNF-alpha signaling via NF-kB; 212 genes; every member is in the + arm (projection on the module's main direction 0.585). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.20; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (39.2, 20.0); signed map (47.3, 23.1). **Vector** length 46.0, 15.3% of its response variance represented; |z| ≥ 3 in 325 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +2.5 | +2.4 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | +2.2 | -0.0 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | +1.9 | +2.6 |
|  | [[TAK-901 (drug)]] 5 µM |  | +1.9 | +3.3 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +1.8 | +7.3 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | +1.7 | +1.7 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +1.7 | +1.7 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +1.6 | +1.9 |
|  | [[Binimetinib (drug)]] 5 µM |  | +1.5 | +2.8 |
|  | [[Belumosudil (drug)]] 5 µM |  | +1.5 | +2.1 |
| fall | [[Dexamethasone (drug)]] 0.5 µM |  | -1.7 | -3.3 |
|  | [[Dexamethasone (drug)]] 0.05 µM |  | -1.4 | -1.5 |
|  | [[Dexamethasone (drug)]] 5 µM |  | -1.4 | -2.6 |
|  | [[Triamcinolone (drug)]] 0.5 µM |  | -1.3 | -0.5 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | -1.3 | -0.3 |

## What is on record

|  |  |
|---|---|
| Name | musculin |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 8q13.3 — chr8:71,841,560-71,844,412 (-) |
| Ensembl biotype | protein_coding |
| Also known as | ABF-1, bHLHa22 |
| Gene groups (HGNC) | Basic helix-loop-helix proteins |
| Hallmark sets | TNFA_SIGNALING_VIA_NFKB |
| Matched by | ensembl_id |

**Function**, from UniProt [O60682](https://www.uniprot.org/uniprotkb/O60682) (Musculin):

> Transcription repressor capable of inhibiting the transactivation capability of TCF3/E47. May play a role in regulating antigen-dependent B-cell differentiation.

**Summary**, from NCBI Gene [9242](https://www.ncbi.nlm.nih.gov/gene/9242):

> The protein encoded by this gene is a transcriptional repressor capable of binding an E-box element either as a homodimer or as a heterodimer with E2A in vitro. The encoded protein also forms heterodimers with E2A proteins in vivo. This protein is capable of inhibiting the transactivation capability of E47, an E2A protein, in mammalian cells. This gene is a downstream target of the B-cell receptor signal transduction pathway. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:7321](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:7321) · Entrez [9242](https://www.ncbi.nlm.nih.gov/gene/9242) · UniProt [O60682](https://www.uniprot.org/uniprotkb/O60682) · Ensembl [ENSG00000178860](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000178860)

## Data

Gene col 10966: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10966); `tables/drug_effects.parquet` (23 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10966, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10966]; `tensor/DDL_lfc|DDL_z.npy` [10966]; `embed/gene_vectors.npy` [10966]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10966 or target_col == 10966). Every well: [[MSC — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MSC.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
