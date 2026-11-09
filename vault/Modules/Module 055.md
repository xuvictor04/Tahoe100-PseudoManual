---
module: 55
type: "module"
n_genes: 87
n_plus: 87
n_minus: 0
arms_opposite: false
mean_cos_between_arms: -0.31351912021636963
label: "Regulation of FZD by ubiquitination"
label_source: "reactome"
tags: ["module"]
generated_by: "tahoemap"
---

# Module 055

*Regulation of FZD by ubiquitination · 87 genes (single-armed) · [[Module 055.canvas|open the canvas]]*

A module is a community of the gene graph that links each gene to its 15 strongest partners by |cos| that are replicated (`both halves`: same sign, fdr ≤ 0.10, in two random halves of the compounds) or very strong in one random half (`graph/`). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.31; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.

Label from the validation stage: **Regulation of FZD by ubiquitination** (reactome, q 0.043; `validation/module_labels.csv`).

## Enriched for

*Hypergeometric test per arm, BH q (`validation/module_enrichment.csv`).*

| Arm | Set | Source | Overlap | Fold | q |
|---|---|---|---|---|---|
| all | Regulation of FZD by ubiquitination | reactome | 3/87 | 30.6 | 0.043 |
| + | Regulation of FZD by ubiquitination | reactome | 3/87 | 30.6 | 0.043 |

## Drugs that move it

*Mean pooled z of its genes (`graph/module_pooled_z.npy`, row 54), drug-doses with |z| ≥ 1: the 10 strongest, and any of the 10 strongest without an alert beyond them. ⚠ = the drug-dose's artifact flags: the module may move because of what the drug-dose did to the cells (cell death, a drop in transcription, a shift in the cell-cycle mix, ...); shown, not left out.*

- Raise it: [[Dinaciclib (drug)]] 5 µM (+8.5, ⚠ toxic; transcription drop; cell-cycle shift); [[Dinaciclib (drug)]] 0.5 µM (+8.1, ⚠ toxic; transcription drop; cell-cycle shift); [[Dinaciclib (drug)]] 0.05 µM (+6.2, ⚠ toxic; transcription drop; cell-cycle shift); [[Tucidinostat (drug)]] 5 µM (+4.6); [[Idarubicin (hydrochloride) (drug)]] 5 µM (+4.6, ⚠ cell-cycle shift); [[Tucidinostat (drug)]] 0.5 µM (+3.1, ⚠ cell-cycle shift); [[Docetaxel (drug)]] 0.05 µM (+2.6, ⚠ transcription drop; cell-cycle shift); [[Ipatasertib (drug)]] 0.5 µM (+2.1); [[Selinexor (drug)]] 5 µM (+2.1, ⚠ cell-cycle shift); [[Lonafarnib (drug)]] 5 µM (+2.0, ⚠ toxic); [[XRK3F2 (drug)]] 0.5 µM (+1.9); [[Entrectinib (drug)]] 5 µM (+1.8); [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM (+1.7); [[Filgotinib (drug)]] 5 µM (+1.5); [[Ponatinib (drug)]] 0.5 µM (+1.5); [[Carbamazepine (drug)]] 5 µM (+1.4); [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM (+1.4); [[Bendamustine (drug)]] 5 µM (+1.2) (50 in all, 18 with an alert ⚠; shown: the 10 strongest and the 8 next strongest without an alert)
- Lower it: [[Digitoxin (drug)]] 0.5 µM (-4.6, ⚠ cell-cycle shift); [[Ouabain (Octahydrate) (drug)]] 5 µM (-4.4, ⚠ cell-cycle shift); [[Homoharringtonine (drug)]] 0.5 µM (-3.2, ⚠ cell-cycle shift); [[Harringtonine (drug)]] 5 µM (-2.8, ⚠ cell-cycle shift); [[Belinostat (drug)]] 5 µM (-2.8, ⚠ cell-cycle shift); [[Ouabain (Octahydrate) (drug)]] 0.5 µM (-2.8, ⚠ cell-cycle shift); [[Panobinostat (drug)]] 0.5 µM (-2.3, ⚠ cell-cycle shift); [[Harringtonine (drug)]] 0.5 µM (-1.9, ⚠ cell-cycle shift); [[c-Kit-IN-1 (drug)]] 0.05 µM (-1.9, ⚠ unreliable plate only); [[Digitoxin (drug)]] 0.05 µM (-1.9, ⚠ cell-cycle shift); [[Mebendazole (drug)]] 5 µM (-1.9); [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM (-1.7); [[Lucanthone (drug)]] 0.05 µM (-1.6); [[PH-797804 (drug)]] 5 µM (-1.6); [[Vinblastine (sulfate) (drug)]] 5 µM (-1.6); [[Erlotinib (drug)]] 0.05 µM (-1.5); [[Artesunate (drug)]] 0.5 µM (-1.5); [[BAY1125976 (drug)]] 5 µM (-1.4); [[Ixazomib citrate (drug)]] 0.5 µM (-1.4); [[Rutin (trihydrate) (drug)]] 0.05 µM (-1.4) (54 in all, 18 with an alert ⚠; shown: the 10 strongest and the 10 next strongest without an alert)

## Cell lines where it responds most

*The lines with the largest mean |module score| over the module's 8 strongest drug-doses (`graph/modules.parquet` responsive_lines), strongest first.*

- [[COLO 205 (line)]], [[LoVo (line)]], [[LS 180 (line)]], [[SW480 (line)]], [[SW48 (line)]], [[RKO (line)]], [[KATO III (line)]], [[SNU-1 (line)]]

## + arm (87)

| Gene | Projection | Name |
|---|---|---|
| [[LINC01819]] | 0.925 | long independently transcribed non-coding RNA 1819 |
| [[C9orf152]] | 0.899 | chromosome 9 open reading frame 152 |
| [[GPX2]] | 0.893 | glutathione peroxidase 2 |
| [[EDAR]] | 0.892 | ectodysplasin A receptor |
| [[EPS8L3]] | 0.878 | EPS8 signaling adaptor L3 |
| [[HNF4A]] | 0.871 | hepatocyte nuclear factor 4 alpha |
| [[IL20RA]] | 0.870 | interleukin 20 receptor subunit alpha |
| [[BMP4]] | 0.867 | bone morphogenetic protein 4 |
| [[CLRN3]] | 0.854 | clarin 3 |
| [[TPRXL]] | 0.840 | tetrapeptide repeat homeobox like (pseudogene) |
| [[MYO7B]] | 0.839 | myosin VIIB |
| [[KCNE3]] | 0.833 | potassium voltage-gated channel subfamily E regulatory subunit 3 |
| [[ABO]] | 0.823 | ABO, alpha 1-3-N-acetylgalactosaminyltransferase and alpha 1-3-galactosyltransferase |
| [[SKAP1]] | 0.812 | src kinase associated phosphoprotein 1 |
| [[VILL]] | 0.793 | villin like |
| [[SYK]] | 0.791 | spleen associated tyrosine kinase |
| [[INPP5D]] | 0.787 | inositol polyphosphate-5-phosphatase D |
| [[LINC01559]] | 0.784 | long independently transcribed non-coding RNA 1559 |
| [[TNFRSF14-AS1]] | 0.783 | TNFRSF14 antisense RNA 1 |
| [[LGR6]] | 0.782 | leucine rich repeat containing G protein-coupled receptor 6 |
| [[NPSR1-AS1]] | 0.781 | NPSR1 antisense RNA 1 |
| [[SLC52A3]] | 0.781 | solute carrier family 52 member 3 |
| [[RNF43]] | 0.774 | ring finger protein 43 |
| [[TSPOAP1]] | 0.773 | TSPO associated protein 1 |
| [[USH1C]] | 0.769 | USH1 protein network component harmonin |
| [[ZNF503-AS1]] | 0.769 | ZNF503 antisense RNA 1 |
| [[HSD17B2]] | 0.767 | hydroxysteroid 17-beta dehydrogenase 2 |
| [[SLC5A1]] | 0.766 | solute carrier family 5 member 1 |
| [[LINC03040]] | 0.758 | long independently transcribed non-coding RNA 3040 |
| [[ZBTB7C]] | 0.741 | zinc finger and BTB domain containing 7C |
| [[VSNL1]] | 0.734 | visinin like 1 |
| [[ADGRG5]] | 0.724 | adhesion G protein-coupled receptor G5 |
| [[AFAP1L2]] | 0.723 | actin filament associated protein 1 like 2 |
| [[KCNH8]] | 0.720 | potassium voltage-gated channel subfamily H member 8 |
| [[DENND2D]] | 0.714 | DENN domain containing 2D |
| [[KLK6]] | 0.711 | kallikrein related peptidase 6 |
| [[MROH7]] | 0.709 | maestro heat like repeat family member 7 |
| [[SLC6A14]] | 0.700 | solute carrier family 6 member 14 |
| [[LGR5]] | 0.694 | leucine rich repeat containing G protein-coupled receptor 5 |
| [[TFF3]] | 0.689 | trefoil factor 3 |
| [[CADPS]] | 0.686 | calcium dependent secretion activator |
| [[PIK3AP1]] | 0.676 | phosphoinositide-3-kinase adaptor protein 1 |
| [[SEMA4G]] | 0.676 | semaphorin 4G |
| [[FUT2]] | 0.675 | fucosyltransferase 2 (H blood group) |
| [[CYP2S1]] | 0.668 | cytochrome P450 family 2 subfamily S member 1 |
| [[BCAR3-AS1]] | 0.656 | BCAR3 antisense RNA 1 |
| [[LINC01956]] | 0.653 | long independently transcribed non-coding RNA 1956 |
| [[TNFSF15]] | 0.651 | TNF superfamily member 15 |
| [[GRIN2B]] | 0.650 | glutamate ionotropic receptor NMDA type subunit 2B |
| [[ALDH1L1]] | 0.649 | aldehyde dehydrogenase 1 family member L1 |
| [[LINC02580]] | 0.648 | long independently transcribed non-coding RNA 2580 |
| [[HR]] | 0.644 | HR lysine demethylase and nuclear receptor corepressor |
| [[KCTD14]] | 0.633 | potassium channel tetramerization domain containing 14 |
| [[FOXQ1]] | 0.632 | forkhead box Q1 |
| [[SULT1C2]] | 0.631 | sulfotransferase family 1C member 2 |
| [[FAM83F]] | 0.628 | scaffolding CK1 anchoring protein F |
| [[DNAJC15]] | 0.615 | DnaJ heat shock protein family (Hsp40) member C15 |
| [[HPGD]] | 0.607 | 15-hydroxyprostaglandin dehydrogenase |
| [[SPINT1-AS1]] | 0.600 | SPINT1 antisense RNA 1 |
| [[PIWIL1]] | 0.586 | piwi like RNA-mediated gene silencing 1 |
| [[IQGAP2]] | 0.580 | IQ motif containing GTPase activating protein 2 |
| [[FAM221A]] | 0.567 | family with sequence similarity 221 member A |
| [[HCN1]] | 0.566 | hyperpolarization activated cyclic nucleotide gated potassium channel 1 |
| [[LINC01290]] | 0.562 | long independently transcribed non-coding RNA 1290 |
| [[KBTBD12]] | 0.556 | kelch repeat and BTB domain containing 12 |
| [[PLS1]] | 0.546 | plastin 1 |
| [[LPAR5]] | 0.546 | lysophosphatidic acid receptor 5 |
| [[MGST2]] | 0.535 | microsomal glutathione S-transferase 2 |
| [[SPIRE2]] | 0.533 | spire type actin nucleation factor 2 |
| [[ABHD12B]] | 0.523 | abhydrolase domain containing 12B |
| [[UGT8]] | 0.519 | UDP glycosyltransferase 8 |
| [[SYDE1]] | -0.517 | synapse defective Rho GTPase activating protein 1 |
| [[SLC27A2]] | 0.512 | solute carrier family 27 member 2 |
| [[XK]] | 0.500 | X-linked Kx blood group antigen, Kell and VPS13A binding protein |
| [[STXBP6]] | 0.494 | syntaxin binding protein 6 |
| [[MYOM3]] | 0.483 | myomesin 3 |
| [[LINC02405]] | 0.476 | long independently transcribed non-coding RNA 2405 |
| [[RNF128]] | 0.473 | ring finger protein 128 |
| [[MCF2L]] | 0.473 | MCF.2 cell line derived transforming sequence like |
| [[SNTB1]] | 0.471 | syntrophin beta 1 |
| [[DNAJC22]] | 0.467 | DnaJ heat shock protein family (Hsp40) member C22 |
| [[MFSD6]] | 0.455 | major facilitator superfamily domain containing 6 |
| [[GNB4]] | -0.447 | G protein subunit beta 4 |
| [[FAAH]] | 0.432 | fatty acid amide hydrolase |
| [[DYRK2]] | 0.375 | dual specificity tyrosine phosphorylation regulated kinase 2 |
| [[LYPD6B]] | 0.372 | LY6/PLAUR domain containing 6B |
| [[MAPK13]] | 0.366 | mitogen-activated protein kinase 13 |

## − arm (0)

None: a single-armed module.

## Data

- `graph/nodes.parquet` — module == 55; `graph/modules.parquet` — module == 55; `graph/edges.parquet` — both ends in the module; `graph/module_scores.npy` — [54] (drug-dose × line)
