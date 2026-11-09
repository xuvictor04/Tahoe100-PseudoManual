---
symbol: "NDUFB3"
type: "gene"
col: 4036
ensembl_id: "ENSG00000119013"
name: "NADH:ubiquinone oxidoreductase subunit B3"
location: "2q33.1"
module: 58
arm: "+"
pooled_cpm: 21.48
n_lines_expressing: 50
n_dd_up: 14
n_dd_down: 1
n_dd_up_clean: 2
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/058"]
generated_by: "tahoemap"
---

# NDUFB3

*NADH:ubiquinone oxidoreductase subunit B3* — 2q33.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 14 drug-doses (12 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 3.12× (z +7.2, q 4e-10, up in 28 of 32 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~56% of this change. The strongest without an alert is [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM: 1.50× (z +3.8, q 0.012, up in 30 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 5 µM in 1 line (A549 10.9×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~56% of this change).
> Pooled over the cell lines (median), lowered significantly by 1 drug-dose (none with an alert); the strongest is [[GSK1059615 (drug)]] 5 µM: 0.307× (z -4.1, q 0.028, down in 40 of 46 measured lines).
> Its strongest partners by |cos| (88 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 24 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[NDUFA3]] (+0.73, fdr 1e-05), [[NDUFAB1]] (+0.67, fdr 7e-06), [[MTLN]] (+0.66, fdr 1e-05, ⚠ MTLN in the vector space only through flagged drug-doses), [[TRAPPC5]] (+0.65, fdr 1e-05); moves opposite to [[UBQLN4]] (-0.57, fdr 6e-05), [[CERS2]] (-0.55, fdr 7e-05), [[ADSS2]] (-0.55, fdr 4e-05).
> It is in [[Module 058]], a single-armed module (oxidative phosphorylation).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 13 with an alert ⚠. 14 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 12 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4036.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 5 µM in 1 line (A549 10.9×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~56% of this change).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~56% of this change | **3.12×** | +7.2 | 4e-10 | 28/32 (A549, A-172, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~57% of this change | **3.57×** | +6.7 | 5e-09 | 35/37 (A549, NCI-H460, …) | all doses, stronger at high dose | composition shift; noisy plate (z scaled) |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~45% of this change | **2.46×** | +5.9 | 7e-07 | 45/48 (HOP62, A549, …) | all doses, stronger at high dose |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~56% of this change | **2.30×** | +5.0 | 1e-04 | 28/36 (LOX-IMVI, MIA PaCa-2, …) | all doses, stronger at high dose | composition shift |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~67% of this change | **2.04×** | +4.7 | 3e-04 | 39/48 (MIA PaCa-2, HOP62, …) | all doses, stronger at high dose |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~52% of this change | **2.02×** | +4.6 | 4e-04 | 36/45 (NCI-H2347, HOP62, …) | inconsistent across doses | low cells (technical?); position effect removed |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~70% of this change | **1.91×** | +4.2 | 0.002 | 39/47 (A549, COLO 205, …) | rises with dose |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.50×** | +3.8 | 0.012 | 30/48 (A-172, HOP62, …) | top dose only |  |
| [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **1.74×** | +3.6 | 0.017 | 30/47 (A-172, SW 900, …) | rises with dose |  |
| [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~34% of this change | **2.81×** | +3.5 | 0.022 | 29/48 (LoVo, RPMI-7951, …) | rises with dose | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Arbutin (drug)]] 5 µM |  | **1.70×** | +3.4 | 0.041 | 29/46 (SW 900, COLO 205, …) | top dose only | position effect removed |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.65×** | +3.2 | 0.074 | 25/42 (CFPAC-1, MIA PaCa-2, …) | top dose only | cell-cycle shift (explains ~20% here); position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~38% of this change | **1.40×** | +3.1 | 0.074 | 21/46 (AsPC-1, NCI-H2347, …) | top dose only |  |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.16× | +3.1 | 0.074 | 9/48 (BT-474, J82, …) | inconsistent across doses |  |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~94% of this change | **1.64×** | +3.1 | 0.074 | 23/47 (A549, MIA PaCa-2, …) | rises with dose | composition shift; position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 3 in all, none with an alert. 1 of them lowers it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 4036.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[GSK1059615 (drug)]] 5 µM |  | **0.307×** | -4.1 | 0.028 | 40/46 (H4, COLO 205, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Sapanisertib (drug)]] 5 µM |  | 0.390× | -3.2 | 0.34 | 30/48 (LS 180, SW480, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Hydroxyurea (drug)]] 5 µM |  | 0.617× | -3.1 | 0.39 | 24/47 (HepG2/C3A, SNU-423, …) | top dose only | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.61 per unit of S-phase module lfc, +0.56 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4036. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A549 (line)]] | wt | 14.4 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 10.9× (z +10.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~56% of this change | — |
| [[A-172 (line)]] | wt | 20.6 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 20.2 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 30.0 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 14.6 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 20.8 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 13.6 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 10.8 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 16.4 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 20.4 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 12.9 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 20.4 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 16.3 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 18.4 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 16.9 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 15.2 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 13.4 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 15.0 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 17.7 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 23.9 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 13.4 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 28.3 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 24.2 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 19.7 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 16.4 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 26.6 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 11.8 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 15.5 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 11.7 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 105 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 14.6 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 20.3 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 18.4 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 23.0 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 17.9 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 33.4 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 13.7 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 17.0 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 19.2 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 19.8 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 22.6 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 15.5 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 14.3 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 10.5 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 20.8 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 18.6 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 22.9 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 24.3 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 11.5 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 20.5 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4036), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*92 of its nearest partners move with it, 24 of them with an alert (⚠; 12 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NDUFA3]] | +0.73 | +0.54 / +0.82 | both halves | 1e-05 | same gene group; pathway: HALLMARK_OXIDATIVE_PHOSPHORYLATION; STRING 999 |
| [[NDUFAB1]] | +0.67 | +0.62 / +0.64 | both halves | 7e-06 | same gene group; pathway: HALLMARK_OXIDATIVE_PHOSPHORYLATION; STRING 999 |
| [[MTLN]] ⚠ | +0.66 | +0.51 / +0.73 | both halves | 1e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[TRAPPC5]] | +0.65 | +0.55 / +0.64 | both halves | 1e-05 |  |
| [[C19orf53]] | +0.65 | +0.41 / +0.72 | both halves | 4e-05 |  |
| [[NDUFA7]] | +0.64 | +0.37 / +0.75 | both halves | 8e-05 | same gene group; pathway: HALLMARK_OXIDATIVE_PHOSPHORYLATION; STRING 999 |
| [[NDUFC2]] | +0.63 | +0.51 / +0.68 | both halves | 1e-05 | same gene group; pathway: HALLMARK_OXIDATIVE_PHOSPHORYLATION; STRING 999 |
| [[CHMP2A]] | +0.63 | +0.54 / +0.61 | both halves | 1e-05 |  |
| [[NDUFS5]] | +0.62 | +0.46 / +0.64 | both halves | 2e-05 | same gene group; pathway: Aerobic respiration and respiratory electron transport; STRING 999 |
| [[NDUFS8]] | +0.62 | +0.42 / +0.66 | both halves | 4e-05 | pathway: HALLMARK_OXIDATIVE_PHOSPHORYLATION; STRING 999 |
| [[VPS25]] | +0.62 | +0.57 / +0.65 | both halves | 1e-05 |  |
| [[COX5B]] | +0.62 | +0.40 / +0.68 | both halves | 5e-05 | pathway: HALLMARK_OXIDATIVE_PHOSPHORYLATION; STRING 977 |
| [[TMEM160]] | +0.62 | +0.35 / +0.64 | both halves | 1e-04 |  |

## Genes that move opposite

*8 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[UBQLN4]] | -0.57 | -0.38 / -0.59 | both halves | 6e-05 |  |
| [[CERS2]] | -0.55 | -0.38 / -0.57 | both halves | 7e-05 |  |
| [[ADSS2]] | -0.55 | -0.42 / -0.49 | both halves | 4e-05 |  |
| [[SBDSP1]] | -0.54 | -0.30 / -0.49 | both halves | 2e-04 |  |
| [[ELK4]] | -0.51 | -0.32 / -0.51 | both halves | 2e-04 |  |
| [[KLC2]] | -0.50 | -0.31 / -0.55 | both halves | 2e-04 |  |
| [[KCTD15]] | -0.50 | -0.36 / -0.44 | both halves | 1e-04 |  |
| [[SNHG22]] | -0.49 | -0.25 / -0.53 | both halves | 4e-04 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 058]] — oxidative phosphorylation; 80 genes; every member is in the + arm (projection on the module's main direction 0.634). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.35; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-49.1, -18.9); signed map (-37.2, 7.0). **Vector** length 63.2, 18.0% of its response variance represented; |z| ≥ 3 in 504 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *Cristae formation* (reactome, mean cos +0.51 to 4).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~34% of this change | +5.3 | +3.5 |
|  | [[PH-797804 (drug)]] 5 µM |  | +3.6 | +0.2 |
|  | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~27% of this change | +2.7 | +3.6 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~70% of this change | +2.0 | +4.2 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~45% of this change | +1.9 | +5.9 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.9 | +2.0 |
|  | [[Medroxyprogesterone acetate (drug)]] 0.5 µM |  | +1.7 | +1.5 |
|  | [[Verteporfin (drug)]] 5 µM |  | +1.6 | -0.1 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +1.5 | +3.8 |
| fall | [[Auranofin (drug)]] 5 µM |  | -3.1 | +0.3 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.5 | -0.2 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~56% of this change | -2.5 | +7.2 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~56% of this change | -2.4 | +5.0 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -2.3 | -1.0 |
|  | [[GSK1059615 (drug)]] 5 µM |  | -2.1 | -4.1 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -1.7 | -2.0 |
|  | [[Dihydroartemisinin (drug)]] 5 µM |  | -1.5 | -2.8 |
|  | [[Temsirolimus (drug)]] 0.5 µM |  | -1.5 | -1.1 |

## What is on record

|  |  |
|---|---|
| Name | NADH:ubiquinone oxidoreductase subunit B3 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 2q33.1 — chr2:201,071,433-201,085,750 (+) |
| Ensembl biotype | protein_coding |
| Also known as | B12 |
| Gene groups (HGNC) | NADH:ubiquinone oxidoreductase supernumerary subunits |
| Hallmark sets | OXIDATIVE_PHOSPHORYLATION |
| Reactome | 3 pathways, smallest: Complex I biogenesis; Respiratory electron transport; Aerobic respiration and respiratory electron transport |
| Matched by | ensembl_id |

**Function**, from UniProt [O43676](https://www.uniprot.org/uniprotkb/O43676) (NADH dehydrogenase):

> Accessory subunit of the mitochondrial membrane respiratory chain NADH dehydrogenase (Complex I), that is believed not to be involved in catalysis. Complex I functions in the transfer of electrons from NADH to the respiratory chain. The immediate electron acceptor for the enzyme is believed to be ubiquinone.

**Summary**, from NCBI Gene [4709](https://www.ncbi.nlm.nih.gov/gene/4709):

> This gene encodes an accessory subunit of the mitochondrial membrane respiratory chain NADH dehydrogenase (Complex I) which is the first enzyme in the electron transport chain of mitochondria. This protein localizes to the inner membrane of the mitochondrion as a single-pass membrane protein. Mutations in this gene contribute to mitochondrial complex 1 deficiency. Alternative splicing results in multiple transcript variants encoding the same protein. Humans have multiple pseudogenes of this …

**Accessions** — [HGNC:7698](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:7698) · Entrez [4709](https://www.ncbi.nlm.nih.gov/gene/4709) · UniProt [O43676](https://www.uniprot.org/uniprotkb/O43676) · Ensembl [ENSG00000119013](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000119013)

## Data

Gene col 4036: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4036); `tables/drug_effects.parquet` (18 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4036, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4036]; `tensor/DDL_lfc|DDL_z.npy` [4036]; `embed/gene_vectors.npy` [4036]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4036 or target_col == 4036). Every well: [[NDUFB3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/NDUFB3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
