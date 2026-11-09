---
symbol: "UFM1"
type: "gene"
col: 4203
ensembl_id: "ENSG00000120686"
name: "ubiquitin fold modifier 1"
location: "13q13.3"
module: 56
arm: "+"
pooled_cpm: 122.67
n_lines_expressing: 50
n_dd_up: 12
n_dd_down: 11
n_dd_up_clean: 10
n_dd_down_clean: 10
in_vector_space: true
direction_upstream: 1
direction_downstream: 1
tags: ["gene", "module/056"]
generated_by: "tahoemap"
---

# UFM1

*ubiquitin fold modifier 1* — 13q13.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 12 drug-doses (2 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 1.58× (z +6.5, q 4e-08, up in 38 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 11 drug-doses (1 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 0.5 µM: 0.643× (z -6.3, q 8e-08, down in 37 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SERP1]] (+0.74, fdr 7e-06), [[SEC22B]] (+0.74, fdr 7e-06), [[PGM3]] (+0.73, fdr 7e-06); moves opposite to [[MARK2]] (-0.57, fdr 2e-05), [[TET3]] (-0.53, fdr 1e-05).
> It is in [[Module 056]], a single-armed module (Asparagine N-linked glycosylation).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[AGR2]] → it (grade B ⚠); 1 goes from it, the strongest it → cells under [[Anethole trithione (drug)]] 0.5 µM (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 2 with an alert ⚠. 12 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4203.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.58×** | +6.5 | 4e-08 | 38/48 (J82, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.52×** | +5.9 | 8e-07 | 36/48 (NCI-H23, J82, …) | rises with dose | cell-cycle shift (explains ~1% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.45×** | +4.9 | 2e-04 | 32/45 (NCI-H460, C-33 A, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.38×** | +4.6 | 7e-04 | 32/48 (NCI-H1573, hTERT-HPNE, …) | inconsistent across doses | cell-cycle shift (explains ~18% here) |
| [[TAK-901 (drug)]] 5 µM |  | **1.79×** | +4.4 | 0.001 | 29/49 (RPMI-7951, hTERT-HPNE, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~3% here); composition shift; noisy plate (z scaled) |
| [[Auranofin (drug)]] 5 µM |  | **1.34×** | +4.2 | 0.003 | 33/48 (SHP-77, AN3 CA, …) | rises with dose |  |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.31×** | +3.8 | 0.011 | 28/48 (J82, NCI-H2030, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **1.21×** | +3.7 | 0.017 | 24/49 (MIA PaCa-2, SK-MEL-2, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **1.28×** | +3.5 | 0.026 | 26/48 (PANC-1, SNU-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here) |
| [[Abemaciclib (drug)]] 5 µM |  | **1.60×** | +3.5 | 0.026 | 30/48 (SHP-77, SW1417, …) | rises with dose | noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.26×** | +3.3 | 0.045 | 28/48 (HepG2/C3A, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here) |
| [[Abemaciclib (drug)]] 0.5 µM |  | **1.37×** | +3.2 | 0.062 | 27/48 (LoVo, MIA PaCa-2, …) | rises with dose | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 1 with an alert ⚠. 11 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 4203.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 0.5 µM |  | **0.643×** | -6.3 | 8e-08 | 37/48 (CFPAC-1, HT-29, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.644×** | -6.3 | 8e-08 | 41/48 (AsPC-1, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.702×** | -5.1 | 7e-05 | 34/48 (AsPC-1, CFPAC-1, …) | rises with dose | cell-cycle shift (explains ~17% here); position effect removed |
| [[Berbamine (drug)]] 0.05 µM |  | **0.762×** | -3.9 | 0.013 | 30/48 (MIA PaCa-2, LS 180, …) | inconsistent across doses |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~21% of this change | **0.817×** | -3.9 | 0.013 | 27/49 (LoVo, HCT15, …) | top dose only |  |
| [[Belumosudil (drug)]] 5 µM |  | **0.761×** | -3.8 | 0.015 | 28/48 (NCI-H2347, J82, …) | top dose only |  |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **0.775×** | -3.7 | 0.020 | 29/48 (HOP62, AsPC-1, …) | inconsistent across doses |  |
| [[Busulfan (drug)]] 0.05 µM |  | **0.798×** | -3.2 | 0.079 | 27/49 (HT-29, A-172, …) | inconsistent across doses |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.799×** | -3.2 | 0.079 | 24/48 (CFPAC-1, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here) |
| [[(R)-Verapamil (hydrochloride) (drug)]] 0.05 µM |  | **0.802×** | -3.2 | 0.087 | 22/49 (NCI-H2122, SW480, …) | inconsistent across doses |  |
| [[Cobimetinib (drug)]] 5 µM |  | **0.799×** | -3.1 | 0.097 | 21/47 (Panc 03.27, SW 1271, …) | rises with dose |  |
| [[Megestrol (drug)]] 0.05 µM |  | 0.810× | -3.0 | 0.11 | 23/48 (HT-29, H4, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.17 per unit of S-phase module lfc, +0.16 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4203. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 93.8 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.89× (z +8.6) ⚠ cell-cycle shift, would explain all of this change | — |
| [[J82 (line)]] | alt | 237 | 1 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.28× (z +10.2) | — |
| [[NCI-H1573 (line)]] | alt | 111 | 1 | 0 | [[Homoharringtonine (drug)]] 0.5 µM 2.77× (z +9.2) | — |
| [[NCI-H2030 (line)]] | alt | 91.6 | 1 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.77× (z +9.1) | — |
| [[NCI-H23 (line)]] | alt | 93.0 | 1 (1 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 2.51× (z +8.9) ⚠ toxic; transcription drop | — |
| [[NCI-H2347 (line)]] | alt | 120 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.569× (z -9.9) ⚠ cell-cycle shift, would explain all of this change |
| [[A-427 (line)]] | wt | 47.8 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 200 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 103 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 90.1 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 176 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 64.1 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 67.0 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 77.6 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 103 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 113 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 289 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 165 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 187 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 86.4 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 89.3 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 114 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 223 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 135 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 176 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 158 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 171 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 132 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 135 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 125 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 81.8 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 70.6 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 113 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 89.3 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 134 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 90.6 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 142 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 83.5 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 113 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 183 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 65.0 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 63.0 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 114 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 97.4 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 163 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 129 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 134 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 104 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 115 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 144 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4203), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*98 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SERP1]] | +0.74 | +0.73 / +0.67 | both halves | 7e-06 | pathway: HALLMARK_MTORC1_SIGNALING |
| [[SEC22B]] | +0.74 | +0.77 / +0.76 | both halves | 7e-06 |  |
| [[PGM3]] | +0.73 | +0.80 / +0.63 | both halves | 7e-06 |  |
| [[DNAJC25]] | +0.73 | +0.76 / +0.63 | both halves | 7e-06 |  |
| [[TMEM263]] | +0.69 | +0.74 / +0.65 | both halves | 7e-06 |  |
| [[SRP54]] | +0.68 | +0.75 / +0.62 | both halves | 7e-06 |  |
| [[SEC31A]] | +0.67 | +0.68 / +0.70 | both halves | 7e-06 |  |
| [[KDELR2]] | +0.67 | +0.71 / +0.64 | both halves | 7e-06 |  |
| [[OSTC]] | +0.67 | +0.70 / +0.61 | both halves | 7e-06 |  |
| [[SEC24A]] | +0.66 | +0.68 / +0.66 | both halves | 7e-06 |  |
| [[TVP23C]] | +0.66 | +0.66 / +0.66 | both halves | 7e-06 |  |
| [[COG6]] | +0.66 | +0.70 / +0.67 | both halves | 7e-06 |  |

## Genes that move opposite

*2 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MARK2]] | -0.57 | -0.48 / -0.61 | both halves | 2e-05 |  |
| [[TET3]] | -0.53 | -0.51 / -0.50 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[AGR2]] | B | AGR2 activity raises UFM1's level | lines that do not express AGR2 (32) vs lines expressing it (18) | 1.29× lower at baseline in the lines without AGR2 | 0.069 | ⚠ within organs, on part of the lines; also absent: FXYD3, SERPINB5, PRKCH-AS1 |

### Downstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| cells under [[Anethole trithione (drug)]] 0.5 µM | C | UFM1's natural level raises the cells' numbers under Anethole trithione 0.5 µM (protects the cells) | UFM1's natural level across 48 lines (lineage-adjusted; a glimpse) | r +0.59 | 0.475 over the table, 0.098 within its drug-dose | ⚠ within its drug-dose only (a lead); tissue can mimic it |

## Where it sits

- **Module**: [[Module 056]] — Asparagine N-linked glycosylation; 87 genes; every member is in the + arm (projection on the module's main direction 0.710). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.33; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (12.6, -35.3); signed map (-51.4, 12.3). **Vector** length 110, 38.1% of its response variance represented; |z| ≥ 3 in 874 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *Asparagine N-linked glycosylation* (reactome, mean cos +0.57 to 23); *ER to Golgi Anterograde Transport* (reactome, mean cos +0.59 to 16); *Transport to the Golgi and subsequent modification* (reactome, mean cos +0.59 to 16).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Auranofin (drug)]] 5 µM |  | +5.5 | +4.2 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +4.7 | +4.9 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift | +4.4 | +2.4 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift | +4.0 | +1.3 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +3.3 | +4.6 |
|  | [[Terfenadine (drug)]] 5 µM |  | +2.6 | +2.6 |
|  | [[Abemaciclib (drug)]] 5 µM |  | +2.6 | +3.5 |
|  | [[EX229 (drug)]] 0.05 µM |  | +2.3 | +2.9 |
|  | [[S-Adenosyl-L-methionine (disulfate tosylate) (drug)]] 5 µM |  | +2.0 | +1.7 |
| fall | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | -4.1 | -1.1 |
|  | [[PH-797804 (drug)]] 5 µM |  | -4.1 | +2.2 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | -3.6 | +1.4 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | -3.3 | -2.2 |
|  | [[TAK-901 (drug)]] 5 µM |  | -3.0 | +4.4 |
|  | [[Belumosudil (drug)]] 5 µM |  | -3.0 | -3.8 |
|  | [[Retinoic acid (drug)]] 0.05 µM |  | -2.8 | -2.7 |
|  | [[Berbamine (drug)]] 0.05 µM |  | -2.8 | -3.9 |

## What is on record

|  |  |
|---|---|
| Name | ubiquitin fold modifier 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 13q13.3 — chr13:38,349,849-38,363,619 (+) |
| Ensembl biotype | protein_coding |
| Also known as | bA131P10.1; previously C13orf20 |
| Hallmark sets | MTORC1_SIGNALING |
| Matched by | ensembl_id |

**Function**, from UniProt [P61960](https://www.uniprot.org/uniprotkb/P61960) (Ubiquitin-fold modifier 1):

> Ubiquitin-like modifier which can be covalently attached via an isopeptide bond to lysine residues of substrate proteins as a monomer or a lysine-linked polymer. The so-called ufmylation, requires the UFM1-activating E1 enzyme UBA5, the UFM1-conjugating E2 enzyme UFC1, and the UFM1-ligase E3 enzyme UFL1. Ufmylation is involved in various processes, such as ribosome recycling, response to DNA damage, transcription or reticulophagy (also called ER-phagy) induced in response to endoplasmic …

**Summary**, from NCBI Gene [51569](https://www.ncbi.nlm.nih.gov/gene/51569):

> UFM1 is a ubiquitin-like protein that is conjugated to target proteins by E1-like activating enzyme UBA5 (UBE1DC1; MIM 610552) and E2-like conjugating enzyme UFC1 (MIM 610554) in a manner analogous to ubiquitylation (see UBE2M; MIM 603173) (Komatsu et al., 2004 [PubMed 15071506]).[supplied by OMIM, Dec 2008]

**Accessions** — [HGNC:20597](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:20597) · Entrez [51569](https://www.ncbi.nlm.nih.gov/gene/51569) · UniProt [P61960](https://www.uniprot.org/uniprotkb/P61960) · Ensembl [ENSG00000120686](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000120686)

## Data

Gene col 4203: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4203); `tables/drug_effects.parquet` (24 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4203, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4203]; `tensor/DDL_lfc|DDL_z.npy` [4203]; `embed/gene_vectors.npy` [4203]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4203 or target_col == 4203). Every well: [[UFM1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/UFM1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
