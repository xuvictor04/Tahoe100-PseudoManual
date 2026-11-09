---
symbol: "ERFL"
type: "gene"
col: 15586
ensembl_id: "ENSG00000268041"
name: "ETS repressor factor like"
location: "19q13.2"
module: 38
arm: "+"
pooled_cpm: 2.38
n_lines_expressing: 50
n_dd_up: 14
n_dd_down: 10
n_dd_up_clean: 9
n_dd_down_clean: 5
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/038"]
generated_by: "tahoemap"
---

# ERFL

*ETS repressor factor like* — 19q13.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 14 drug-doses (5 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 2.70× (z +8.5, q 9e-15, up in 0 of 4 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Auranofin (drug)]] 5 µM: 2.44× (z +8.4, q 1e-14, up in 24 of 39 measured lines).
> Pooled over the cell lines (median), lowered significantly by 10 drug-doses (5 with an alert ⚠); the strongest is [[Harringtonine (drug)]] 5 µM: 0.410× (z -7.6, q 8e-12, down in 23 of 37 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[HYPK]] (+0.65, fdr 1e-05), [[PNPLA7]] (+0.62, fdr 2e-05), [[COL20A1]] (+0.62, fdr 1e-05); moves opposite to [[NT5DC1]] (-0.52, fdr 2e-05).
> It is in [[Module 038]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[GAL3ST1]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 6 with an alert ⚠. 14 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 15586.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.70×** | +8.5 | 9e-15 | 0/4 | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Auranofin (drug)]] 5 µM |  | **2.44×** | +8.4 | 1e-14 | 24/39 (HCT15, HT-29, …) | top dose only | position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.76×** | +7.5 | 1e-11 | 10/32 (A549, NCI-H460, …) | top dose only | cell-cycle shift (explains ~0% here); position effect removed |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.48×** | +5.2 | 3e-05 | 13/33 (NCI-H460, NCI-H1573, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.81×** | +5.2 | 3e-05 | 0/6 | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.59×** | +4.3 | 0.001 | 1/13 (HEC-1-A) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **2.00×** | +3.4 | 0.049 | 1/10 (A-172) | inconsistent across doses | cell-cycle shift (explains ~17% here); noisy plate (z scaled) |
| [[XRK3F2 (drug)]] 0.5 µM |  | **1.66×** | +3.4 | 0.049 | 1/14 (BT-474) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled); position effect removed |
| [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM |  | **1.43×** | +3.4 | 0.049 | 3/22 (Panc 03.27, A498, …) | inconsistent across doses | low cells (technical?); position effect removed |
| [[Procainamide (hydrochloride) (drug)]] 0.05 µM |  | **1.46×** | +3.3 | 0.058 | 3/34 (AsPC-1, A498, …) | inconsistent across doses | position effect removed |
| [[Bosentan (hydrate) (drug)]] 5 µM |  | **1.46×** | +3.2 | 0.058 | 3/23 (AsPC-1, NCI-H460, …) | top dose only | position effect removed |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.41×** | +3.2 | 0.058 | 1/14 (A549) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Lidocaine (hydrochloride) (drug)]] 0.5 µM |  | **1.40×** | +3.1 | 0.072 | 1/26 (PANC-1) | inconsistent across doses |  |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.10× | +3.1 | 0.072 | 5/44 (HOP62, MIA PaCa-2, …) | inconsistent across doses |  |
| [[Belinostat (drug)]] 0.5 µM |  | **1.38×** | +3.1 | 0.086 | 6/28 (LS 180, NCI-H1573, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 6 with an alert ⚠. 10 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 15586.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Harringtonine (drug)]] 5 µM |  | **0.410×** | -7.6 | 8e-12 | 23/37 (SW480, HOP62, …) | rises with dose | cell-cycle shift (explains ~21% here); composition shift; position effect removed |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.444×** | -7.6 | 8e-12 | 24/43 (NCI-H2030, HOP62, …) | rises with dose | cell-cycle shift (explains ~10% here); position effect removed |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change | **0.521×** | -6.1 | 2e-07 | 14/22 (HOP62, HEC-1-A, …) | all doses, stronger at high dose | position effect removed |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **0.546×** | -5.7 | 2e-06 | 17/40 (BT-474, H4, …) | all doses, stronger at high dose | position effect removed |
| [[(S)-Crizotinib (drug)]] 0.05 µM |  | **0.542×** | -5.3 | 1e-05 | 12/42 (CFPAC-1, C-33 A, …) | inconsistent across doses |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **0.600×** | -4.8 | 2e-04 | 17/39 (SW480, NCI-H23, …) | all doses, stronger at high dose |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~43% of this change | **0.601×** | -4.8 | 2e-04 | 16/44 (AsPC-1, H4, …) | all doses, stronger at high dose | composition shift |
| [[Cytarabine (hydrochloride) (drug)]] 5 µM |  | **0.616×** | -4.1 | 0.002 | 6/39 (AsPC-1, SW 900, …) | top dose only | cell-cycle shift (explains ~10% here); position effect removed |
| [[Atazanavir (sulfate) (drug)]] 0.5 µM |  | **0.679×** | -3.6 | 0.018 | 9/33 (AsPC-1, HOP62, …) | two highest doses |  |
| [[Carbidopa (monohydrate) (drug)]] 0.05 µM | ⚠ unreliable plate only; position not correctable | **0.686×** | -3.5 | 0.024 | 8/43 (Hs 766T, SNU-423, …) | inconsistent across doses |  |
| [[Ribociclib (drug)]] 0.05 µM | ⚠ unreliable plate only; position not correctable | 0.724× | -3.0 | 0.13 | 8/42 (SW1417, A549, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.34 per unit of S-phase module lfc, -0.22 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 15586. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HOP62 (line)]] | alt | 4.48 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.0849× (z -8.5) ⚠ toxic; cell-cycle shift, explains ~52% of this change |
| [[NCI-H2030 (line)]] | alt | 2.33 | 0 | 1 | — | [[Harringtonine (drug)]] 0.5 µM 0.0315× (z -9.7) |
| [[SW480 (line)]] | alt | 2.11 | 0 | 1 | — | [[Saquinavir (drug)]] 0.5 µM 0.0904× (z -8.7) |
| [[A-172 (line)]] | wt | 3.71 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 1.96 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 2.52 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 3.53 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 0.909 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 2.24 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 3.76 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 2.52 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 1.10 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 1.58 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 1.27 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 2.36 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 3.57 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 5.36 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 4.52 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 0.862 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 0.808 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 3.65 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 4.84 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 2.66 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 0.933 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 3.81 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 5.92 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 1.44 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 1.34 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 2.57 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 1.48 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 0.774 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 1.78 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 3.22 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 1.92 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 1.11 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 2.55 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 1.78 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 2.37 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 0.948 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 1.72 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 3.90 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 1.20 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 0.633 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 1.99 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 1.17 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 2.46 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 2.00 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 1.76 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 1.02 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 3.48 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 15586), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*99 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[HYPK]] | +0.65 | +0.51 / +0.69 | both halves | 1e-05 |  |
| [[PNPLA7]] | +0.62 | +0.47 / +0.63 | both halves | 2e-05 |  |
| [[COL20A1]] | +0.62 | +0.55 / +0.64 | both halves | 1e-05 |  |
| [[MYO15A]] | +0.61 | +0.57 / +0.56 | both halves | 1e-05 |  |
| [[ASIC4]] | +0.60 | +0.51 / +0.62 | both halves | 1e-05 |  |
| [[TMEM225B]] | +0.60 | +0.60 / +0.59 | both halves | 7e-06 |  |
| [[FLRT1]] | +0.60 | +0.56 / +0.60 | both halves | 1e-05 |  |
| [[C17orf100]] | +0.58 | +0.48 / +0.65 | both halves | 2e-05 |  |
| [[TMEM269]] | +0.57 | +0.51 / +0.57 | both halves | 1e-05 |  |
| [[L3MBTL1]] | +0.57 | +0.50 / +0.60 | both halves | 1e-05 |  |
| [[SLC9A5]] | +0.56 | +0.52 / +0.58 | both halves | 1e-05 |  |
| [[HYAL1]] | +0.56 | +0.50 / +0.53 | both halves | 1e-05 |  |

## Genes that move opposite

*1 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NT5DC1]] | -0.52 | -0.50 / -0.48 | both halves | 2e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[GAL3ST1]] | B | GAL3ST1 activity raises ERFL's level | lines that do not express GAL3ST1 (5) vs lines expressing it (45) | 1.55× lower at baseline in the lines without GAL3ST1 | 0.069 | ⚠ within organs, on part of the lines; also absent: ID2, ENSG00000275993; maybe low, not absent |
| [[PANX2]] | B | PANX2 activity raises ERFL's level | lines that do not express PANX2 (9) vs lines expressing it (41) | 1.32× lower at baseline in the lines without PANX2 | 0.078 | ⚠ within organs, on part of the lines; also absent: APBA2, CABYR; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 038]]; 122 genes; every member is in the + arm (projection on the module's main direction 0.528). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.28; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (35.5, -21.6); signed map (13.0, 13.0). **Vector** length 51.2, 6.68% of its response variance represented; |z| ≥ 3 in 1,035 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Auranofin (drug)]] 5 µM |  | +4.6 | +8.4 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +4.3 | +7.5 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +3.6 | +5.2 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +3.6 | +8.5 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +3.3 | +5.2 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +1.6 | +2.5 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | +1.4 | +0.6 |
|  | [[Temsirolimus (drug)]] 0.5 µM |  | +1.3 | +1.0 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.2 | +2.7 |
| fall | [[Harringtonine (drug)]] 0.5 µM |  | -4.0 | -7.6 |
|  | [[Harringtonine (drug)]] 5 µM |  | -3.0 | -7.6 |
|  | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~27% of this change | -2.5 | -5.7 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~43% of this change | -2.4 | -4.8 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -2.0 | -2.7 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -1.5 | -1.6 |
|  | [[Berbamine (drug)]] 0.05 µM |  | -1.4 | -3.0 |
|  | [[Relugolix (drug)]] 0.5 µM |  | -1.3 | -1.4 |
|  | [[Diammonium Glycyrrhizinate (drug)]] 0.05 µM |  | -1.3 | -1.7 |

## What is on record

|  |  |
|---|---|
| Name | ETS repressor factor like |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 19q13.2 — chr19:41,907,704-41,928,449 (-) |
| Ensembl biotype | protein_coding |
| Also known as | erfl1 |
| Matched by | ensembl_id |

UniProt [A0A1W2PQ73](https://www.uniprot.org/uniprotkb/A0A1W2PQ73) carries no function annotation.

**Summary**, from NCBI Gene [390937](https://www.ncbi.nlm.nih.gov/gene/390937):

> Predicted to enable DNA-binding transcription factor activity, RNA polymerase II-specific. Predicted to be involved in cell differentiation and regulation of transcription by RNA polymerase II. Predicted to be active in nucleus. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:53894](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:53894) · Entrez [390937](https://www.ncbi.nlm.nih.gov/gene/390937) · UniProt [A0A1W2PQ73](https://www.uniprot.org/uniprotkb/A0A1W2PQ73) · Ensembl [ENSG00000268041](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000268041)

## Data

Gene col 15586: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 15586); `tables/drug_effects.parquet` (26 rows, flagged included); `relations/gene_relations.parquet` (col_a == 15586, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 15586]; `tensor/DDL_lfc|DDL_z.npy` [15586]; `embed/gene_vectors.npy` [15586]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 15586 or target_col == 15586). Every well: [[ERFL — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ERFL.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
