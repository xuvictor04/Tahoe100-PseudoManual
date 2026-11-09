---
symbol: "SYNPO2"
type: "gene"
col: 10251
ensembl_id: "ENSG00000172403"
name: "synaptopodin 2"
location: "4q26"
module: 150
arm: "+"
pooled_cpm: 4.27
n_lines_expressing: 45
n_dd_up: 40
n_dd_down: 0
n_dd_up_clean: 35
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 8
direction_downstream: 7
tags: ["gene", "module/150"]
generated_by: "tahoemap"
---

# SYNPO2

*synaptopodin 2* — 4q26

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 40 drug-doses (5 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 11.9× (z +33.4, q 0e+00, up in 31 of 33 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Daptomycin (drug)]] 5 µM in 1 line (CHP-212 0.107×; ⚠ unreliable plate only); [[Vinblastine (sulfate) (drug)]] 5 µM in 1 line (CHP-212 0.214×); [[Simotinib (drug)]] 0.05 µM in 1 line (NCI-H1573 0.0700×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ARHGAP15]] (+0.76, fdr 7e-06), [[GUCY1A2]] (+0.75, fdr 7e-06), [[CFAP54]] (+0.74, fdr 7e-06); moves opposite to [[HERC2P2]] (-0.61, fdr 4e-05).
> It is in [[Module 150]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 8 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); 7 go from it, the strongest it → [[LINC02306]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 40 in all, 5 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 40 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10251.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **11.9×** | +33.4 | 0e+00 | 31/33 (HOP62, A-172, …) | rises with dose | cell-cycle shift (explains ~3% here); position effect removed |
| [[Auranofin (drug)]] 5 µM |  | **8.23×** | +20.1 | 0e+00 | 31/37 (SW480, LoVo, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 5 µM |  | **3.46×** | +16.7 | 0e+00 | 27/34 (NCI-H460, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **4.97×** | +14.7 | 0e+00 | 24/30 (HOP62, HS-578T, …) | top dose only | cell-cycle shift (explains ~7% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **4.43×** | +13.6 | 4e-40 | 27/34 (HOP62, SW480, …) | top dose only | cell-cycle shift (explains ~6% here); position effect removed |
| [[Panobinostat (drug)]] 5 µM |  | **4.16×** | +13.6 | 6e-40 | 31/40 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **2.54×** | +12.5 | 5e-34 | 24/41 (HOP62, A-172, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **3.01×** | +10.5 | 9e-24 | 26/34 (NCI-H460, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **2.99×** | +10.4 | 1e-23 | 26/39 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **2.10×** | +10.0 | 1e-21 | 25/41 (NCI-H460, SW480, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.92×** | +9.8 | 6e-21 | 1/8 (hTERT-HPNE) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here); composition shift |
| [[Belinostat (drug)]] 5 µM |  | **2.53×** | +8.8 | 5e-17 | 23/38 (SW480, PANC-1, …) | top dose only | cell-cycle shift (explains ~13% here) |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **2.17×** | +7.4 | 7e-12 | 24/38 (HEC-1-A, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~8% here); position effect removed |
| [[Harringtonine (drug)]] 5 µM |  | **2.23×** | +7.3 | 9e-12 | 13/38 (HS-578T, hTERT-HPNE, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **2.12×** | +7.1 | 3e-11 | 18/40 (HS-578T, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 5 µM |  | **1.69×** | +7.0 | 9e-11 | 15/41 (A498, A-427, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~5% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 2 in all, none with an alert. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 10251.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Daptomycin (drug)]] 5 µM in 1 line (CHP-212 0.107×; ⚠ unreliable plate only); [[Vinblastine (sulfate) (drug)]] 5 µM in 1 line (CHP-212 0.214×); [[Simotinib (drug)]] 0.05 µM in 1 line (NCI-H1573 0.0700×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Niclosamide (olamine) (drug)]] 0.5 µM |  | 0.680× | -3.7 | 0.12 | 6/40 (A-427, HepG2/C3A, …) | inconsistent across doses |  |
| [[Digitoxin (drug)]] 0.05 µM |  | 0.706× | -3.3 | 0.28 | 12/38 (NCI-H23, CHP-212, …) | inconsistent across doses | cell-cycle shift (explains ~1% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.31 per unit of S-phase module lfc, -0.20 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10251. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 1.25 | 4 | 0 | [[Auranofin (drug)]] 5 µM 50.4× (z +10.9) | — |
| [[C32 (line)]] | wt | 2.45 | 3 | 0 | [[Auranofin (drug)]] 5 µM 59.8× (z +9.7) | — |
| [[HOP62 (line)]] | alt | 2.29 | 3 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 29.4× (z +13.5) | — |
| [[LoVo (line)]] | wt | 2.58 | 3 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 13.8× (z +11.4) | — |
| [[NCI-H460 (line)]] | wt | 4.93 | 3 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 7.75× (z +12.2) | — |
| [[A-172 (line)]] | wt | 3.66 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 18.7× (z +12.5) | — |
| [[A498 (line)]] | wt | 7.36 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.91× (z +9.9) | — |
| [[CHP-212 (line)]] | wt | 123 | 0 | 2 (1 ⚠) | — | [[Daptomycin (drug)]] 5 µM 0.107× (z -9.3) ⚠ unreliable plate only · without an alert: [[Vinblastine (sulfate) (drug)]] 5 µM 0.214× (z -9.1) |
| [[HEC-1-A (line)]] | alt | 1.95 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 25.4× (z +12.0) | — |
| [[HS-578T (line)]] | alt | 4.56 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 16.3× (z +11.9) | — |
| [[hTERT-HPNE (line)]] | wt | 15.0 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.45× (z +9.0) | — |
| [[NCI-H1573 (line)]] | alt | 5.57 | 1 | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.68× (z +9.7) | [[Simotinib (drug)]] 0.05 µM 0.0700× (z -8.9) |
| [[CFPAC-1 (line)]] | alt | 7.31 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 8.26× (z +10.3) | — |
| [[HT-29 (line)]] | alt | 1.19 | 1 | 0 | [[Auranofin (drug)]] 5 µM 111× (z +9.5) | — |
| [[J82 (line)]] | alt | 3.99 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 8.92× (z +10.0) | — |
| [[NCI-H2030 (line)]] | alt | 7.08 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.73× (z +9.9) | — |
| [[NCI-H2347 (line)]] | alt | 5.12 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.03× (z +9.2) | — |
| [[PANC-1 (line)]] | alt | 1.66 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 9.95× (z +10.0) | — |
| [[SK-MEL-2 (line)]] | alt | 2.87 | 1 | 0 | [[Auranofin (drug)]] 5 µM 35.0× (z +9.6) | — |
| [[SNU-423 (line)]] | alt | 2.23 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 22.3× (z +11.2) | — |
| [[SW 900 (line)]] | alt | 2.88 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 14.4× (z +9.0) | — |
| [[A-427 (line)]] | wt | 29.7 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 2.03 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 1.26 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 1.13 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 1.46 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 4.69 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 3.52 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 7.22 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 1.22 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 1.16 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 1.47 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 1.18 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 1.01 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 0.836 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.921 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 3.33 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 4.54 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 3.40 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 5.48 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 37.0 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 1.81 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 1.90 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 5.62 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 1.04 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 0.906 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 10.4 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 1.84 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 1.25 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 1.26 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10251), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*99 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ARHGAP15]] | +0.76 | +0.78 / +0.58 | both halves | 7e-06 |  |
| [[GUCY1A2]] | +0.75 | +0.75 / +0.65 | both halves | 7e-06 |  |
| [[CFAP54]] | +0.74 | +0.73 / +0.59 | both halves | 7e-06 |  |
| [[SP140]] | +0.73 | +0.72 / +0.59 | both halves | 7e-06 |  |
| [[LINC02268]] | +0.73 | +0.73 / +0.62 | both halves | 7e-06 |  |
| [[NEB]] | +0.73 | +0.76 / +0.63 | both halves | 7e-06 |  |
| [[COL21A1]] | +0.72 | +0.69 / +0.72 | both halves | 7e-06 |  |
| [[SYT16]] | +0.71 | +0.76 / +0.54 | both halves | 1e-05 |  |
| [[TRIM69]] | +0.71 | +0.77 / +0.47 | both halves | 2e-05 |  |
| [[FAT3]] | +0.71 | +0.69 / +0.60 | both halves | 7e-06 |  |
| [[DYNLRB2-AS1]] | +0.70 | +0.65 / +0.64 | both halves | 7e-06 |  |
| [[KCNT2]] | +0.70 | +0.72 / +0.59 | both halves | 7e-06 |  |

## Genes that move opposite

*1 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[HERC2P2]] | -0.61 | -0.41 / -0.54 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*8 arrows, 8 of them with an alert ⚠; grade A 0, B 7, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers SYNPO2's level | compounds that target TOP2A: 5 of 5 raise it (Amsacrine, Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 100% of the class's compounds vs 6.4% of all compounds | 0.008 | ⚠ off-target possible; 5 compounds; artifact flags |
| [[LINC01687]] | B | LINC01687 activity raises SYNPO2's level | lines that do not express LINC01687 (31) vs lines expressing it (19) | 1.72× lower at baseline in the lines without LINC01687 | 0.020 | ⚠ within organs, on part of the lines; also absent: ENSG00000226043, LINC02616, TPTE |
| [[TLL1]] | B | TLL1 activity raises SYNPO2's level | lines that do not express TLL1 (28) vs lines expressing it (22) | 2.21× lower at baseline in the lines without TLL1 | 0.032 | ⚠ within organs, on part of the lines; also absent: GUCY1A1, CDH6, COL1A1; maybe low, not absent |
| [[LINC02240]] | B | LINC02240 activity raises SYNPO2's level | lines that do not express LINC02240 (35) vs lines expressing it (15) | 1.92× lower at baseline in the lines without LINC02240 | 0.046 | ⚠ within organs, on part of the lines; co-occurs with KRAS, TP53; also absent: LINC02941, CHL1, EDNRB; maybe low, not absent |
| [[RERG]] | B | RERG activity raises SYNPO2's level | lines that do not express RERG (24) vs lines expressing it (26) | 1.39× lower at baseline in the lines without RERG | 0.066 | ⚠ within organs, on part of the lines; also absent: NPFFR2, MGAT4C, ENSG00000266450; maybe low, not absent |
| [[BMPR1B]] | B | BMPR1B activity raises SYNPO2's level | lines that do not express BMPR1B (28) vs lines expressing it (22) | 2.34× lower at baseline in the lines without BMPR1B | 0.069 | ⚠ within organs, on part of the lines; also absent: ENSG00000286385, SLC6A17, EPHA5-AS1 |
| [[PAPLN]] | B | PAPLN activity raises SYNPO2's level | lines that do not express PAPLN (16) vs lines expressing it (34) | 2.13× lower at baseline in the lines without PAPLN | 0.099 | ⚠ within organs, on part of the lines; also absent: BEX2, AFAP1L1, BEX4; maybe low, not absent |
| [[COL28A1]] | C | COL28A1 activity lowers SYNPO2's level | lines that do not express COL28A1 (3) vs lines expressing it (47) | 3.52× higher at baseline in the lines without COL28A1 | 0.089 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: DNAJC6, KIFC3, MLLT3; maybe low, not absent; its own permutation p |

### Downstream of this gene

*7 arrows, 7 of them with an alert ⚠; grade A 0, B 7, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[LINC02306]] | B | SYNPO2 activity lowers LINC02306's level | lines that do not express SYNPO2 (5) vs lines expressing it (45) | 2.61× higher at baseline in the lines without SYNPO2 | 0.008 | ⚠ within organs, on part of the lines; also absent: RIPOR3, PER3, TESK2; maybe low, not absent |
| [[RIPK2-DT]] | B | SYNPO2 activity raises RIPK2-DT's level | lines that do not express SYNPO2 (5) vs lines expressing it (45) | 2.04× lower at baseline in the lines without SYNPO2 | 0.018 | ⚠ within organs, on part of the lines; also absent: RIPOR3, PER3, TESK2; maybe low, not absent |
| [[LINC02492]] | B | SYNPO2 activity lowers LINC02492's level | lines that do not express SYNPO2 (5) vs lines expressing it (45) | 2.55× higher at baseline in the lines without SYNPO2 | 0.040 | ⚠ within organs, on part of the lines; also absent: RIPOR3, PER3, TESK2; maybe low, not absent |
| [[NEB]] | B | SYNPO2 activity lowers NEB's level | lines that do not express SYNPO2 (5) vs lines expressing it (45) | 1.60× higher at baseline in the lines without SYNPO2 | 0.081 | ⚠ within organs, on part of the lines; also absent: RIPOR3, PER3, TESK2; maybe low, not absent |
| [[RGS7]] | B | SYNPO2 activity lowers RGS7's level | lines that do not express SYNPO2 (5) vs lines expressing it (45) | 2.09× higher at baseline in the lines without SYNPO2 | 0.089 | ⚠ within organs, on part of the lines; also absent: RIPOR3, PER3, TESK2; maybe low, not absent |
| [[UNC79]] | B | SYNPO2 activity lowers UNC79's level | lines that do not express SYNPO2 (5) vs lines expressing it (45) | 1.86× higher at baseline in the lines without SYNPO2 | 0.091 | ⚠ within organs, on part of the lines; also absent: RIPOR3, PER3, TESK2; maybe low, not absent |
| [[HCP5]] | B | SYNPO2 activity raises HCP5's level | lines that do not express SYNPO2 (5) vs lines expressing it (45) | 3.09× lower at baseline in the lines without SYNPO2 | 0.093 | ⚠ within organs, on part of the lines; also absent: RIPOR3, PER3, TESK2; maybe low, not absent |

## Where it sits

- **Module**: [[Module 150]]; 30 genes; every member is in the + arm (projection on the module's main direction 0.802). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (25.6, 25.0); signed map (37.7, 15.0). **Vector** length 65.0, 10.8% of its response variance represented; |z| ≥ 3 in 1,136 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +9.4 | +33.4 |
|  | [[Auranofin (drug)]] 5 µM |  | +8.6 | +20.1 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +8.0 | +9.8 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +7.5 | +7.1 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +7.2 | +7.0 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +6.1 | +12.5 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +5.7 | +10.0 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +3.0 | +6.5 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | +2.6 | +3.1 |
| fall | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.2 | -0.4 |
|  | [[Belinostat (drug)]] 5 µM |  | -2.1 | +8.8 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -1.9 | -1.5 |
|  | [[Digitoxin (drug)]] 0.05 µM |  | -1.8 | -3.3 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | -1.8 | +0.9 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -1.6 | -0.4 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | -1.6 | -1.5 |
|  | [[Dexamethasone (drug)]] 5 µM |  | -1.5 | -2.0 |

## What is on record

|  |  |
|---|---|
| Name | synaptopodin 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 4q26 — chr4:118,850,688-119,061,247 (+) |
| Ensembl biotype | protein_coding |
| Also known as | MYOPODIN |
| Gene groups (HGNC) | PDZ domain containing |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9UMS6](https://www.uniprot.org/uniprotkb/Q9UMS6) (Synaptopodin-2):

> Has an actin-binding and actin-bundling activity. Can induce the formation of F-actin networks in an isoform-specific manner. At the sarcomeric Z lines is proposed to act as adapter protein that links nascent myofibers to the sarcolemma via ZYX and may play a role in early assembly and stabilization of the Z lines. Involved in autophagosome formation. May play a role in chaperone-assisted selective autophagy (CASA) involved in Z lines maintenance in striated muscle under mechanical tension; may …

**Summary**, from NCBI Gene [171024](https://www.ncbi.nlm.nih.gov/gene/171024):

> Enables alpha-actinin binding activity and filamin binding activity. Involved in obsolete regulation of Rho-dependent protein serine/threonine kinase activity; positive regulation of actin filament bundle assembly; and positive regulation of cell migration. Located in Z disc; focal adhesion; and stress fiber. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:17732](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:17732) · Entrez [171024](https://www.ncbi.nlm.nih.gov/gene/171024) · UniProt [Q9UMS6](https://www.uniprot.org/uniprotkb/Q9UMS6) · Ensembl [ENSG00000172403](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000172403)

## Data

Gene col 10251: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10251); `tables/drug_effects.parquet` (42 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10251, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10251]; `tensor/DDL_lfc|DDL_z.npy` [10251]; `embed/gene_vectors.npy` [10251]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10251 or target_col == 10251). Every well: [[SYNPO2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SYNPO2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
