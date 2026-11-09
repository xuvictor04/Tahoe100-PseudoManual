---
symbol: "PPM1N"
type: "gene"
col: 13143
ensembl_id: "ENSG00000213889"
name: "protein phosphatase, Mg2+/Mn2+ dependent 1N (putative)"
location: "19q13.32"
module: 21
arm: "+"
pooled_cpm: 4.27
n_lines_expressing: 49
n_dd_up: 17
n_dd_down: 6
n_dd_up_clean: 13
n_dd_down_clean: 5
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/021"]
generated_by: "tahoemap"
---

# PPM1N

*protein phosphatase, Mg2+/Mn2+ dependent 1N (putative)* — 19q13.32

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 17 drug-doses (4 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 2.33× (z +9.7, q 2e-19, up in 34 of 35 measured lines).
> Pooled over the cell lines (median), lowered significantly by 6 drug-doses (1 with an alert ⚠); the strongest is [[Digitoxin (drug)]] 0.5 µM: 0.536× (z -5.1, q 2e-04, down in 21 of 40 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ETFBKMT]] (+0.65, fdr 1e-05), [[CTDSPL2-DT]] (+0.64, fdr 7e-06), [[CAPN12]] (+0.64, fdr 1e-05); moves opposite to [[MTOR]] (-0.56, fdr 4e-05).
> It is in [[Module 021]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[NPHS1]] → it (grade C ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 17 in all, 4 with an alert ⚠. 17 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 13143.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.33×** | +9.7 | 2e-19 | 34/35 (HOP62, A498, …) | top dose only | cell-cycle shift (explains ~4% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.43×** | +9.6 | 2e-19 | 6/7 (SW480, HT-29, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **3.01×** | +8.9 | 1e-16 | 18/21 (LoVo, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **2.12×** | +8.6 | 1e-15 | 34/42 (HT-29, LS 180, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.95×** | +7.7 | 2e-12 | 20/37 (C32, HS-578T, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Selinexor (drug)]] 5 µM |  | **1.76×** | +6.4 | 1e-08 | 20/41 (RKO, AsPC-1, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~1% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **2.10×** | +6.0 | 1e-07 | 28/40 (KATO III, HT-29, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.14×** | +5.7 | 8e-07 | 8/14 (SW480, HT-29, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here); composition shift |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.97×** | +5.5 | 3e-06 | 23/42 (KATO III, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here) |
| [[Panobinostat (drug)]] 5 µM |  | **1.74×** | +4.5 | 4e-04 | 20/43 (KATO III, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here) |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.88×** | +3.6 | 0.018 | 5/32 (SW480, A498, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled); position effect removed |
| [[9-ING-41 (drug)]] 0.5 µM |  | **1.82×** | +3.4 | 0.032 | 10/36 (NCI-H460, KATO III, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Sunitinib (drug)]] 5 µM | ⚠ toxic | **1.49×** | +3.2 | 0.052 | 9/36 (NCI-H460, A549, …) | top dose only |  |
| [[XRK3F2 (drug)]] 0.5 µM |  | **1.76×** | +3.2 | 0.052 | 6/24 (PANC-1, AsPC-1, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Bimiralisib (drug)]] 0.5 µM |  | **1.76×** | +3.2 | 0.052 | 11/37 (AsPC-1, NCI-H23, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Celecoxib (drug)]] 0.5 µM |  | **1.72×** | +3.1 | 0.075 | 5/37 (SW480, NCI-H23, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Selinexor (drug)]] 0.5 µM |  | **1.46×** | +3.1 | 0.076 | 6/40 (HS-578T, SK-MEL-2, …) | rises with dose | cell-cycle shift (explains ~0% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, 1 with an alert ⚠. 6 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 13143.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 0.5 µM |  | **0.536×** | -5.1 | 2e-04 | 21/40 (LoVo, HT-29, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); position effect removed |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.565×** | -4.6 | 1e-03 | 16/42 (PANC-1, LoVo, …) | inconsistent across doses |  |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.594×** | -4.2 | 0.004 | 15/40 (SW480, MIA PaCa-2, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); position effect removed |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.610×** | -4.0 | 0.008 | 17/35 (RKO, SW480, …) | inconsistent across doses | cell-cycle shift (explains ~7% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **0.655×** | -3.4 | 0.066 | 8/42 (A549, SNU-1, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.663×** | -3.3 | 0.079 | 14/39 (KATO III, A-427, …) | all doses, flat | cell-cycle shift (explains ~0% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.17 per unit of S-phase module lfc, -0.10 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 13143. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HOP62 (line)]] | alt | 3.83 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.59× (z +8.8) | — |
| [[A-427 (line)]] | wt | 4.44 | 0 | 1 | — | [[Pentoxifylline (drug)]] 0.5 µM 0.0733× (z -8.7) |
| [[A498 (line)]] | wt | 3.35 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 10.2× (z +12.3) | — |
| [[C32 (line)]] | wt | 3.64 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 51.7× (z +14.1) | — |
| [[HS-578T (line)]] | alt | 3.41 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 23.9× (z +13.8) | — |
| [[HT-29 (line)]] | alt | 9.91 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.209× (z -9.4) |
| [[hTERT-HPNE (line)]] | wt | 3.57 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 9.55× (z +8.5) | — |
| [[KATO III (line)]] | alt | 5.28 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.0740× (z -8.6) |
| [[RPMI-7951 (line)]] | alt | 2.24 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 19.4× (z +9.1) | — |
| [[A-172 (line)]] | wt | 3.18 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 7.90 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 1.61 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 5.39 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 0.834 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 4.96 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 2.06 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 1.36 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 6.10 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 1.41 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 7.64 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 2.27 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 3.23 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 5.21 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 2.57 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 6.21 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 4.87 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 2.63 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 4.39 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 2.60 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 1.43 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 7.31 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 3.95 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 6.45 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 2.15 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 2.54 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 5.48 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 2.90 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 2.31 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 5.36 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 6.33 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 2.99 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 4.04 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 2.18 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 1.71 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 2.83 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 2.26 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 4.33 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 5.97 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 2.69 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 7.61 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 13143), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*99 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ETFBKMT]] | +0.65 | +0.53 / +0.69 | both halves | 1e-05 |  |
| [[CTDSPL2-DT]] | +0.64 | +0.66 / +0.67 | both halves | 7e-06 |  |
| [[CAPN12]] | +0.64 | +0.57 / +0.66 | both halves | 1e-05 |  |
| [[MYO1F]] | +0.63 | +0.47 / +0.69 | both halves | 2e-05 |  |
| [[RELA-DT]] | +0.62 | +0.61 / +0.62 | both halves | 7e-06 |  |
| [[WASL-DT]] | +0.62 | +0.41 / +0.74 | both halves | 4e-05 |  |
| [[LINC02175]] | +0.61 | +0.60 / +0.55 | both halves | 1e-05 |  |
| [[ACAP1]] | +0.61 | +0.56 / +0.66 | both halves | 1e-05 |  |
| [[TTC36-AS1]] | +0.61 | +0.63 / +0.59 | both halves | 7e-06 |  |
| [[CATSPERD]] | +0.61 | +0.59 / +0.63 | both halves | 7e-06 |  |
| [[CHMP3-AS1]] | +0.60 | +0.52 / +0.65 | both halves | 1e-05 |  |
| [[SEC1P]] | +0.59 | +0.66 / +0.57 | both halves | 1e-05 |  |

## Genes that move opposite

*1 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MTOR]] | -0.56 | -0.42 / -0.61 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[NPHS1]] | C | NPHS1 activity weakens PPM1N's drug response | lines that do not express NPHS1 (3) vs lines expressing it (39) | the lines without NPHS1 respond 1.25× as strongly (z diff -0.70); strongest at Tucidinostat 5 µM: 4.15x vs 2.14x (z diff -3.1) | 0.069 | ⚠ few lines (4 vs 46); across organs; co-occurs with CTNNB1; also absent: FSD1L, MYO5A, DPF1; maybe low, not absent; target measured in part of the lines; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 021]]; 188 genes; every member is in the + arm (projection on the module's main direction 0.629). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.33; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (12.8, 31.9); signed map (37.4, 2.9). **Vector** length 65.2, 11.7% of its response variance represented; |z| ≥ 3 in 848 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +5.9 | +8.6 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +5.5 | +6.0 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +4.5 | +9.7 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +4.4 | +9.6 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +4.2 | +8.9 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +2.3 | +3.2 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | +2.2 | +1.9 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +2.1 | +3.6 |
|  | [[Auranofin (drug)]] 5 µM |  | +1.9 | +2.8 |
| fall | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -3.5 | -4.6 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -3.0 | -2.0 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | -2.9 | -5.1 |
|  | [[Digitoxin (drug)]] 0.05 µM |  | -1.8 | -4.2 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift | -1.7 | -2.4 |
|  | [[Abemaciclib (drug)]] 0.5 µM |  | -1.7 | -2.3 |
|  | [[TAK-733 (drug)]] 5 µM |  | -1.7 | -2.0 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -1.6 | -1.4 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -1.6 | -1.8 |
|  | [[Fenofibrate (drug)]] 0.05 µM |  | -1.5 | -2.2 |

## What is on record

|  |  |
|---|---|
| Name | protein phosphatase, Mg2+/Mn2+ dependent 1N (putative) |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 19q13.32 — chr19:45,488,777-45,502,513 (+) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ40125 |
| Gene groups (HGNC) | Protein phosphatases, Mg2+/Mn2+ dependent |
| Matched by | ensembl_id |

UniProt [Q8N819](https://www.uniprot.org/uniprotkb/Q8N819) carries no function annotation.

**Summary**, from NCBI Gene [147699](https://www.ncbi.nlm.nih.gov/gene/147699):

> Predicted to enable protein serine/threonine phosphatase activity. Predicted to be involved in positive regulation of canonical Wnt signaling pathway and regulation of canonical NF-kappaB signal transduction. Predicted to be active in cytosol and nucleus. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:26845](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:26845) · Entrez [147699](https://www.ncbi.nlm.nih.gov/gene/147699) · UniProt [Q8N819](https://www.uniprot.org/uniprotkb/Q8N819) · Ensembl [ENSG00000213889](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000213889)

## Data

Gene col 13143: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 13143); `tables/drug_effects.parquet` (23 rows, flagged included); `relations/gene_relations.parquet` (col_a == 13143, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 13143]; `tensor/DDL_lfc|DDL_z.npy` [13143]; `embed/gene_vectors.npy` [13143]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 13143 or target_col == 13143). Every well: [[PPM1N — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PPM1N.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
