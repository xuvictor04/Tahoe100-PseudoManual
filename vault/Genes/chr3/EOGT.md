---
symbol: "EOGT"
type: "gene"
col: 8680
ensembl_id: "ENSG00000163378"
name: "EGF domain specific O-linked N-acetylglucosamine transferase"
location: "3p14.1"
module: 38
arm: "+"
pooled_cpm: 24.05
n_lines_expressing: 49
n_dd_up: 6
n_dd_down: 12
n_dd_up_clean: 5
n_dd_down_clean: 10
in_vector_space: true
direction_upstream: 0
direction_downstream: 1
tags: ["gene", "module/038"]
generated_by: "tahoemap"
---

# EOGT

*EGF domain specific O-linked N-acetylglucosamine transferase* — 3p14.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 6 drug-doses (1 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.26× (z +5.5, q 2e-05, up in 23 of 46 measured lines).
> Pooled over the cell lines (median), lowered significantly by 12 drug-doses (2 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 0.392× (z -16.3, q 0e+00, down in 44 of 47 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CCDC62]] (+0.72, fdr 1e-05), [[LINC02936]] (+0.68, fdr 1e-05), [[RRH]] (+0.67, fdr 7e-06); moves opposite to [[CFD]] (-0.56, fdr 8e-05), [[ISCA2]] (-0.54, fdr 2e-04).
> It is in [[Module 038]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): none points to it; 1 goes from it, the strongest it → [[IDI2-AS1]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, 1 with an alert ⚠. 6 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8680.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.26×** | +5.5 | 2e-05 | 23/46 (MIA PaCa-2, A498, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.32×** | +4.6 | 0.001 | 19/44 (HT-29, A498, …) | rises with dose | cell-cycle shift (explains ~2% here) |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **1.29×** | +4.5 | 0.001 | 18/46 (A-172, RPMI-7951, …) | rises with dose | cell-cycle shift (explains ~1% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.28×** | +4.3 | 0.002 | 21/47 (SW480, LoVo, …) | top dose only |  |
| [[PF-06260933 (drug)]] 5 µM |  | **1.46×** | +3.5 | 0.058 | 10/45 (NCI-H2347, HOP62, …) | top dose only | noisy plate (z scaled) |
| [[palbociclib (drug)]] 0.5 µM |  | **1.31×** | +3.3 | 0.078 | 4/47 (A498, SW480, …) | inconsistent across doses | cell-cycle shift (explains ~12% here); noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 3 with an alert ⚠. 12 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 8680.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **0.392×** | -16.3 | 0e+00 | 44/47 (SW480, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.416×** | -15.2 | 0e+00 | 46/47 (LOX-IMVI, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.451×** | -13.9 | 2e-41 | 43/47 (LOX-IMVI, SW480, …) | rises with dose | cell-cycle shift (explains ~2% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.639×** | -7.8 | 9e-13 | 32/47 (LOX-IMVI, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **0.714×** | -5.9 | 5e-07 | 28/46 (SW1417, A498, …) | rises with dose | cell-cycle shift (explains ~3% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **0.793×** | -5.5 | 4e-06 | 22/47 (LOX-IMVI, NCI-H2347, …) | rises with dose |  |
| [[Brivudine (drug)]] 5 µM |  | **0.571×** | -5.1 | 3e-05 | 19/47 (A-172, A498, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Infigratinib (drug)]] 0.05 µM |  | **0.721×** | -4.5 | 5e-04 | 14/47 (MIA PaCa-2, hTERT-HPNE, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Pralsetinib (drug)]] 5 µM |  | **0.647×** | -4.0 | 0.005 | 16/46 (NCI-H1792, SHP-77, …) | top dose only | noisy plate (z scaled) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | **0.810×** | -3.6 | 0.015 | 15/47 (PANC-1, HOP62, …) | all doses, flat |  |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **0.807×** | -3.6 | 0.017 | 18/47 (NCI-H2030, AN3 CA, …) | rises with dose | composition shift |
| [[Darinaparsin (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~18% of this change | 0.859× | -3.5 | 0.019 | 13/47 (NCI-H661, KATO III, …) | top dose only |  |
| [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~11% of this change | **0.817×** | -3.5 | 0.020 | 16/47 (A498, A549, …) | rises with dose |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | 0.834× | -3.0 | 0.091 | 11/46 (NCI-H23, A-427, …) | all doses, flat |  |
| [[Trametinib (drug)]] 0.05 µM |  | 0.880× | -3.0 | 0.091 | 12/47 (PANC-1, Hs 766T, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.02 per unit of S-phase module lfc, -0.09 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8680. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[RKO (line)]] | wt | 51.1 | 0 | 4 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.429× (z -9.9) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.325× (z -9.8) |
| [[LOX-IMVI (line)]] | wt | 40.0 | 0 | 3 | — | [[Panobinostat (drug)]] 0.5 µM 0.220× (z -13.3) |
| [[SW480 (line)]] | alt | 18.7 | 0 | 3 | — | [[Panobinostat (drug)]] 5 µM 0.247× (z -12.5) |
| [[AN3 CA (line)]] | alt | 36.1 | 0 | 2 | — | [[L-Eflornithine (monohydrochloride) (drug)]] 0.5 µM 0.0959× (z -10.0) |
| [[HOP62 (line)]] | alt | 30.2 | 0 | 2 (1 ⚠) | — | [[Lonafarnib (drug)]] 5 µM 0.111× (z -9.4) ⚠ toxic · without an alert: [[Panobinostat (drug)]] 5 µM 0.332× (z -9.0) |
| [[HS-578T (line)]] | alt | 29.6 | 0 | 2 | — | [[Panobinostat (drug)]] 0.5 µM 0.287× (z -9.4) |
| [[hTERT-HPNE (line)]] | wt | 38.7 | 0 | 2 | — | [[Belinostat (drug)]] 5 µM 0.197× (z -9.6) |
| [[NCI-H1573 (line)]] | alt | 36.2 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.237× (z -9.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.290× (z -8.5) |
| [[Panc 03.27 (line)]] | alt | 27.0 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.196× (z -12.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.323× (z -8.9) |
| [[A549 (line)]] | wt | 22.9 | 0 | 1 | — | [[Panobinostat (drug)]] 5 µM 0.209× (z -10.9) |
| [[HCT15 (line)]] | alt | 25.5 | 0 | 1 | — | [[Afatinib (drug)]] 0.05 µM 0.178× (z -9.9) |
| [[HepG2_C3A (line)]] | wt | 23.0 | 0 | 1 | — | [[Pemetrexed (drug)]] 5 µM 0.159× (z -8.9) |
| [[J82 (line)]] | alt | 23.8 | 0 | 1 | — | [[Panobinostat (drug)]] 5 µM 0.372× (z -8.6) |
| [[MIA PaCa-2 (line)]] | alt | 19.3 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.77× (z +9.0) | — |
| [[NCI-H1792 (line)]] | alt | 16.7 | 0 | 1 | — | [[Pralsetinib (drug)]] 5 µM 0.0664× (z -8.8) |
| [[NCI-H2030 (line)]] | alt | 48.3 | 0 | 1 | — | [[Panobinostat (drug)]] 5 µM 0.365× (z -10.7) |
| [[NCI-H460 (line)]] | wt | 19.1 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.385× (z -8.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[PANC-1 (line)]] | alt | 22.9 | 0 | 1 | — | [[Panobinostat (drug)]] 0.5 µM 0.414× (z -8.8) |
| [[SW 900 (line)]] | alt | 23.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.0993× (z -12.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[SW1417 (line)]] | alt | 21.7 | 0 | 1 | — | [[Belinostat (drug)]] 0.5 µM 0.260× (z -10.7) |
| [[A-172 (line)]] | wt | 17.7 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 21.3 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 18.1 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 15.2 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 5.91 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 29.3 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 22.8 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 12.1 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 22.4 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 13.7 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 24.8 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 29.7 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 19.9 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 12.3 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 16.3 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 30.8 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 13.9 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 27.8 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 21.3 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 28.1 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 25.0 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 28.6 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 34.3 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 20.4 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 30.2 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 29.8 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 18.6 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 28.6 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 28.3 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 23.4 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8680), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*98 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CCDC62]] | +0.72 | +0.57 / +0.64 | both halves | 1e-05 |  |
| [[LINC02936]] | +0.68 | +0.52 / +0.54 | both halves | 1e-05 |  |
| [[RRH]] | +0.67 | +0.60 / +0.59 | both halves | 7e-06 |  |
| [[GABRR2]] | +0.67 | +0.59 / +0.56 | both halves | 1e-05 |  |
| [[ARL9]] | +0.67 | +0.53 / +0.60 | both halves | 1e-05 |  |
| [[KLRA1P]] | +0.67 | +0.45 / +0.54 | both halves | 3e-05 |  |
| [[SLC9A5]] | +0.67 | +0.48 / +0.56 | both halves | 2e-05 |  |
| [[NEU3]] | +0.66 | +0.60 / +0.57 | both halves | 1e-05 |  |
| [[ADCY10P1]] | +0.65 | +0.57 / +0.53 | both halves | 1e-05 |  |
| [[CCDC168]] | +0.65 | +0.63 / +0.59 | both halves | 7e-06 |  |
| [[MSH4]] | +0.64 | +0.33 / +0.49 | both halves | 1e-04 |  |
| [[TMED6]] | +0.64 | +0.55 / +0.44 | both halves | 3e-05 |  |

## Genes that move opposite

*2 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CFD]] | -0.56 | -0.41 / -0.37 | both halves | 8e-05 |  |
| [[ISCA2]] | -0.54 | -0.31 / -0.44 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

None: no arrow points to this gene.

### Downstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[IDI2-AS1]] | C | EOGT's natural level weakens IDI2-AS1's drug response | EOGT's natural level across 47 lines (lineage-adjusted; a glimpse) | r -0.64, reverse +0.11; direction not clear | 0.062 | ⚠ tissue can mimic it; precision caveat; direction unclear |

## Where it sits

- **Module**: [[Module 038]]; 122 genes; every member is in the + arm (projection on the module's main direction 0.634). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.28; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (30.3, -16.9); signed map (14.0, 7.5). **Vector** length 93.1, 19.8% of its response variance represented; |z| ≥ 3 in 877 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +7.5 | +5.5 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +6.3 | +4.6 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | +6.0 | +1.1 |
|  | [[Auranofin (drug)]] 5 µM |  | +5.8 | +4.3 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift | +4.9 | +2.0 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | +2.8 | +1.0 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | +2.3 | +2.8 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.1 | +0.2 |
|  | [[S-Adenosyl-L-methionine (disulfate tosylate) (drug)]] 5 µM |  | +2.1 | +2.1 |
| fall | [[Panobinostat (drug)]] 0.5 µM |  | -5.1 | -15.2 |
|  | [[Belinostat (drug)]] 5 µM |  | -4.6 | -13.9 |
|  | [[Panobinostat (drug)]] 5 µM |  | -4.2 | -16.3 |
|  | [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift | -2.9 | -0.8 |
|  | [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift | -2.7 | -2.0 |
|  | [[Brivudine (drug)]] 5 µM |  | -2.3 | -5.1 |
|  | [[Belumosudil (drug)]] 5 µM |  | -2.2 | -0.8 |
|  | [[Radotinib (drug)]] 5 µM |  | -2.1 | -2.2 |
|  | [[Infigratinib (drug)]] 0.05 µM |  | -2.1 | -4.5 |
|  | [[Lonafarnib (drug)]] 0.05 µM |  | -2.0 | -2.8 |

## What is on record

|  |  |
|---|---|
| Name | EGF domain specific O-linked N-acetylglucosamine transferase |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 3p14.1 — chr3:68,975,217-69,013,684 (-) |
| Ensembl biotype | protein_coding |
| Also known as | AER61, FLJ33770; previously C3orf64 |
| Gene groups (HGNC) | O-linked N-acetylglucosaminyltransferases |
| Matched by | ensembl_id |

**Function**, from UniProt [Q5NDL2](https://www.uniprot.org/uniprotkb/Q5NDL2) (EGF domain-specific O-linked N-acetylglucosamine transferase):

> Catalyzes the transfer of a single N-acetylglucosamine from UDP-GlcNAc to a serine or threonine residue in extracellular proteins resulting in their modification with a beta-linked N-acetylglucosamine (O-GlcNAc). Specifically glycosylates the Thr residue located between the fifth and sixth conserved cysteines of folded EGF-like domains.

**Summary**, from NCBI Gene [285203](https://www.ncbi.nlm.nih.gov/gene/285203):

> This gene encodes an enzyme that acts in the lumen of the endoplasmic reticulum to catalyze the transfer of N-acetylglucosamine to serine or threonine residues of extracellular-targeted proteins. This enzyme modifies proteins containing eukaryotic growth factor (EGF)-like domains, including the Notch receptor, thereby regulating developmental signalling. Mutations in this gene have been observed in individuals with Adams-Oliver syndrome 4. Alternative splicing results in multiple transcript …

**Accessions** — [HGNC:28526](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:28526) · Entrez [285203](https://www.ncbi.nlm.nih.gov/gene/285203) · UniProt [Q5NDL2](https://www.uniprot.org/uniprotkb/Q5NDL2) · Ensembl [ENSG00000163378](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000163378)

## Data

Gene col 8680: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8680); `tables/drug_effects.parquet` (21 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8680, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8680]; `tensor/DDL_lfc|DDL_z.npy` [8680]; `embed/gene_vectors.npy` [8680]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8680 or target_col == 8680). Every well: [[EOGT — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/EOGT.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
