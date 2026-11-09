---
symbol: "GMPPA"
type: "gene"
col: 6901
ensembl_id: "ENSG00000144591"
name: "GDP-mannose pyrophosphorylase A"
location: "2q35"
module: 49
arm: "+"
pooled_cpm: 18.75
n_lines_expressing: 50
n_dd_up: 0
n_dd_down: 25
n_dd_up_clean: 0
n_dd_down_clean: 14
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/049"]
generated_by: "tahoemap"
---

# GMPPA

*GDP-mannose pyrophosphorylase A* — 2q35

## At a glance

> [!summary] In this data
> No drug-dose raises it significantly in the pooled (median-over-lines) data.
> Pooled over the cell lines (median), lowered significantly by 25 drug-doses (11 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.346× (z -19.3, q 0e+00, down in 44 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SEC24D]] (+0.82, fdr 7e-06), [[MANF]] (+0.78, fdr 7e-06), [[SSR2]] (+0.77, fdr 7e-06).
> It is in [[Module 049]], a single-armed module (XBP1(S) activates chaperone genes).

## Drugs that raise it

No drug-dose raises it in the pooled data (pooled over the cell lines, median: none with |z| ≥ 3 or q < 0.10). A response seen in fewer than about half of the measured lines does not reach the pooled data; see [[#In which cell lines]].

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 26 in all, 11 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 25 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 11 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 6901.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.346×** | -19.3 | 0e+00 | 44/47 (NCI-H2030, HS-578T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.394×** | -13.9 | 3e-41 | 39/48 (C32, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here); composition shift; position effect removed |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.454×** | -11.7 | 2e-29 | 36/46 (hTERT-HPNE, H4, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.473×** | -11.1 | 1e-26 | 44/48 (C-33 A, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.474×** | -11.1 | 1e-26 | 35/48 (H4, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here); position effect removed |
| [[Harringtonine (drug)]] 5 µM |  | **0.577×** | -7.9 | 4e-13 | 31/47 (NCI-H2347, C32, …) | rises with dose | cell-cycle shift (explains ~19% here); composition shift; position effect removed |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.599×** | -7.6 | 2e-12 | 28/46 (SW 900, C32, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.708×** | -6.7 | 1e-09 | 30/48 (hTERT-HPNE, RPMI-7951, …) | rises with dose |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.658×** | -6.0 | 1e-07 | 28/43 (H4, HepG2/C3A, …) | top dose only | cell-cycle shift (explains ~23% here) |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **0.676×** | -5.8 | 3e-07 | 23/48 (HT-29, HS-578T, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change | **0.684×** | -5.1 | 1e-05 | 20/34 (LoVo, NCI-H1573, …) | inconsistent across doses | composition shift |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~38% of this change | **0.715×** | -5.0 | 3e-05 | 23/48 (NCI-H1792, NCI-H1573, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~36% of this change | **0.735×** | -4.6 | 2e-04 | 20/48 (HS-578T, A498, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.676×** | -4.5 | 2e-04 | 20/48 (A-427, RPMI-7951, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[TAK-901 (drug)]] 5 µM |  | **0.586×** | -4.2 | 0.001 | 18/48 (CFPAC-1, MIA PaCa-2, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~17% here); composition shift; noisy plate (z scaled) |
| [[Selinexor (drug)]] 5 µM |  | **0.804×** | -3.9 | 0.003 | 16/48 (NCI-H1792, KATO III, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.790×** | -3.5 | 0.013 | 18/48 (H4, KATO III, …) | two highest doses |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 0.5 µM |  | **0.792×** | -3.5 | 0.014 | 12/47 (SNU-1, SW 1088, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Brivudine (drug)]] 5 µM |  | **0.652×** | -3.3 | 0.021 | 13/48 (HS-578T, NCI-H1573, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Rapamycin (drug)]] 0.5 µM |  | **0.801×** | -3.3 | 0.023 | 14/48 (Panc 03.27, SW 900, …) | rises with dose |  |
| [[Rapamycin (drug)]] 5 µM |  | 0.843× | -2.9 | 0.078 | 8/48 (Hs 766T, RPMI-7951, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.19 per unit of S-phase module lfc, -0.14 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6901. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[C32 (line)]] | wt | 38.2 | 0 | 7 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.145× (z -14.6) |
| [[H4 (line)]] | wt | 27.7 | 0 | 6 (4 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.0298× (z -17.8) |
| [[hTERT-HPNE (line)]] | wt | 20.1 | 0 | 4 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0411× (z -16.0) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.138× (z -12.0) |
| [[NCI-H2347 (line)]] | alt | 18.6 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.184× (z -16.5) |
| [[SW480 (line)]] | alt | 18.2 | 0 | 4 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.199× (z -12.3) |
| [[HS-578T (line)]] | alt | 28.0 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.186× (z -16.8) |
| [[A-172 (line)]] | wt | 22.2 | 0 | 2 (1 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.147× (z -12.9) ⚠ cell-cycle shift, explains ~38% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.289× (z -10.6) |
| [[C-33 A (line)]] | alt | 11.2 | 0 | 2 | — | [[Digitoxin (drug)]] 0.5 µM 0.0459× (z -13.1) |
| [[HOP62 (line)]] | alt | 15.0 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.258× (z -11.4) |
| [[KATO III (line)]] | alt | 31.2 | 0 | 2 | — | [[Digitoxin (drug)]] 0.5 µM 0.181× (z -10.9) |
| [[LoVo (line)]] | wt | 20.9 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.0952× (z -13.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change |
| [[NCI-H1573 (line)]] | alt | 23.1 | 0 | 2 (1 ⚠) | — | [[Digitoxin (drug)]] 0.5 µM 0.256× (z -10.0) |
| [[A498 (line)]] | wt | 26.6 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.258× (z -16.3) |
| [[A549 (line)]] | wt | 11.8 | 0 | 1 (1 ⚠) | — | [[Lonafarnib (drug)]] 5 µM 0.0552× (z -8.5) ⚠ toxic |
| [[AN3 CA (line)]] | alt | 12.3 | 0 | 1 | — | [[Sinomenine (drug)]] 0.5 µM 0.0457× (z -8.5) |
| [[CFPAC-1 (line)]] | alt | 18.1 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.308× (z -9.4) |
| [[HCT15 (line)]] | alt | 40.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.156× (z -8.5) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[J82 (line)]] | alt | 9.47 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.276× (z -8.6) |
| [[LOX-IMVI (line)]] | wt | 8.89 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.186× (z -11.6) |
| [[NCI-H1792 (line)]] | alt | 22.6 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.159× (z -13.6) |
| [[NCI-H2030 (line)]] | alt | 23.6 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.183× (z -17.2) |
| [[NCI-H460 (line)]] | wt | 14.0 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.318× (z -8.5) |
| [[Panc 03.27 (line)]] | alt | 12.9 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.276× (z -8.6) |
| [[RPMI-7951 (line)]] | alt | 26.1 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.224× (z -11.5) |
| [[SK-MEL-2 (line)]] | alt | 11.4 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.130× (z -11.7) |
| [[SNU-1 (line)]] | wt | 18.5 | 0 | 1 | — | [[Pyridoxine (drug)]] 0.5 µM 0.128× (z -8.8) |
| [[SNU-423 (line)]] | alt | 17.9 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.315× (z -8.7) |
| [[SW 900 (line)]] | alt | 26.5 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.135× (z -12.7) |
| [[A-427 (line)]] | wt | 11.9 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 17.4 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 11.9 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 9.54 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 23.2 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 10.6 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 15.6 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 20.7 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 21.3 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 21.3 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 13.8 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 18.0 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 20.5 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 17.6 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 10.9 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 15.8 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 16.0 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 11.5 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 39.4 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 20.7 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 19.2 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 19.2 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6901), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SEC24D]] | +0.82 | +0.81 / +0.75 | both halves | 7e-06 | pathway: Asparagine N-linked glycosylation |
| [[MANF]] | +0.78 | +0.81 / +0.70 | both halves | 7e-06 | **novel candidate** |
| [[SSR2]] | +0.77 | +0.78 / +0.71 | both halves | 7e-06 |  |
| [[SRP54]] | +0.77 | +0.78 / +0.72 | both halves | 7e-06 |  |
| [[DNAJC25]] | +0.77 | +0.76 / +0.73 | both halves | 7e-06 |  |
| [[TMEM39A]] | +0.77 | +0.79 / +0.68 | both halves | 7e-06 |  |
| [[ACBD3]] | +0.76 | +0.78 / +0.71 | both halves | 7e-06 |  |
| [[TXNDC11]] | +0.76 | +0.74 / +0.73 | both halves | 7e-06 |  |
| [[EIF2AK3]] | +0.76 | +0.76 / +0.70 | both halves | 7e-06 |  |
| [[MED8]] | +0.76 | +0.78 / +0.69 | both halves | 7e-06 |  |
| [[COG6]] | +0.75 | +0.76 / +0.69 | both halves | 7e-06 | pathway: Asparagine N-linked glycosylation |
| [[COPG1]] | +0.75 | +0.82 / +0.67 | both halves | 7e-06 | pathway: Asparagine N-linked glycosylation |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 049]] — XBP1(S) activates chaperone genes; 93 genes; every member is in the + arm (projection on the module's main direction 0.839). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.12; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (12.1, -34.1); signed map (-51.5, 11.3). **Vector** length 102, 24.5% of its response variance represented; |z| ≥ 3 in 913 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *XBP1(S) activates chaperone genes* (reactome, mean cos +0.65 to 8); *IRE1alpha activates chaperones* (reactome, mean cos +0.65 to 8); *Unfolded Protein Response (UPR)* (reactome, mean cos +0.65 to 8).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[venetoclax (drug)]] 5 µM |  | +2.7 | +2.3 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.7 | -0.3 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +2.6 | +0.6 |
|  | [[Sapanisertib (drug)]] 0.5 µM |  | +2.6 | +2.6 |
|  | [[Abemaciclib (drug)]] 0.5 µM |  | +2.3 | +2.2 |
|  | [[Abemaciclib (drug)]] 5 µM |  | +2.1 | +2.0 |
| fall | [[Digitoxin (drug)]] 0.5 µM |  | -5.9 | -11.1 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | -5.4 | -11.1 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | -4.6 | -11.7 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | -4.3 | -13.9 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | -3.0 | -19.3 |
|  | [[Rapamycin (drug)]] 5 µM |  | -2.9 | -2.9 |
|  | [[Temsirolimus (drug)]] 0.05 µM |  | -2.8 | -2.6 |
|  | [[Berbamine (drug)]] 0.05 µM |  | -2.7 | -2.2 |
|  | [[Retinoic acid (drug)]] 0.05 µM |  | -2.4 | -2.4 |
|  | [[Busulfan (drug)]] 0.05 µM |  | -2.3 | -2.3 |

## What is on record

|  |  |
|---|---|
| Name | GDP-mannose pyrophosphorylase A |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 2q35 — chr2:219,498,865-219,513,898 (+) |
| Ensembl biotype | protein_coding |
| Hallmark sets | GLYCOLYSIS |
| Reactome | 4 pathways, smallest: Synthesis of GDP-mannose; Synthesis of substrates in N-glycan biosythesis; Biosynthesis of the N-glycan precursor (dolichol lipid-linked oligosaccharide, LLO) and transfer to a nascent protein |
| Matched by | ensembl_id |

**Function**, from UniProt [Q96IJ6](https://www.uniprot.org/uniprotkb/Q96IJ6) (Mannose-1-phosphate guanylyltransferase regulatory subunit alpha):

> Regulatory subunit of the GMPPA-GMPPB mannose-1-phosphate guanylyltransferase complex; reduces the catalytic activity of GMPPB when part of the complex. Mediates allosteric feedback inhibition of GMPPB catalytic activity upon binding GDP-alpha-D-mannose. Together with GMPPB regulates GDP-alpha-D-mannose levels.

**Summary**, from NCBI Gene [29926](https://www.ncbi.nlm.nih.gov/gene/29926):

> This gene is thought to encode a GDP-mannose pyrophosphorylase. This enzyme catalyzes the reaction which converts mannose-1-phosphate and GTP to GDP-mannose which is involved in the production of N-linked oligosaccharides. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:22923](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:22923) · Entrez [29926](https://www.ncbi.nlm.nih.gov/gene/29926) · UniProt [Q96IJ6](https://www.uniprot.org/uniprotkb/Q96IJ6) · Ensembl [ENSG00000144591](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000144591)

## Data

Gene col 6901: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6901); `tables/drug_effects.parquet` (26 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6901, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6901]; `tensor/DDL_lfc|DDL_z.npy` [6901]; `embed/gene_vectors.npy` [6901]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6901 or target_col == 6901). Every well: [[GMPPA — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/GMPPA.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
