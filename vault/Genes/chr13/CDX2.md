---
symbol: "CDX2"
type: "gene"
col: 9145
ensembl_id: "ENSG00000165556"
name: "caudal type homeobox 2"
location: "13q12.2"
module: 27
arm: "+"
pooled_cpm: 3.72
n_lines_expressing: 23
n_dd_up: 21
n_dd_down: 0
n_dd_up_clean: 10
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 12
direction_downstream: 3
tags: ["gene", "module/027"]
generated_by: "tahoemap"
---

# CDX2

*caudal type homeobox 2* — 13q12.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 21 drug-doses (11 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 4.55× (z +10.0, q 8e-21, up in 0 of 3 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Trametinib (drug)]] 0.5 µM: 1.82× (z +4.4, q 0.001, up in 7 of 21 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 6 here, 2 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Auranofin (drug)]] 5 µM in 3 lines (SHP-77 0.0355×, HCT15 0.0465×, LoVo 0.143×); [[Homoharringtonine (drug)]] 0.5 µM in 1 line (COLO 205 0.0331×; ⚠ cell-cycle shift, explains ~59% of this change); [[Panobinostat (drug)]] 0.5 µM in 1 line (SW1417 0.215×; ⚠ cell-cycle shift, explains ~79% of this change); [[Digitoxin (drug)]] 0.5 µM in 1 line (COLO 205 0.0370×); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (COLO 205 0.101×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[A1CF]] (+0.70, fdr 7e-06), [[C11orf52]] (+0.69, fdr 7e-06), [[BCL2L15]] (+0.67, fdr 9e-06); moves opposite to [[ITGB1BP1]] (-0.51, fdr 3e-05).
> It is in [[Module 027]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 12 arrows point to it, the strongest [[FGL1]] → it (grade B ⚠); 3 go from it, the strongest it → [[KSR2]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 21 in all, 11 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 21 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 11 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9145.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **4.55×** | +10.0 | 8e-21 | 0/3 | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **3.08×** | +7.2 | 2e-10 | 0/6 | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.80×** | +7.1 | 3e-10 | 0/10 | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.91×** | +4.5 | 0.001 | 6/15 (SW1417, SHP-77, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~15% here); position effect removed |
| [[Trametinib (drug)]] 0.5 µM |  | **1.82×** | +4.4 | 0.001 | 7/21 (LoVo, LS 180, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~38% of this change | **1.57×** | +4.4 | 0.001 | 5/17 (KATO III, LS 180, …) | rises with dose | composition shift |
| [[Selinexor (drug)]] 5 µM |  | **1.56×** | +4.3 | 0.001 | 5/21 (SW1417, SW48, …) | top dose only | low cells (technical?); cell-cycle shift (explains ~0% here); position effect removed |
| [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM |  | **1.73×** | +3.8 | 0.011 | 1/18 (KATO III) | inconsistent across doses | low cells (technical?) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **1.76×** | +3.7 | 0.012 | 8/21 (LoVo, LS 180, …) | rises with dose |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.72×** | +3.6 | 0.018 | 3/16 (NCI-H1573, CFPAC-1, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Cobimetinib (drug)]] 5 µM |  | **1.70×** | +3.5 | 0.023 | 9/20 (LoVo, LS 180, …) | all doses, stronger at high dose |  |
| [[Imiquimod (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.66×** | +3.5 | 0.024 | 2/19 (HT-29, NCI-H1573) | top dose only |  |
| [[Binimetinib (drug)]] 5 µM |  | **1.68×** | +3.4 | 0.028 | 7/21 (LoVo, LS 180, …) | all doses, flat | noisy plate (z scaled) |
| [[Elimusertib hydrochloride (drug)]] 0.05 µM |  | **1.69×** | +3.4 | 0.028 | 8/20 (LoVo, LS 180, …) | inconsistent across doses | position effect removed |
| [[Simotinib (drug)]] 5 µM | ⚠ toxic | **1.67×** | +3.4 | 0.028 | 4/17 (RKO, HT-29, …) | top dose only |  |
| [[Belinostat (drug)]] 0.5 µM |  | **1.63×** | +3.3 | 0.029 | 6/20 (LS 180, SW1417, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Binimetinib (drug)]] 0.5 µM |  | **1.53×** | +3.2 | 0.046 | 7/21 (LS 180, LoVo, …) | all doses, flat | noisy plate (z scaled) |
| [[XRK3F2 (drug)]] 0.5 µM |  | **2.43×** | +3.1 | 0.063 | 2/12 (LS 180, LoVo) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 2 in all, none with an alert. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 9145.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 6 here, 2 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Auranofin (drug)]] 5 µM in 3 lines (SHP-77 0.0355×, HCT15 0.0465×, LoVo 0.143×); [[Homoharringtonine (drug)]] 0.5 µM in 1 line (COLO 205 0.0331×; ⚠ cell-cycle shift, explains ~59% of this change); [[Panobinostat (drug)]] 0.5 µM in 1 line (SW1417 0.215×; ⚠ cell-cycle shift, explains ~79% of this change); [[Digitoxin (drug)]] 0.5 µM in 1 line (COLO 205 0.0370×); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (COLO 205 0.101×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[S-Adenosyl-L-methionine (disulfate tosylate) (drug)]] 5 µM |  | 0.721× | -3.2 | 0.51 | 5/21 (CFPAC-1, COLO 205, …) | rises with dose | position effect removed |
| [[Digitoxin (drug)]] 0.5 µM |  | 0.635× | -3.1 | 0.51 | 10/21 (COLO 205, HT-29, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.37 per unit of S-phase module lfc, +0.34 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9145. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[COLO 205 (line)]] | alt | 9.16 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0331× (z -9.3) ⚠ cell-cycle shift, explains ~59% of this change · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.0370× (z -9.0) |
| [[LoVo (line)]] | wt | 20.4 | 1 (1 ⚠) | 1 | [[Trametinib (drug)]] 5 µM 4.74× (z +8.6) ⚠ cell-cycle shift, explains ~35% of this change | [[Auranofin (drug)]] 5 µM 0.143× (z -9.6) |
| [[HCT15 (line)]] | alt | 12.9 | 0 | 1 | — | [[Auranofin (drug)]] 5 µM 0.0465× (z -9.8) |
| [[KATO III (line)]] | alt | 8.48 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 6.96× (z +11.9) ⚠ cell-cycle shift, explains ~38% of this change | — |
| [[SHP-77 (line)]] | alt | 7.60 | 0 | 1 | — | [[Auranofin (drug)]] 5 µM 0.0355× (z -11.1) |
| [[SW1417 (line)]] | alt | 23.7 | 0 | 1 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.215× (z -9.1) ⚠ cell-cycle shift, explains ~79% of this change |
| [[A-172 (line)]] | wt | 0.306 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 2.20 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 0.238 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 0.411 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 0.587 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 2.61 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 0.314 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 0.409 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 0.288 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 1.06 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 0.424 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 0.309 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 0.340 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 0.327 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 0.317 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 0.274 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 0.275 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 2.29 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 0.408 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 0.294 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 0.390 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 30.6 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 1.46 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 1.33 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 0.779 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 2.89 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 2.25 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 2.23 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 0.345 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 0.277 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 3.54 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 0.594 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 0.794 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 1.57 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 6.22 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 0.278 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 0.260 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 7.43 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 0.353 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 0.652 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 0.328 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 2.39 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 13.7 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 4.45 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9145), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*99 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[A1CF]] | +0.70 | +0.61 / +0.71 | both halves | 7e-06 | **novel candidate** |
| [[C11orf52]] | +0.69 | +0.65 / +0.58 | both halves | 7e-06 |  |
| [[BCL2L15]] | +0.67 | +0.69 / +0.57 | both halves | 9e-06 |  |
| [[RSPH1]] | +0.67 | +0.66 / +0.67 | both halves | 7e-06 |  |
| [[CHDH]] | +0.66 | +0.65 / +0.56 | both halves | 1e-05 |  |
| [[HNF1A-AS1]] | +0.66 | +0.60 / +0.62 | both halves | 7e-06 |  |
| [[RASSF6]] | +0.66 | +0.64 / +0.60 | both halves | 7e-06 |  |
| [[MGC32805]] | +0.66 | +0.59 / +0.70 | both halves | 7e-06 |  |
| [[AXIN2]] | +0.66 | +0.62 / +0.63 | both halves | 7e-06 | STRING 445 |
| [[KCNE3]] | +0.66 | +0.58 / +0.67 | both halves | 7e-06 |  |
| [[ILDR1]] | +0.66 | +0.58 / +0.68 | both halves | 8e-06 |  |
| [[PRR15]] | +0.65 | +0.60 / +0.65 | both halves | 7e-06 |  |

## Genes that move opposite

*1 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ITGB1BP1]] | -0.51 | -0.48 / -0.45 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*12 arrows, 12 of them with an alert ⚠; grade A 0, B 3, C 9.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[FGL1]] | B | FGL1 activity lowers CDX2's level | lines that do not express FGL1 (39) vs lines expressing it (11) | 1.04× higher at baseline in the lines without FGL1 | 0.062 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: SYT4, AFP, CALCA |
| [[RSPH1]] | B | RSPH1 activity raises CDX2's level | lines that do not express RSPH1 (13) vs lines expressing it (37) | 2.22× lower at baseline in the lines without RSPH1 | 0.079 | ⚠ within organs, on part of the lines; co-occurs with TERT; also absent: SLC37A1, ABCG1, SHROOM3; maybe low, not absent |
| [[MAP2K1]] | B | MAP2K1 activity lowers CDX2's level | compounds that target MAP2K1: 3 of 4 raise it (Binimetinib, Cobimetinib, Trametinib) | 75% of the class's compounds vs 4.5% of all compounds | 0.095 | ⚠ off-target possible; 3 compounds |
| [[SORL1]] | C | SORL1 activity raises CDX2's level | lines that do not express SORL1 (21) vs lines expressing it (29) | 2.35× lower at baseline in the lines without SORL1 | 0.030 | ⚠ within organs, on part of the lines; also absent: PRR15-DT, PLEKHG6, SLC52A3; co-absent with the target |
| [[LINC01748]] | C | LINC01748 activity raises CDX2's level | lines that do not express LINC01748 (34) vs lines expressing it (16) | 2.66× lower at baseline in the lines without LINC01748 | 0.037 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: CALB1, ATP10B, CLRN3; co-absent with the target |
| [[SAMD12]] | C | SAMD12 activity raises CDX2's level | lines that do not express SAMD12 (20) vs lines expressing it (30) | 2.55× lower at baseline in the lines without SAMD12 | 0.049 | ⚠ within organs, on part of the lines; also absent: MST1R, STYK1, ENSG00000263325; co-absent with the target |
| [[MYB]] | C | MYB activity raises CDX2's level | lines that do not express MYB (24) vs lines expressing it (26) | 2.34× lower at baseline in the lines without MYB | 0.054 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: NOS3, CKMT1B, LINC01748; co-absent with the target |
| [[NOTUM]] | C | NOTUM activity raises CDX2's level | lines that do not express NOTUM (31) vs lines expressing it (19) | 2.10× lower at baseline in the lines without NOTUM | 0.070 | ⚠ within organs, on part of the lines; also absent: FGF20, AXIN2, XKR7; co-absent with the target |
| [[NPNT]] | C | NPNT activity raises CDX2's level | lines that do not express NPNT (33) vs lines expressing it (17) | 2.91× lower at baseline in the lines without NPNT | 0.073 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: PRSS8, RAB25, TMPRSS4; co-absent with the target |
| [[BMP7]] | C | BMP7 activity raises CDX2's level | lines that do not express BMP7 (23) vs lines expressing it (27) | 1.72× lower at baseline in the lines without BMP7 | 0.073 | ⚠ within organs, on part of the lines; also absent: NFASC, ENSG00000291189, KIF1A; co-absent with the target |
| [[MGC32805]] | C | MGC32805 activity raises CDX2's level | lines that do not express MGC32805 (32) vs lines expressing it (18) | 1.97× lower at baseline in the lines without MGC32805 | 0.081 | ⚠ within organs, on part of the lines; also absent: CEACAM5, ST18, PRR15L; maybe low, not absent; co-absent with the target |
| [[FAAH2]] | C | FAAH2 activity raises CDX2's level | lines that do not express FAAH2 (26) vs lines expressing it (24) | 2.65× lower at baseline in the lines without FAAH2 | 0.092 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: CDH1, TNNT2, ST14; maybe low, not absent; co-absent with the target |

### Downstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 2, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[KSR2]] | B | CDX2 activity raises KSR2's level | lines that do not express CDX2 (27) vs lines expressing it (23) | 2.70× lower at baseline in the lines without CDX2 | 0.026 | ⚠ within organs, on part of the lines; also absent: FAM83F, CKMT1A, ENSG00000225680 |
| [[HSD11B2]] | B | CDX2 activity raises HSD11B2's level | lines that do not express CDX2 (27) vs lines expressing it (23) | 2.05× lower at baseline in the lines without CDX2 | 0.094 | ⚠ within organs, on part of the lines; also absent: FAM83F, CKMT1A, ENSG00000225680 |
| [[RNF43]] | C | CDX2 activity raises RNF43's level | lines that do not express CDX2 (27) vs lines expressing it (23) | 4.57× lower at baseline in the lines without CDX2 | 0.094 | ⚠ within organs, on part of the lines; also absent: FAM83F, CKMT1A, ENSG00000225680; co-absent with the target |

## Where it sits

- **Module**: [[Module 027]]; 155 genes; every member is in the + arm (projection on the module's main direction 0.624). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.24; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (27.2, 48.6); signed map (56.7, 3.1). **Vector** length 55.0, 14.2% of its response variance represented; |z| ≥ 3 in 516 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~38% of this change | +3.0 | +4.4 |
|  | [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | +2.4 | +4.5 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | +2.3 | +2.3 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +2.1 | +10.0 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +2.1 | +2.7 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +1.9 | +4.4 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +1.9 | +3.1 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +1.8 | +3.5 |
|  | [[Bimiralisib (drug)]] 0.5 µM |  | +1.7 | +2.1 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +1.7 | +2.4 |
| fall | [[Auranofin (drug)]] 5 µM |  | -1.4 | +0.7 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -1.3 | -1.5 |
|  | [[Dabrafenib (drug)]] 5 µM |  | -1.2 | -1.4 |
|  | [[TAK-733 (drug)]] 0.05 µM |  | -1.1 | -1.7 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | -1.1 | -3.1 |
|  | [[Abemaciclib (drug)]] 0.5 µM |  | -1.0 | -1.5 |

## What is on record

|  |  |
|---|---|
| Name | caudal type homeobox 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 13q12.2 — chr13:27,960,918-27,969,315 (-) |
| Ensembl biotype | protein_coding |
| Also known as | ; previously CDX3 |
| Gene groups (HGNC) | HOXL subclass homeoboxes |
| Reactome | 5 pathways, smallest: POU5F1 (OCT4), SOX2, NANOG repress genes related to differentiation; Synthesis, secretion, and inactivation of Glucagon-like Peptide-1 (GLP-1); Incretin synthesis, secretion, and inactivation |
| Matched by | ensembl_id |

**Function**, from UniProt [Q99626](https://www.uniprot.org/uniprotkb/Q99626) (Homeobox protein CDX-2):

> Transcription factor which regulates the transcription of multiple genes expressed in the intestinal epithelium (By similarity). Binds to the promoter of the intestinal sucrase-isomaltase SI and activates SI transcription (By similarity). Binds to the DNA sequence 5'-ATAAAAACTTAT-3' in the promoter region of VDR and activates VDR transcription (By similarity). Binds to and activates transcription of LPH (By similarity). Activates transcription of CLDN2 and intestinal mucin MUC2 (By similarity). …

**Summary**, from NCBI Gene [1045](https://www.ncbi.nlm.nih.gov/gene/1045):

> This gene is a member of the caudal-related homeobox transcription factor gene family. The encoded protein is a major regulator of intestine-specific genes involved in cell growth an differentiation. This protein also plays a role in early embryonic development of the intestinal tract. Aberrant expression of this gene is associated with intestinal inflammation and tumorigenesis. [provided by RefSeq, Jan 2012]

**Accessions** — [HGNC:1806](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:1806) · Entrez [1045](https://www.ncbi.nlm.nih.gov/gene/1045) · UniProt [Q99626](https://www.uniprot.org/uniprotkb/Q99626) · Ensembl [ENSG00000165556](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000165556)

## Data

Gene col 9145: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9145); `tables/drug_effects.parquet` (23 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9145, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9145]; `tensor/DDL_lfc|DDL_z.npy` [9145]; `embed/gene_vectors.npy` [9145]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9145 or target_col == 9145). Every well: [[CDX2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CDX2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
