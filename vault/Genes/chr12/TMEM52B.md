---
symbol: "TMEM52B"
type: "gene"
col: 9167
ensembl_id: "ENSG00000165685"
name: "transmembrane protein 52B"
location: "12p13.2"
module: 66
arm: "+"
pooled_cpm: 2.7
n_lines_expressing: 11
n_dd_up: 25
n_dd_down: 0
n_dd_up_clean: 12
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 3
direction_downstream: 4
tags: ["gene", "module/066"]
generated_by: "tahoemap"
---

# TMEM52B

*transmembrane protein 52B* — 12p13.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 25 drug-doses (13 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 3.41× (z +10.8, q 3e-24, up in 6 of 8 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 4 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Panobinostat (drug)]] 5 µM in 2 lines (A-427 0.139×, NCI-H23 0.0730×; ⚠ cell-cycle shift, explains ~55% of this change); [[Belinostat (drug)]] 5 µM in 2 lines (A-427 0.198×, NCI-H23 0.164×; ⚠ cell-cycle shift, explains ~54% of this change); [[Panobinostat (drug)]] 0.5 µM in 1 line (A-427 0.122×; ⚠ cell-cycle shift, explains ~23% of this change).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[OLR1]] (+0.82, fdr 7e-06, ⚠ same locus), [[C1QTNF1-AS1]] (+0.75, fdr 1e-05), [[KCNT2]] (+0.61, fdr 1e-05), [[KMO]] (+0.60, fdr 3e-05); moves opposite to [[MLPH]] (-0.50, fdr 5e-05), [[P3H1]] (-0.49, fdr 1e-04).
> It is in [[Module 066]], a single-armed module (epithelial mesenchymal transition).
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[CXCL3]] → it (grade B ⚠); 4 go from it, the strongest it → [[OLR1]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 25 in all, 13 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 25 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 13 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9167.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **3.41×** | +10.8 | 3e-24 | 6/8 (J82, HOP62, …) | rises with dose | cell-cycle shift (explains ~7% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **5.89×** | +10.6 | 9e-24 | 2/2 (J82, A-427) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **5.12×** | +10.1 | 6e-22 | 3/5 (J82, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **4.61×** | +8.8 | 2e-16 | 1/3 (J82) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **3.02×** | +6.6 | 5e-09 | 5/8 (J82, HOP62, …) | rises with dose | cell-cycle shift (explains ~7% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.01×** | +6.1 | 9e-08 | 2/8 (J82, HOP62) | top dose only | cell-cycle shift (explains ~0% here); position effect removed |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **2.26×** | +5.0 | 4e-05 | 0/5 | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~9% here) |
| [[AZD2858 (drug)]] 0.5 µM | ⚠ toxic | **3.11×** | +5.0 | 4e-05 | 0/3 | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Selinexor (drug)]] 5 µM |  | **1.74×** | +4.8 | 8e-05 | 4/8 (A-172, HOP62, …) | top dose only | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.13×** | +4.7 | 2e-04 | 4/7 (J82, A-172, …) | rises with dose | cell-cycle shift (explains ~9% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **2.15×** | +4.5 | 3e-04 | 4/6 (J82, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Nimesulide (drug)]] 5 µM | ⚠ toxic; unreliable plate only | **2.07×** | +4.5 | 3e-04 | 1/7 (SW480) | inconsistent across doses |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.86×** | +3.8 | 0.006 | 0/7 | top dose only | cell-cycle shift (explains ~5% here) |
| [[XRK3F2 (drug)]] 0.5 µM |  | **2.36×** | +3.8 | 0.006 | 1/4 (A-427) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.85×** | +3.6 | 0.011 | 0/6 | top dose only | cell-cycle shift (explains ~3% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.76×** | +3.4 | 0.028 | 2/6 (J82, HOP62) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Dapagliflozin ((2S)-1,2-propanediol, hydrate) (drug)]] 0.05 µM |  | **1.78×** | +3.3 | 0.032 | 1/6 (HCT15) | inconsistent across doses |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **1.66×** | +3.1 | 0.057 | 5/8 (J82, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.42×** | +3.0 | 0.066 | 0/8 | rises with dose |  |
| [[GSK1059615 (drug)]] 0.5 µM |  | **1.96×** | +3.0 | 0.076 | 1/6 (A-427) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Bimiralisib (drug)]] 0.5 µM |  | **1.93×** | +2.9 | 0.089 | 1/7 (A-427) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

No drug-dose lowers it in the pooled data (pooled over the cell lines, median: none with |z| ≥ 3 or q < 0.10). A response seen in fewer than about half of the measured lines does not reach the pooled data; see [[#In which cell lines]].

In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 4 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Panobinostat (drug)]] 5 µM in 2 lines (A-427 0.139×, NCI-H23 0.0730×; ⚠ cell-cycle shift, explains ~55% of this change); [[Belinostat (drug)]] 5 µM in 2 lines (A-427 0.198×, NCI-H23 0.164×; ⚠ cell-cycle shift, explains ~54% of this change); [[Panobinostat (drug)]] 0.5 µM in 1 line (A-427 0.122×; ⚠ cell-cycle shift, explains ~23% of this change).

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.14 per unit of S-phase module lfc, +0.21 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9167. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[J82 (line)]] | alt | 22.0 | 5 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 13.0× (z +18.3) | — |
| [[A-427 (line)]] | wt | 42.5 | 0 | 4 (4 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.122× (z -13.6) ⚠ cell-cycle shift, explains ~23% of this change |
| [[HOP62 (line)]] | alt | 2.26 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 53.5× (z +12.5) | — |
| [[NCI-H23 (line)]] | alt | 30.5 | 0 | 2 (2 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.0730× (z -12.7) ⚠ cell-cycle shift, explains ~55% of this change |
| [[A-172 (line)]] | wt | 1.04 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 19.7× (z +8.6) | — |
| [[A498 (line)]] | wt | 0.792 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 0.642 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 0.483 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 0.375 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 0.590 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 0.418 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 0.393 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 0.347 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 0.436 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 0.352 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 0.614 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 9.73 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 0.376 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 0.367 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 0.488 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 0.431 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 0.392 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 0.502 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 0.372 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 0.369 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 0.385 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 0.315 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.332 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 0.424 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 0.367 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 0.473 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 1.03 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 0.318 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 0.452 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 1.61 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 0.414 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 0.403 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 0.347 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 0.346 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 0.382 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 0.353 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 0.362 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 0.359 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 0.435 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 0.675 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 0.448 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 0.450 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 0.444 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 0.371 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 0.953 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9167), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*98 of its nearest partners move with it, 2 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[OLR1]] | +0.82 | +0.80 / +0.80 | both halves | 7e-06 | STRING 614; ⚠ same locus (0.0 kb: neighbours can correlate without regulation) |
| [[C1QTNF1-AS1]] | +0.75 | +0.57 / +0.69 | both halves | 1e-05 |  |
| [[KCNT2]] | +0.61 | +0.56 / +0.51 | both halves | 1e-05 |  |
| [[KMO]] | +0.60 | +0.45 / +0.59 | both halves | 3e-05 |  |
| [[TCEAL1]] | +0.59 | +0.48 / +0.47 | both halves | 2e-05 |  |
| [[TRIML2]] | +0.59 | +0.55 / +0.42 | both halves | 4e-05 |  |
| [[LINC00882]] | +0.59 | +0.58 / +0.48 | both halves | 2e-05 |  |
| [[C7orf31]] | +0.59 | +0.55 / +0.36 | both halves | 1e-04 |  |
| [[ZFHX4-AS1]] | +0.59 | +0.65 / +0.37 | both halves | 8e-05 |  |
| [[IL32]] | +0.58 | +0.47 / +0.51 | both halves | 2e-05 |  |
| [[LRP1B]] | +0.58 | +0.41 / +0.56 | both halves | 4e-05 |  |
| [[SLC2A6]] | +0.58 | +0.53 / +0.53 | both halves | 1e-05 |  |
| [[EPHA5]] | +0.58 | +0.49 / +0.49 | both halves | 1e-05 |  |

## Genes that move opposite

*2 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MLPH]] | -0.50 | -0.48 / -0.40 | both halves | 5e-05 |  |
| [[P3H1]] | -0.49 | -0.48 / -0.35 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 1, C 2.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CXCL3]] | B | CXCL3 activity lowers TMEM52B's level | lines that do not express CXCL3 (14) vs lines expressing it (36) | 1.54× higher at baseline in the lines without CXCL3 | 0.055 | ⚠ within organs, on part of the lines; also absent: MGLL, SPTLC3, PCED1B |
| [[OLR1]] | C | OLR1 activity raises TMEM52B's level | lines that do not express OLR1 (40) vs lines expressing it (10) | 3.94× lower at baseline in the lines without OLR1 | 0.010 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: TMEM52B, ENSG00000230258, PSG9; co-absent with the target |
| [[TRIM58]] | C | TRIM58 activity raises TMEM52B's level | lines that do not express TRIM58 (31) vs lines expressing it (19) | 1.98× lower at baseline in the lines without TRIM58 | 0.076 | ⚠ within organs, on part of the lines; also absent: ENSG00000235749, MME, FGF20; co-absent with the target |

### Downstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 0, C 4.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[OLR1]] | C | TMEM52B activity raises OLR1's level | lines that do not express TMEM52B (39) vs lines expressing it (11) | 6.80× lower at baseline in the lines without TMEM52B | 0.005 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: OLR1, HOXD11, ENSG00000230258; co-absent with the target |
| [[HOXD11]] | C | TMEM52B activity raises HOXD11's level | lines that do not express TMEM52B (39) vs lines expressing it (11) | 4.65× lower at baseline in the lines without TMEM52B | 0.021 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: OLR1, HOXD11, ENSG00000230258; co-absent with the target |
| [[TRIM58]] | C | TMEM52B activity raises TRIM58's level | lines that do not express TMEM52B (39) vs lines expressing it (11) | 2.03× lower at baseline in the lines without TMEM52B | 0.058 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: OLR1, HOXD11, ENSG00000230258; co-absent with the target |
| [[LINC01010]] | C | TMEM52B activity raises LINC01010's level | lines that do not express TMEM52B (39) vs lines expressing it (11) | 1.30× lower at baseline in the lines without TMEM52B | 0.063 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: OLR1, HOXD11, ENSG00000230258; co-absent with the target |

## Where it sits

- **Module**: [[Module 066]] — epithelial mesenchymal transition; 74 genes; every member is in the + arm (projection on the module's main direction 0.437). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (32.7, 24.7); signed map (43.6, 17.7). **Vector** length 31.2, 11.0% of its response variance represented; |z| ≥ 3 in 204 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +2.6 | +10.1 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +2.6 | +8.8 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +2.5 | +10.8 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +2.5 | +10.6 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +2.2 | +6.1 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +1.9 | +2.8 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +1.7 | +3.0 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +1.0 | +2.4 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | +1.0 | +2.0 |
|  | [[Binimetinib (drug)]] 5 µM |  | +0.9 | +1.6 |
| fall | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~54% of this change | -1.0 | -0.6 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | -0.9 | -1.0 |
|  | [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift | -0.8 | -0.1 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~55% of this change | -0.8 | -0.8 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~23% of this change | -0.8 | -1.3 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -0.7 | -1.2 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | -0.7 | +0.6 |
|  | [[BAY1125976 (drug)]] 5 µM |  | -0.6 | -1.8 |
|  | [[Clobetasol propionate (drug)]] 5 µM |  | -0.6 | -1.6 |

## What is on record

|  |  |
|---|---|
| Name | transmembrane protein 52B |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 12p13.2 — chr12:10,170,542-10,191,804 (+) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ31166; previously C12orf59 |
| Matched by | ensembl_id |

UniProt [Q4KMG9](https://www.uniprot.org/uniprotkb/Q4KMG9) carries no function annotation.

**Summary**, from NCBI Gene [120939](https://www.ncbi.nlm.nih.gov/gene/120939):

> Located in extracellular exosome. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:26438](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:26438) · Entrez [120939](https://www.ncbi.nlm.nih.gov/gene/120939) · UniProt [Q4KMG9](https://www.uniprot.org/uniprotkb/Q4KMG9) · Ensembl [ENSG00000165685](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000165685)

## Data

Gene col 9167: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9167); `tables/drug_effects.parquet` (25 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9167, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9167]; `tensor/DDL_lfc|DDL_z.npy` [9167]; `embed/gene_vectors.npy` [9167]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9167 or target_col == 9167). Every well: [[TMEM52B — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TMEM52B.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
