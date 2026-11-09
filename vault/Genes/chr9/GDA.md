---
symbol: "GDA"
type: "gene"
col: 4040
ensembl_id: "ENSG00000119125"
name: "guanine deaminase"
location: "9q21.13"
module: 19
arm: "+"
pooled_cpm: 116.24
n_lines_expressing: 15
n_dd_up: 19
n_dd_down: 19
n_dd_up_clean: 14
n_dd_down_clean: 17
in_vector_space: true
direction_upstream: 32
direction_downstream: 57
tags: ["gene", "module/019"]
generated_by: "tahoemap"
---

# GDA

*guanine deaminase* — 9q21.13

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 19 drug-doses (5 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 3.04× (z +12.1, q 4e-31, up in 7 of 14 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Tucidinostat (drug)]] 5 µM: 1.61× (z +7.4, q 3e-11, up in 11 of 13 measured lines).
> Pooled over the cell lines (median), lowered significantly by 19 drug-doses (2 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 0.5 µM: 0.600× (z -5.5, q 2e-05, down in 6 of 13 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[GTF2I-AS1]] (+0.61, fdr 8e-06), [[LINC01508]] (+0.58, fdr 1e-05), [[SLC19A3]] (+0.58, fdr 1e-05); moves opposite to [[NPHP3]] (-0.43, fdr 1e-04).
> It is in [[Module 019]], a single-armed module (Neuronal System).
> Probable direction (from the cell lines, not proof of direct regulation): 32 arrows point to it, the strongest [[CHN2]] → it (grade B ⚠); 57 go from it, the strongest it → [[NOSTRIN]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 19 in all, 5 with an alert ⚠. 19 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4040.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **3.04×** | +12.1 | 4e-31 | 7/14 (HT-29, SW1417, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.47×** | +9.5 | 6e-19 | 7/12 (HT-29, SW1417, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here); composition shift; position effect removed |
| [[Tucidinostat (drug)]] 5 µM |  | **1.61×** | +7.4 | 3e-11 | 11/13 (A498, LoVo, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.98×** | +6.9 | 7e-10 | 4/12 (HT-29, SW1417, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here); composition shift; position effect removed |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.69×** | +5.7 | 1e-06 | 10/14 (A498, LS 180, …) | rises with dose | cell-cycle shift (explains ~1% here) |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.85×** | +4.7 | 2e-04 | 1/13 (HCT15) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.51×** | +4.3 | 0.001 | 6/13 (AsPC-1, SW1417, …) | top dose only | cell-cycle shift (explains ~8% here) |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **1.47×** | +4.2 | 0.002 | 6/13 (NCI-H460, HCT15, …) | inconsistent across doses |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.29×** | +4.0 | 0.004 | 0/14 | top dose only | cell-cycle shift (explains ~0% here) |
| [[Sunitinib (drug)]] 5 µM | ⚠ toxic | **1.40×** | +3.6 | 0.014 | 5/13 (AsPC-1, HCT15, …) | rises with dose | position effect removed |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.41×** | +3.6 | 0.014 | 0/15 | top dose only | cell-cycle shift (explains ~0% here) |
| [[AZD-7648 (drug)]] 0.5 µM |  | **1.53×** | +3.3 | 0.047 | 1/13 (AsPC-1) | two highest doses | low cells (technical?); noisy plate (z scaled) |
| [[L-Thyroxine (sodium salt pentahydrate) (drug)]] 5 µM |  | **1.35×** | +3.3 | 0.049 | 8/13 (LS 180, LoVo, …) | top dose only |  |
| [[Gemcitabine (drug)]] 0.5 µM |  | **1.34×** | +3.2 | 0.057 | 2/13 (HCT15, AsPC-1) | two highest doses | noisy plate (z scaled) |
| [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | **1.33×** | +3.1 | 0.063 | 0/13 | inconsistent across doses |  |
| [[Methylprednisolone succinate (drug)]] 0.5 µM |  | **1.49×** | +3.1 | 0.066 | 0/13 | inconsistent across doses | low cells (technical?); noisy plate (z scaled) |
| [[BAY1125976 (drug)]] 0.5 µM |  | **1.49×** | +3.1 | 0.066 | 0/13 | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Budesonide (drug)]] 0.05 µM |  | **1.32×** | +3.0 | 0.083 | 0/13 | inconsistent across doses |  |
| [[Lactate (calcium) (drug)]] 0.05 µM |  | **1.31×** | +3.0 | 0.087 | 3/13 (A498, NCI-H460, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 19 in all, 2 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 19 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 4040.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.600×** | -5.5 | 2e-05 | 6/13 (NCI-H460, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.615×** | -5.3 | 4e-05 | 10/13 (LoVo, KATO III, …) | all doses, flat |  |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.713×** | -5.2 | 4e-05 | 10/13 (NCI-H460, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | **0.602×** | -5.1 | 5e-05 | 3/13 (LoVo, NCI-H460, …) | inconsistent across doses |  |
| [[Harringtonine (drug)]] 5 µM |  | **0.621×** | -5.0 | 8e-05 | 6/13 (NCI-H460, A498, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[TAK-733 (drug)]] 0.05 µM |  | **0.648×** | -4.5 | 8e-04 | 6/13 (LS 180, HEC-1-A, …) | inconsistent across doses |  |
| [[Belinostat (drug)]] 5 µM |  | **0.664×** | -4.4 | 8e-04 | 9/13 (NCI-H460, KATO III, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.690×** | -4.0 | 0.004 | 12/13 (NCI-H460, KATO III, …) | rises with dose | cell-cycle shift (explains ~1% here); position effect removed |
| [[Larotrectinib (drug)]] 5 µM |  | **0.790×** | -3.6 | 0.016 | 11/13 (NCI-H2030, SW1417, …) | top dose only | position effect removed |
| [[Abemaciclib (drug)]] 5 µM |  | **0.483×** | -3.6 | 0.016 | 10/13 (KATO III, NCI-H460, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.718×** | -3.6 | 0.016 | 10/13 (NCI-H460, KATO III, …) | rises with dose | cell-cycle shift (explains ~2% here); position effect removed |
| [[Abemaciclib (drug)]] 0.5 µM |  | **0.627×** | -3.6 | 0.016 | 7/13 (NCI-H460, KATO III, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[TAK-733 (drug)]] 5 µM |  | **0.502×** | -3.4 | 0.026 | 6/13 (NCI-H460, KATO III, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Anethole trithione (drug)]] 0.5 µM |  | **0.730×** | -3.4 | 0.026 | 0/13 | rises with dose |  |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.736×** | -3.3 | 0.034 | 1/13 (NCI-H460) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[MK-8353 (drug)]] 0.5 µM |  | **0.655×** | -3.2 | 0.040 | 0/13 | inconsistent across doses | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.08 per unit of S-phase module lfc, +0.20 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4040. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 1,533 | 0 | 15 (4 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.0687× (z -24.9) |
| [[KATO III (line)]] | alt | 256 | 0 | 4 | — | [[Panobinostat (drug)]] 5 µM 0.106× (z -13.2) |
| [[A498 (line)]] | wt | 111 | 1 | 2 | [[Tucidinostat (drug)]] 5 µM 2.75× (z +8.9) | [[Homoharringtonine (drug)]] 5 µM 0.197× (z -14.2) |
| [[AsPC-1 (line)]] | alt | 179 | 0 | 2 | — | [[Panobinostat (drug)]] 0.5 µM 0.196× (z -10.2) |
| [[LoVo (line)]] | wt | 113 | 0 | 2 (1 ⚠) | — | [[Auranofin (drug)]] 5 µM 0.206× (z -10.4) |
| [[NCI-H2030 (line)]] | alt | 82.9 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.247× (z -12.2) |
| [[COLO 205 (line)]] | alt | 39.8 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.179× (z -11.5) |
| [[HEC-1-A (line)]] | alt | 161 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.422× (z -9.4) |
| [[LS 180 (line)]] | wt | 120 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.335× (z -9.8) |
| [[SW1417 (line)]] | alt | 82.5 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.433× (z -8.9) |
| [[A-172 (line)]] | wt | 9.97 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 7.55 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 10.6 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 23.3 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 9.19 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 12.6 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 10.4 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 51.2 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 13.7 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 27.4 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 29.7 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 11.0 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 11.6 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 10.3 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 12.2 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 44.0 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 15.2 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 8.45 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 13.6 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 7.67 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 13.6 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 18.3 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 63.9 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 14.6 n.m. | — | — | — | — |
| [[NCI-H2347 (line)]] | alt | 6.97 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 151 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 17.2 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 13.9 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 12.6 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 10.4 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 9.35 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 8.56 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 8.82 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 11.0 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 11.6 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 24.6 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 13.1 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 16.2 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 23.9 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 15.0 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4040), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*99 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GTF2I-AS1]] | +0.61 | +0.60 / +0.58 | both halves | 8e-06 |  |
| [[LINC01508]] | +0.58 | +0.54 / +0.55 | both halves | 1e-05 |  |
| [[SLC19A3]] | +0.58 | +0.53 / +0.53 | both halves | 1e-05 |  |
| [[CCDC68]] | +0.58 | +0.50 / +0.65 | both halves | 1e-05 |  |
| [[IL22RA1]] | +0.55 | +0.49 / +0.47 | both halves | 2e-05 |  |
| [[CTSE]] | +0.54 | +0.48 / +0.58 | both halves | 2e-05 | pathway: HALLMARK_COAGULATION |
| [[FGFBP1]] | +0.54 | +0.49 / +0.49 | both halves | 1e-05 |  |
| [[SPINK13]] | +0.54 | +0.52 / +0.38 | both halves | 6e-05 |  |
| [[SLITRK4]] | +0.53 | +0.52 / +0.51 | both halves | 1e-05 |  |
| [[SCARA5]] | +0.52 | +0.55 / +0.43 | both halves | 3e-05 |  |
| [[CDH17]] | +0.52 | +0.50 / +0.52 | both halves | 1e-05 |  |
| [[GPRIN3]] | +0.52 | +0.48 / +0.49 | both halves | 2e-05 |  |

## Genes that move opposite

*1 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NPHP3]] | -0.43 | -0.51 / -0.33 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*32 arrows, 32 of them with an alert ⚠; grade A 0, B 3, C 29. Shown: the 12 strongest; 20 more arrows (20 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CHN2]] | B | CHN2 activity raises GDA's level | lines that do not express CHN2 (20) vs lines expressing it (30) | 2.31× lower at baseline in the lines without CHN2 | 0.050 | ⚠ within organs, on part of the lines; also absent: CPVL, IL20RA, PRR15 |
| [[SPTLC3]] | B | SPTLC3 activity raises GDA's level | lines that do not express SPTLC3 (16) vs lines expressing it (34) | 2.22× lower at baseline in the lines without SPTLC3 | 0.052 | ⚠ within organs, on part of the lines; also absent: TMEM92-AS1, CXCL3, PTPRB; maybe low, not absent |
| [[NOSTRIN]] | B | NOSTRIN activity raises GDA's level | lines that do not express NOSTRIN (16) vs lines expressing it (34) | 2.67× lower at baseline in the lines without NOSTRIN | 0.057 | ⚠ within organs, on part of the lines; also absent: SLC9A2, SLPI, SULT2B1; maybe low, not absent |
| [[ZNF736P9Y]] | C | ZNF736P9Y activity raises GDA's level | lines that do not express ZNF736P9Y (40) vs lines expressing it (10) | 2.58× lower at baseline in the lines without ZNF736P9Y | 0.006 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: SPINK13, SUCNR1, ENSG00000260364; co-absent with the target |
| [[AKR1B10]] | C | AKR1B10 activity raises GDA's level | lines that do not express AKR1B10 (41) vs lines expressing it (9) | 5.60× lower at baseline in the lines without AKR1B10 | 0.008 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: FGFR2, GABRP, MUC17; co-absent with the target |
| [[MARCOL]], [[SPINK13]] | C | MARCOL, SPINK13 activity raises GDA's level | lines that do not express MARCOL, SPINK13 (45) vs lines expressing them (5) | 5.30× lower at baseline in the lines without MARCOL, SPINK13 | 0.009 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: TBXT, ENSG00000230258, ENSG00000230975; co-absent with the target; co-absent genes |
| [[MYOM3]] | C | MYOM3 activity raises GDA's level | lines that do not express MYOM3 (27) vs lines expressing it (23) | 3.64× lower at baseline in the lines without MYOM3 | 0.009 | ⚠ within organs, on part of the lines; also absent: HNF4A, EPS8L3, USH1C; co-absent with the target |
| [[LYZ]] | C | LYZ activity raises GDA's level | lines that do not express LYZ (40) vs lines expressing it (10) | 3.85× lower at baseline in the lines without LYZ | 0.011 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: GCNT3, TRIM31, MUC17; co-absent with the target |
| [[GPA33]] | C | GPA33 activity raises GDA's level | lines that do not express GPA33 (41) vs lines expressing it (9) | 3.98× lower at baseline in the lines without GPA33 | 0.013 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: PHGR1, NPSR1, CDH17; co-absent with the target |
| [[POF1B]] | C | POF1B activity raises GDA's level | lines that do not express POF1B (34) vs lines expressing it (16) | 3.66× lower at baseline in the lines without POF1B | 0.014 | ⚠ within organs, on part of the lines; also absent: S100P, ENSG00000287426, TRIM31; co-absent with the target |
| [[TSPAN8]] | C | TSPAN8 activity raises GDA's level | lines that do not express TSPAN8 (34) vs lines expressing it (16) | 3.81× lower at baseline in the lines without TSPAN8 | 0.014 | ⚠ within organs, on part of the lines; also absent: ENSG00000267881, SERPINB5, CDH17; co-absent with the target |
| [[NPSR1]] | C | NPSR1 activity raises GDA's level | lines that do not express NPSR1 (42) vs lines expressing it (8) | 5.24× lower at baseline in the lines without NPSR1 | 0.016 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: REG4, MUC17, CDH17; co-absent with the target |

### Downstream of this gene

*57 arrows, 57 of them with an alert ⚠; grade A 0, B 8, C 49. Shown: the 12 strongest; 45 more arrows (45 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[NOSTRIN]] | B | GDA activity raises NOSTRIN's level | lines that do not express GDA (35) vs lines expressing it (15) | 3.89× lower at baseline in the lines without GDA | 6e-04 | ⚠ within organs, on part of the lines; also absent: HHLA2, GPA33, LGALS4 |
| [[IL22RA1]] | B | GDA activity raises IL22RA1's level | lines that do not express GDA (35) vs lines expressing it (15) | 3.31× lower at baseline in the lines without GDA | 0.004 | ⚠ within organs, on part of the lines; also absent: HHLA2, GPA33, LGALS4 |
| [[SPTLC3]] | B | GDA activity raises SPTLC3's level | lines that do not express GDA (35) vs lines expressing it (15) | 1.91× lower at baseline in the lines without GDA | 0.011 | ⚠ within organs, on part of the lines; also absent: HHLA2, GPA33, LGALS4 |
| [[ZG16B]] | B | GDA activity raises ZG16B's level | lines that do not express GDA (35) vs lines expressing it (15) | 1.80× lower at baseline in the lines without GDA | 0.032 | ⚠ within organs, on part of the lines; also absent: HHLA2, GPA33, LGALS4 |
| [[NT5C2]] | B | GDA activity raises NT5C2's level | lines that do not express GDA (35) vs lines expressing it (15) | 1.42× lower at baseline in the lines without GDA | 0.060 | ⚠ within organs, on part of the lines; also absent: HHLA2, GPA33, LGALS4 |
| [[CHN2]] | B | GDA activity raises CHN2's level | lines that do not express GDA (35) vs lines expressing it (15) | 3.39× lower at baseline in the lines without GDA | 0.067 | ⚠ within organs, on part of the lines; also absent: HHLA2, GPA33, LGALS4 |
| [[HR]] | B | GDA activity raises HR's level | lines that do not express GDA (35) vs lines expressing it (15) | 1.78× lower at baseline in the lines without GDA | 0.079 | ⚠ within organs, on part of the lines; also absent: HHLA2, GPA33, LGALS4 |
| [[HTR1D]] | B | GDA activity raises HTR1D's level | lines that do not express GDA (35) vs lines expressing it (15) | 1.70× lower at baseline in the lines without GDA | 0.094 | ⚠ within organs, on part of the lines; also absent: HHLA2, GPA33, LGALS4 |
| [[TRIM31]] | C | GDA activity raises TRIM31's level | lines that do not express GDA (35) vs lines expressing it (15) | 5.43× lower at baseline in the lines without GDA | 0.002 | ⚠ within organs, on part of the lines; also absent: HHLA2, GPA33, LGALS4; co-absent with the target |
| [[TRIM15]] | C | GDA activity raises TRIM15's level | lines that do not express GDA (35) vs lines expressing it (15) | 4.75× lower at baseline in the lines without GDA | 0.003 | ⚠ within organs, on part of the lines; also absent: HHLA2, GPA33, LGALS4; co-absent with the target |
| [[CYP3A5]] | C | GDA activity raises CYP3A5's level | lines that do not express GDA (35) vs lines expressing it (15) | 6.60× lower at baseline in the lines without GDA | 0.003 | ⚠ within organs, on part of the lines; also absent: HHLA2, GPA33, LGALS4; co-absent with the target |
| [[MUC13]] | C | GDA activity raises MUC13's level | lines that do not express GDA (35) vs lines expressing it (15) | 6.38× lower at baseline in the lines without GDA | 0.004 | ⚠ within organs, on part of the lines; also absent: HHLA2, GPA33, LGALS4; co-absent with the target |

## Where it sits

- **Module**: [[Module 019]] — Neuronal System; 196 genes; every member is in the + arm (projection on the module's main direction 0.516). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.17; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (45.5, 38.7); signed map (45.5, 45.1). **Vector** length 66.7, 27.4% of its response variance represented; |z| ≥ 3 in 423 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +6.1 | +7.4 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +4.7 | +5.7 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +4.6 | +9.5 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +4.5 | +12.1 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +3.9 | +6.9 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.6 | +2.2 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | +1.6 | +1.5 |
|  | [[Arbutin (drug)]] 0.05 µM |  | +1.3 | +1.8 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.3 | +4.7 |
| fall | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -3.7 | -5.3 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -2.7 | -3.6 |
|  | [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift | -2.3 | -2.6 |
|  | [[TAK-733 (drug)]] 5 µM |  | -2.3 | -3.4 |
|  | [[EX229 (drug)]] 5 µM |  | -1.9 | -2.6 |
|  | [[Abemaciclib (drug)]] 0.5 µM |  | -1.9 | -3.6 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -1.9 | -2.3 |

## What is on record

|  |  |
|---|---|
| Name | guanine deaminase |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 9q21.13 — chr9:72,114,595-72,257,193 (+) |
| Ensembl biotype | protein_coding |
| Also known as | CYPIN, GAH |
| Gene groups (HGNC) | M38 metallopeptidases |
| Hallmark sets | COAGULATION |
| Reactome | 3 pathways, smallest: Purine catabolism; Nucleotide catabolism; Metabolism of nucleotides |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9Y2T3](https://www.uniprot.org/uniprotkb/Q9Y2T3) (Guanine deaminase):

> Catalyzes the hydrolytic deamination of guanine, producing xanthine and ammonia.

**Summary**, from NCBI Gene [9615](https://www.ncbi.nlm.nih.gov/gene/9615):

> This gene encodes an enzyme responsible for the hydrolytic deamination of guanine. Studies in rat ortholog suggest this gene plays a role in microtubule assembly. Multiple transcript variants encoding different isoforms have been found for this gene. [provided by RefSeq, Nov 2011]

**Accessions** — [HGNC:4212](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:4212) · Entrez [9615](https://www.ncbi.nlm.nih.gov/gene/9615) · UniProt [Q9Y2T3](https://www.uniprot.org/uniprotkb/Q9Y2T3) · Ensembl [ENSG00000119125](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000119125)

## Data

Gene col 4040: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4040); `tables/drug_effects.parquet` (38 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4040, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4040]; `tensor/DDL_lfc|DDL_z.npy` [4040]; `embed/gene_vectors.npy` [4040]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4040 or target_col == 4040). Every well: [[GDA — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/GDA.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
