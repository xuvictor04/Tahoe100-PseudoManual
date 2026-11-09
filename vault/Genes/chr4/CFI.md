---
symbol: "CFI"
type: "gene"
col: 12975
ensembl_id: "ENSG00000205403"
name: "complement factor I"
location: "4q25"
module: 152
arm: "+"
pooled_cpm: 6.18
n_lines_expressing: 19
n_dd_up: 18
n_dd_down: 9
n_dd_up_clean: 12
n_dd_down_clean: 9
in_vector_space: true
direction_upstream: 19
direction_downstream: 29
tags: ["gene", "module/152"]
generated_by: "tahoemap"
---

# CFI

*complement factor I* — 4q25

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 18 drug-doses (6 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 4.16× (z +12.7, q 4e-34, up in 8 of 8 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.80× (z +7.7, q 1e-12, up in 2 of 16 measured lines).
> Pooled over the cell lines (median), lowered significantly by 9 drug-doses (none with an alert); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.585× (z -7.0, q 2e-09, down in 15 of 16 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[AGT]] (+0.65, fdr 1e-05), [[TF]] (+0.61, fdr 1e-05), [[A2M]] (+0.58, fdr 1e-05); moves opposite to [[C11orf80]] (-0.46, fdr 8e-05), [[STK10]] (-0.44, fdr 4e-05).
> It is in [[Module 152]], a single-armed module (Retinoid metabolism and transport).
> Probable direction (from the cell lines, not proof of direct regulation): 19 arrows point to it, the strongest [[MAP2K1]] → it (grade B ⚠); 29 go from it, the strongest it → [[SV2A]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 18 in all, 6 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 18 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 12975.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **4.16×** | +12.7 | 4e-34 | 8/8 (A498, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **3.80×** | +12.4 | 1e-32 | 9/13 (A498, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **3.04×** | +9.5 | 3e-19 | 7/10 (A498, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.80×** | +7.7 | 1e-12 | 2/16 (HOP62, A498) | top dose only | cell-cycle shift (explains ~8% here) |
| [[Cobimetinib (drug)]] 5 µM |  | **1.95×** | +6.0 | 2e-07 | 9/15 (A498, CFPAC-1, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 5 µM |  | **1.49×** | +5.2 | 2e-05 | 6/17 (NCI-H2347, A498, …) | all doses, stronger at high dose |  |
| [[Cobimetinib (drug)]] 0.5 µM |  | **1.74×** | +5.2 | 2e-05 | 11/16 (A498, HepG2/C3A, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.73×** | +5.1 | 2e-05 | 5/16 (NCI-H2347, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Trametinib (drug)]] 0.5 µM |  | **1.49×** | +4.2 | 0.002 | 8/16 (CFPAC-1, A498, …) | two highest doses | noisy plate (z scaled) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.34×** | +3.8 | 0.008 | 0/17 | top dose only |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.49×** | +3.6 | 0.018 | 1/15 (HOP62) | top dose only | cell-cycle shift (explains ~18% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.44×** | +3.4 | 0.029 | 1/11 (C32) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Binimetinib (drug)]] 5 µM |  | **1.43×** | +3.3 | 0.050 | 6/17 (CFPAC-1, A498, …) | all doses, flat | noisy plate (z scaled) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | **1.40×** | +3.1 | 0.071 | 5/17 (A498, SW480, …) | inconsistent across doses |  |
| [[AZD2858 (drug)]] 0.5 µM | ⚠ toxic | **1.66×** | +3.1 | 0.071 | 1/11 (NCI-H2347) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Binimetinib (drug)]] 0.05 µM |  | **1.27×** | +3.1 | 0.071 | 7/17 (CFPAC-1, SW480, …) | all doses, flat |  |
| [[Selinexor (drug)]] 5 µM |  | **1.26×** | +3.1 | 0.071 | 3/17 (SW 900, HOP62, …) | all doses, flat | low cells (technical?); cell-cycle shift (explains ~9% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, none with an alert. 9 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 12975.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.585×** | -7.0 | 2e-09 | 15/16 (H4, C32, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.595×** | -4.8 | 5e-04 | 14/16 (CFPAC-1, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.617×** | -4.3 | 0.004 | 11/16 (C32, SW 900, …) | rises with dose | cell-cycle shift (explains ~6% here); composition shift |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.655×** | -3.9 | 0.014 | 9/15 (C32, HepG2/C3A, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[BAY1125976 (drug)]] 5 µM |  | **0.484×** | -3.5 | 0.053 | 2/16 (HepG2/C3A, CFPAC-1) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.687×** | -3.4 | 0.054 | 6/15 (CHP-212, J82, …) | inconsistent across doses | cell-cycle shift (explains ~1% here); position effect removed |
| [[Tofacitinib (drug)]] 5 µM |  | **0.778×** | -3.2 | 0.084 | 9/17 (C32, HepG2/C3A, …) | top dose only |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.702×** | -3.2 | 0.084 | 8/16 (C32, NCI-H1792, …) | rises with dose | cell-cycle shift (explains ~3% here) |
| [[Tofacitinib (citrate) (drug)]] 5 µM |  | **0.783×** | -3.2 | 0.096 | 5/17 (C32, HepG2/C3A, …) | rises with dose |  |
| [[Peretinoin (drug)]] 5 µM |  | 0.708× | -3.0 | 0.13 | 6/15 (C32, HepG2/C3A, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.20 per unit of S-phase module lfc, -0.14 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 12975. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[C32 (line)]] | wt | 84.0 | 0 | 5 | — | [[Homoharringtonine (drug)]] 5 µM 0.165× (z -18.0) |
| [[A498 (line)]] | wt | 21.4 | 1 (1 ⚠) | 3 | [[Dinaciclib (drug)]] 0.5 µM 3.16× (z +8.5) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.246× (z -14.6) |
| [[CFPAC-1 (line)]] | alt | 20.7 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.135× (z -17.4) |
| [[H4 (line)]] | wt | 37.7 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.0489× (z -24.4) |
| [[HepG2_C3A (line)]] | wt | 76.1 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.135× (z -16.8) |
| [[HOP62 (line)]] | alt | 2.32 | 0 | 1 (1 ⚠) | — | [[Fostamatinib (disodium hexahydrate) (drug)]] 5 µM 0.0536× (z -9.3) ⚠ unreliable plate only |
| [[SHP-77 (line)]] | alt | 20.2 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.115× (z -15.9) |
| [[SW 900 (line)]] | alt | 13.0 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.147× (z -8.5) |
| [[A-172 (line)]] | wt | 1.50 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 0.536 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 0.649 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 3.49 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 0.996 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 0.666 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 0.874 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 29.6 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 0.933 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 0.884 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 1.14 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 0.790 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 1.20 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 1.05 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 6.55 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 2.63 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 0.912 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 1.04 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 1.24 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 1.17 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.673 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 0.686 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 18.2 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 0.628 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 9.33 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 0.597 n.m. | — | — | — | — |
| [[NCI-H2347 (line)]] | alt | 3.96 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 0.681 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 8.80 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 1.03 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 1.96 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 0.553 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 0.727 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 1.44 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 1.30 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 0.777 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 0.800 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 17.4 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 0.942 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 0.871 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 0.839 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 1.84 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 12975), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*98 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[AGT]] | +0.65 | +0.68 / +0.54 | both halves | 1e-05 | **novel candidate** |
| [[TF]] | +0.61 | +0.51 / +0.59 | both halves | 1e-05 | pathway: HALLMARK_COAGULATION |
| [[A2M]] | +0.58 | +0.53 / +0.57 | both halves | 1e-05 | pathway: HALLMARK_COAGULATION; STRING 502 |
| [[NREP]] | +0.57 | +0.50 / +0.58 | both halves | 1e-05 |  |
| [[MOXD1]] | +0.57 | +0.54 / +0.56 | both halves | 1e-05 |  |
| [[APOD]] | +0.57 | +0.50 / +0.30 | both halves | 2e-04 | **novel candidate** |
| [[PCDHB2]] | +0.56 | +0.56 / +0.44 | both halves | 3e-05 |  |
| [[EPHA3]] | +0.55 | +0.54 / +0.58 | both halves | 1e-05 |  |
| [[ANGPT1]] | +0.55 | +0.48 / +0.57 | both halves | 2e-05 |  |
| [[PI15]] | +0.54 | +0.38 / +0.54 | both halves | 7e-05 |  |
| [[LRP2]] | +0.54 | +0.47 / +0.54 | both halves | 2e-05 |  |
| [[SPARC]] | +0.54 | +0.47 / +0.52 | both halves | 2e-05 | pathway: HALLMARK_COAGULATION |

## Genes that move opposite

*2 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[C11orf80]] | -0.46 | -0.37 / -0.46 | both halves | 8e-05 |  |
| [[STK10]] | -0.44 | -0.43 / -0.41 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*19 arrows, 19 of them with an alert ⚠; grade A 0, B 2, C 17. Shown: the 12 strongest; 7 more arrows (7 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MAP2K1]] | B | MAP2K1 activity lowers CFI's level | compounds that target MAP2K1: 3 of 4 raise it (Binimetinib, Cobimetinib, Trametinib) | 75% of the class's compounds vs 3.4% of all compounds | 0.067 | ⚠ off-target possible; 3 compounds |
| [[TOP2A]] | B | TOP2A activity lowers CFI's level | compounds that target TOP2A: 3 of 5 raise it (Doxorubicin, Idarubicin, Mitoxantrone) | 60% of the class's compounds vs 3.4% of all compounds | 0.095 | ⚠ off-target possible; 3 compounds; artifact flags |
| [[SNTB1]] | C | SNTB1 activity raises CFI's level | lines that do not express SNTB1 (19) vs lines expressing it (31) | 3.07× lower at baseline in the lines without SNTB1 | 0.003 | ⚠ within organs, on part of the lines; also absent: IL1R2, ENSG00000227486, ENSG00000254979; co-absent with the target |
| [[SOX5]] | C | SOX5 activity raises CFI's level | lines that do not express SOX5 (24) vs lines expressing it (26) | 3.49× lower at baseline in the lines without SOX5 | 0.007 | ⚠ within organs, on part of the lines; also absent: CTHRC1, MOXD1, AK5; co-absent with the target |
| [[CPE]] | C | CPE activity raises CFI's level | lines that do not express CPE (28) vs lines expressing it (22) | 2.63× lower at baseline in the lines without CPE | 0.007 | ⚠ within organs, on part of the lines; also absent: PEX5L, SLC7A2, NPFFR2; co-absent with the target |
| [[AGT]] | C | AGT activity raises CFI's level | lines that do not express AGT (33) vs lines expressing it (17) | 2.86× lower at baseline in the lines without AGT | 0.009 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: AMBP, RIT2, SOX11; co-absent with the target |
| [[RUNX1T1]] | C | RUNX1T1 activity raises CFI's level | lines that do not express RUNX1T1 (38) vs lines expressing it (12) | 3.31× lower at baseline in the lines without RUNX1T1 | 0.026 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: DPP10, ENSG00000232252, SYT4; co-absent with the target |
| [[FKBP9P1-1]] | C | FKBP9P1-1 activity raises CFI's level | lines that do not express FKBP9P1-1 (30) vs lines expressing it (20) | 1.90× lower at baseline in the lines without FKBP9P1-1 | 0.032 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: ENSG00000231317, ENSG00000253642, ENSG00000287622; maybe low, not absent; co-absent with the target |
| [[HLA-DRA]] | C | HLA-DRA activity raises CFI's level | lines that do not express HLA-DRA (39) vs lines expressing it (11) | 2.43× lower at baseline in the lines without HLA-DRA | 0.032 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: HLA-DRB1, SOX10, ENSG00000287530; co-absent with the target |
| [[PPP2R2B]] | C | PPP2R2B activity raises CFI's level | lines that do not express PPP2R2B (23) vs lines expressing it (27) | 2.89× lower at baseline in the lines without PPP2R2B | 0.040 | ⚠ within organs, on part of the lines; also absent: SSTR2, COL5A1, MCAM; maybe low, not absent; co-absent with the target |
| [[PPARGC1A]] | C | PPARGC1A activity raises CFI's level | lines that do not express PPARGC1A (27) vs lines expressing it (23) | 2.37× lower at baseline in the lines without PPARGC1A | 0.043 | ⚠ within organs, on part of the lines; also absent: ZBTB7C, PCK1, ILDR2; co-absent with the target |
| [[LOXL4]] | C | LOXL4 activity raises CFI's level | lines that do not express LOXL4 (30) vs lines expressing it (20) | 2.10× lower at baseline in the lines without LOXL4 | 0.046 | ⚠ within organs, on part of the lines; also absent: HSD17B2, BATF, TFF3; co-absent with the target |

### Downstream of this gene

*29 arrows, 29 of them with an alert ⚠; grade A 0, B 9, C 20. Shown: the 12 strongest; 17 more arrows (17 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SV2A]] | B | CFI activity raises SV2A's level | lines that do not express CFI (31) vs lines expressing it (19) | 3.08× lower at baseline in the lines without CFI | 0.003 | ⚠ within organs, on part of the lines; also absent: ENSG00000285330, ENSG00000239268, RUNX1T1 |
| [[FKBP9P1]] | B | CFI activity raises FKBP9P1's level | lines that do not express CFI (31) vs lines expressing it (19) | 1.59× lower at baseline in the lines without CFI | 0.013 | ⚠ within organs, on part of the lines; also absent: ENSG00000285330, ENSG00000239268, RUNX1T1 |
| [[CYP27A1]] | B | CFI activity raises CYP27A1's level | lines that do not express CFI (31) vs lines expressing it (19) | 1.94× lower at baseline in the lines without CFI | 0.016 | ⚠ within organs, on part of the lines; also absent: ENSG00000285330, ENSG00000239268, RUNX1T1 |
| [[NYAP2]] | B | CFI activity raises NYAP2's level | lines that do not express CFI (31) vs lines expressing it (19) | 2.41× lower at baseline in the lines without CFI | 0.020 | ⚠ within organs, on part of the lines; also absent: ENSG00000285330, ENSG00000239268, RUNX1T1 |
| [[DIRC3]] | B | CFI activity raises DIRC3's level | lines that do not express CFI (31) vs lines expressing it (19) | 2.70× lower at baseline in the lines without CFI | 0.027 | ⚠ within organs, on part of the lines; also absent: ENSG00000285330, ENSG00000239268, RUNX1T1 |
| [[RAB17]] | B | CFI activity raises RAB17's level | lines that do not express CFI (31) vs lines expressing it (19) | 1.22× lower at baseline in the lines without CFI | 0.050 | ⚠ within organs, on part of the lines; also absent: ENSG00000285330, ENSG00000239268, RUNX1T1 |
| [[NELL1]] | B | CFI activity raises NELL1's level | lines that do not express CFI (31) vs lines expressing it (19) | 1.80× lower at baseline in the lines without CFI | 0.078 | ⚠ within organs, on part of the lines; also absent: ENSG00000285330, ENSG00000239268, RUNX1T1 |
| [[TET1]] | B | CFI activity raises TET1's level | lines that do not express CFI (31) vs lines expressing it (19) | 2.36× lower at baseline in the lines without CFI | 0.089 | ⚠ within organs, on part of the lines; also absent: ENSG00000285330, ENSG00000239268, RUNX1T1 |
| [[LRP2]] | B | CFI activity raises LRP2's level | lines that do not express CFI (31) vs lines expressing it (19) | 1.53× lower at baseline in the lines without CFI | 0.098 | ⚠ within organs, on part of the lines; also absent: ENSG00000285330, ENSG00000239268, RUNX1T1 |
| [[SNTB1]] | C | CFI activity raises SNTB1's level | lines that do not express CFI (31) vs lines expressing it (19) | 2.22× lower at baseline in the lines without CFI | 0.002 | ⚠ within organs, on part of the lines; also absent: ENSG00000285330, ENSG00000239268, RUNX1T1; co-absent with the target |
| [[FKBP9P1-1]] | C | CFI activity raises FKBP9P1-1's level | lines that do not express CFI (31) vs lines expressing it (19) | 2.16× lower at baseline in the lines without CFI | 0.005 | ⚠ within organs, on part of the lines; also absent: ENSG00000285330, ENSG00000239268, RUNX1T1; co-absent with the target |
| [[SMIM10]] | C | CFI activity raises SMIM10's level | lines that do not express CFI (31) vs lines expressing it (19) | 2.27× lower at baseline in the lines without CFI | 0.007 | ⚠ within organs, on part of the lines; also absent: ENSG00000285330, ENSG00000239268, RUNX1T1; co-absent with the target |

## Where it sits

- **Module**: [[Module 152]] — Retinoid metabolism and transport; 29 genes; every member is in the + arm (projection on the module's main direction 0.568). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (51.0, 29.6); signed map (30.0, 40.5). **Vector** length 48.8, 14.0% of its response variance represented; |z| ≥ 3 in 414 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +5.8 | +12.4 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +5.7 | +9.5 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +5.6 | +12.7 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +4.0 | +7.7 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +4.0 | +5.2 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +2.4 | +6.0 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.0 | +3.8 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +1.9 | +4.2 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | +1.8 | +2.0 |
| fall | [[Harringtonine (drug)]] 0.5 µM |  | -2.3 | -3.2 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -2.0 | -1.6 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -1.9 | -2.8 |
|  | [[Harringtonine (drug)]] 5 µM |  | -1.7 | -4.3 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -1.6 | -4.8 |
|  | [[BAY1125976 (drug)]] 5 µM |  | -1.5 | -3.5 |
|  | [[Sapanisertib (drug)]] 5 µM |  | -1.3 | -2.2 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -1.3 | -1.4 |

## What is on record

|  |  |
|---|---|
| Name | complement factor I |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 4q25 — chr4:109,731,008-109,802,150 (-) |
| Ensembl biotype | protein_coding |
| Also known as | FI, C3b-INA, C3bINA, KAF; previously IF |
| Gene groups (HGNC) | Serine proteases; Scavenger receptor cysteine rich domain containing; Complement system regulators and receptors |
| Hallmark sets | COAGULATION |
| Reactome | 3 pathways, smallest: Regulation of Complement cascade; Complement cascade; Innate Immune System |
| Matched by | ensembl_id |

**Function**, from UniProt [P05156](https://www.uniprot.org/uniprotkb/P05156) (Complement factor I):

> Trypsin-like serine protease that plays an essential role in regulating the immune response by controlling all complement pathways. Inhibits these pathways by cleaving three peptide bonds in the alpha-chain of C3b and two bonds in the alpha-chain of C4b thereby inactivating these proteins. Essential cofactors for these reactions include factor H and C4BP in the fluid phase and membrane cofactor protein/CD46 and CR1 on cell surfaces. The presence of these cofactors on healthy cells allows …

**Summary**, from NCBI Gene [3426](https://www.ncbi.nlm.nih.gov/gene/3426):

> This gene encodes a serine proteinase that is essential for regulating the complement cascade. The encoded preproprotein is cleaved to produce both heavy and light chains, which are linked by disulfide bonds to form a heterodimeric glycoprotein. This heterodimer can cleave and inactivate the complement components C4b and C3b, and it prevents the assembly of the C3 and C5 convertase enzymes. Defects in this gene cause complement factor I deficiency, an autosomal recessive disease associated with …

**Accessions** — [HGNC:5394](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:5394) · Entrez [3426](https://www.ncbi.nlm.nih.gov/gene/3426) · UniProt [P05156](https://www.uniprot.org/uniprotkb/P05156) · Ensembl [ENSG00000205403](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000205403)

## Data

Gene col 12975: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 12975); `tables/drug_effects.parquet` (28 rows, flagged included); `relations/gene_relations.parquet` (col_a == 12975, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 12975]; `tensor/DDL_lfc|DDL_z.npy` [12975]; `embed/gene_vectors.npy` [12975]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 12975 or target_col == 12975). Every well: [[CFI — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CFI.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
